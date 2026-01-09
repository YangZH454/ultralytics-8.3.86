import sys
import cv2
import numpy as np
import socket
import json
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QMessageBox, QSizePolicy
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QTimer
from ultralytics import YOLO
from main_window_ui import Ui_MainWindow

#封装三维矩阵转QImage的函数
def convert2QImage(img):
    #使用三个变量保存三维矩阵的三个维度具体值
    heigth, width, channel = img.shape
    #将获取到的三维矩阵参数作为QImage的构造函数传参
    return QImage(img, width, heigth, channel*width, QImage.Format.Format_BGR888)

#为了让界面能够显示 需要自行封装一个类 既可以调用show函数 又可以访问界面
#所以需要继承两个类
class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        #还需要手动调用QMainWindow的构造函数
        super(mainWindow, self).__init__()
        #页面绘制
        self.setupUi(self)
        #初始化基础模型
        self.model = YOLO("yolo11n.pt")
        #信号与槽绑定，将按钮被按下的信号与对应的槽函数进行绑定
        self.pushButton.clicked.connect(self.get_image_path)
        #调用页面初始化函数
        self.page_init()
        #摄像头初始化
        self.cap_init()
        #模型选择初始化
        self.model_init()
        #视频初始化
        self.video_init()
        #模型conf初始化
        self.model_conf_setting()
        #网络通信初始化
        self.network_init()
        #UI自适应初始化
        self.ui_adaptive_init()
        #让程序运行的初始界面处于第一页
        self.stackedWidget.setCurrentIndex(0)

    #页面初始化函数 填充combox控件的内容
    def page_init(self):
        self.comboBox_page.addItem("图像检测")
        self.comboBox_page.addItem("摄像头检测")
        self.comboBox_page.addItem("视频检测")
        #将combox页码变化信号与翻页函数进行绑定
        self.comboBox_page.currentIndexChanged.connect(self.page_choose)

    #翻页函数
    def page_choose(self):
        #先打印翻页函数调用后 combox_page的当前页码
        page = self.comboBox_page.currentIndex()
        #将stackedWidget的当前页码设置为combox_page的当前页码
        self.stackedWidget.setCurrentIndex(page)
        #翻页时需要关闭摄像头 关闭计时器 清空画布
        self.det_cap_label.clear()
        self.orig_cap_label.clear()
        self.det_img_label.clear()
        self.orig_img_label.clear()
        if self.cap.isOpened():
            print("翻页时关闭摄像头")
            self.pushButton_cap.setText("开启摄像头")
            self.cap.release()
            self.cap_timer.stop()
        #恢复窗口最小尺寸限制，允许手动调整
        self.setMinimumSize(0, 0)

    #模型切换初始化
    def model_init(self):
        #添加模型可选条目
        self.comboBox_model.addItem('基础模型')
        self.comboBox_model.addItem('自训练模型1')
        self.comboBox_model.addItem('表情情绪模型')
        #信号与槽绑定模型选择函数
        self.comboBox_model.currentIndexChanged.connect(self.model_choose)

    #模型切换实现操作
    def model_choose(self):
        #获取对应模型文字信息索引号
        page = self.comboBox_model.currentIndex()
        #根据页码索引号初始化对应的模型
        #第一页是基础模型
        if page == 0:
            self.model = YOLO('yolo11n.pt')
            print('基础模型')
        #第二页是自训练模型1
        elif page == 1:
            self.model = YOLO('runs/detect/train/weights/best.pt')
            print('自训练模型1')
        elif page == 2:
            self.model = YOLO('emotion.pt')
            

    #模型置信度阈值实施修改
    def model_conf_setting(self):
        #先自行设置一个conf的初始值
        self.model_conf = 0.25
        #在指定位置显示初始conf值
        self.label_conf.setText(f'模型置信度阈值：0.25')

        self.horizontalSlider_model.setValue(25)
        #滑动条在滑动时 会产生数值变化信号 将这个信号与conf修改函数进行绑定
        self.horizontalSlider_model.valueChanged.connect(self.conf_value_change)

    #滑动条数值变化槽函数
    def conf_value_change(self):
        #获取滑动条的数值
        value = self.horizontalSlider_model.value()
        #将滑动条的value除以100 用于模型检测conf值的范围
        #将conf值初始化为页面类的一个属性
        self.model_conf = value/100
        #将conf的变化值设置到label上
        self.label_conf.setText(f'模型置信度阈值：{value/100}')

    #图像路径获取函数
    def get_image_path(self):
        print("图像检测")
        #调用获取文件路径函数
        path = QFileDialog.getOpenFileName(filter="*.jpg; *.png")
        #判断path的第一个成员是否为空（用户是不是选择了文件）
        #没有必要强行判断path[0]是不是假 因为如果不是假 就是真
        if path[0]:
            #确保窗口大小不会因为图像内容而自动调整
            #保存当前窗口大小，防止自动调整
            current_size = self.size()
            self.setMinimumSize(current_size)
            #提取出元组中的文件路径
            image_path = path[0]
            #将图像路径传参给model对象
            result = self.model(source=image_path, verbose = False, conf = self.model_conf)
            #将检测结果提取 作为参数进行格式化打印
            self.detection_format_print(result[0])
            #将检测结果提取 作为参数进行锚框坐标格式化打印
            self.detection_box_format_print(result[0])
            #将检测结果打包并发送到服务器
            detection_data = self.detection_data_pack(result[0])
            self.send_detection_data(detection_data)
            #获取检测结果返回值中的图像矩阵
            orig_arr = result[0].orig_img
            det_arr = result[0].plot()
            #把两个图像矩阵显示在指定画布上
            self.detection_img_show(orig_arr, self.orig_img_label)
            self.detection_img_show(det_arr, self.det_img_label)

        #如果path[0]为空 代表用户没有选择文件，打印信息
        else:
            print("用户没有选择文件")
            QMessageBox.information(self, "消息", "用户未选择图像")

    #UI自适应初始化函数
    def ui_adaptive_init(self):
        #存储原始图像数据用于窗口大小变化时重新缩放
        self.image_pixmaps = {}
        #为所有图像显示Label设置自适应策略
        image_labels = [self.orig_img_label, self.det_img_label, 
                       self.orig_cap_label, self.det_cap_label,
                       self.orig_video_label, self.det_video_label]
        for label in image_labels:
            #设置大小策略为Expanding，但设置最小尺寸为0，防止内容过大时窗口自动拉大
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            label.setMinimumSize(0, 0)
            #设置对齐方式为居中
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            #不自动缩放内容，由我们手动控制
            label.setScaledContents(False)

    #检测结果显示 将传入的图像矩阵显示到指定的画布上 限制函数的传参类型
    def detection_img_show(self, arr:np.ndarray, place:QLabel):
        #将图像矩阵转换为QImage对象
        qimage_arr = convert2QImage(arr)
        #将QImage对象转换为QPixmap对象
        qpixmap_arr = QPixmap.fromImage(qimage_arr)
        #保存原始图像数据
        self.image_pixmaps[place] = qpixmap_arr
        #更新显示
        self.update_image_display(place)

    #更新图像显示函数
    def update_image_display(self, label:QLabel):
        #如果该label有保存的图像数据
        if label in self.image_pixmaps:
            pixmap = self.image_pixmaps[label]
            #获取label的当前可用大小
            label_size = label.size()
            #如果label大小有效，则缩放图像
            if label_size.width() > 0 and label_size.height() > 0:
                #使用label的当前大小进行缩放，确保不会超出label范围
                scaled_pixmap = pixmap.scaled(label_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                #设置pixmap，但不让它影响label的大小
                #使用setPixmap而不是setScaledContents，确保布局控制大小
                label.setPixmap(scaled_pixmap)

    #重写窗口大小变化事件
    def resizeEvent(self, event):
        #调用父类方法
        super().resizeEvent(event)
        #更新所有图像显示
        for label in self.image_pixmaps.keys():
            self.update_image_display(label)

    #摄像头初始化函数
    def cap_init(self):
        #初始化摄像头 此时无需传参
        self.cap = cv2.VideoCapture()
        #初始化摄像头图像获取时用的定时器
        self.cap_timer = QTimer()
        #初始化定时器的时间间隔
        self.cap_timer.setInterval(1)
        #摄像头开关按钮绑定槽函数
        self.pushButton_cap.clicked.connect(self.cap_operation)
        #将计时器计时一次结束后产生的信号与摄像头图像采集函数进行绑定
        self.cap_timer.timeout.connect(self.cap_image_detect)

    #摄像头开关操作函数
    def cap_operation(self):
        #判断摄像头的开关状态 如果为关闭状态 此时按按钮应该打开摄像头
        if self.cap.isOpened() == False:
            print("摄像头开启")
            #打开本地摄像头 需要摄像头编号以及采样模式
            ret = self.cap.open(0, cv2.CAP_DSHOW)
            #判断摄像头是否成功打开
            if ret:
                print("摄像头打开成功")
                #确保窗口大小不会因为摄像头图像而自动调整
                #保存当前窗口大小，防止自动调整
                current_size = self.size()
                self.setMinimumSize(current_size)
                #开启成功后 修改按钮文本信息为关闭 因为下一次按按钮就是做关闭操作了
                self.pushButton_cap.setText("关闭摄像头")
                #开启定时器 定时获取摄像头图像
                self.cap_timer.start()
            else:
                print("摄像头打开失败")
                #如果打开失败 就调用释放函数
                self.cap.release()
                #摄像头状态有误 定时器也需要关闭
                self.cap_timer.stop()
        #如果摄像头是打开状态 此时按按钮应该关闭摄像头
        else:
            print("摄像头关闭")
            self.cap.release()
            #如果正常开启摄像头 按钮文本改为开启
            self.pushButton_cap.setText("开启摄像头")
            #摄像头正常关闭 定时器也需要关闭
            self.cap_timer.stop()
            #显示画布需要清空
            self.orig_cap_label.clear()
            self.det_cap_label.clear()
            #清理保存的图像数据
            if self.orig_cap_label in self.image_pixmaps:
                del self.image_pixmaps[self.orig_cap_label]
            if self.det_cap_label in self.image_pixmaps:
                del self.image_pixmaps[self.det_cap_label]
<<<<<<< HEAD
=======
            #恢复窗口最小尺寸限制，允许手动调整
            self.setMinimumSize(0, 0)
>>>>>>> 93f972da0d14499d8377a82044990d3f6f93a762

    #摄像头图像采集函数
    def cap_image_detect(self):
        #使用read函数获取摄像头图像
        #返回值1：是否成功捕获到图像矩阵
        #返回值2：图像矩阵
        ret, arr = self.cap.read()
        #判断图像矩阵是否被读到
        if ret:
            arr = cv2.flip(arr, 1)
            #将摄像头采集到的单帧图像数据显示到左侧画布上
            self.detection_img_show(arr, self.orig_cap_label)
            #将图像矩阵作为模型检测的传参进行检测
            result = self.model(source = arr, verbose=False, conf = self.model_conf)
            self.detection_format_print(result[0])
            #将检测结果提取 作为参数进行锚框坐标格式化打印
            self.detection_box_format_print(result[0])
            #将检测结果打包并发送到服务器
            detection_data = self.detection_data_pack(result[0])
            self.send_detection_data(detection_data)
            #提取出检测图像矩阵
            det_arr = result[0].plot()
            #将检测结果显示到右侧画布上
            self.detection_img_show(det_arr, self.det_cap_label)

    #检测结果格式化打印函数 需要传入results类的对象 即检测结果的索引值
    def detection_format_print(self, det_result):
        #获取存放检测对象的字典
        det_dict = det_result.names
        #获取检测对象的boxes属性
        det_boxes = det_result.boxes
        #获取检测结果中的类别索引号矩阵
        det_cls = det_boxes.cls
        #将类别索引号矩阵转换为能够正常提取成员的numpy数组
        det_cls_arr = det_cls.cpu().numpy()
        #统计unique传参内矩阵的元素 有两个返回值
        #第一个返回值是矩阵内出现的不同元素有哪些
        #第二个返回值是矩阵内对应元素的出现次数
        det_cls_unique_arr, det_cls_num_arr = np.unique(det_cls_arr, return_counts=True)
        #使用for循环遍历cls矩阵 把所有的物体类别打印出来
        size = int(len(det_cls_unique_arr))
        for i in range(size):
            #通过for循环的i值作为遍历cls矩阵的索引号
            cls_index = det_cls_unique_arr[i]
            #使用每一轮得到的索引号作为键值访问字典
            cls_obj = det_dict[int(cls_index)]
            #显示对应物体的个数
            cls_num = det_cls_num_arr[i]
            print(f'{cls_obj}的数量：{cls_num}')

    #检测结果锚框坐标格式化打印函数 需要传入results类的对象
    def detection_box_format_print(self, det_result):
        #获取存放检测对象的字典
        det_dict = det_result.names
        #获取检测对象的boxes属性
        det_boxes = det_result.boxes
        #获取检测结果中的类别索引号矩阵
        det_cls = det_boxes.cls
        #将类别索引号矩阵转换为能够正常提取成员的numpy数组
        det_cls_arr = det_cls.cpu().numpy()
        #获取锚框坐标信息 xywh格式（中心点x, 中心点y, 宽度, 高度）
        det_xywh = det_boxes.xywh
        #将坐标矩阵转换为numpy数组
        det_xywh_arr = det_xywh.cpu().numpy()
        #使用for循环遍历所有检测到的物体 打印每个物体的坐标信息
        for i in range(len(det_cls_arr)):
            #获取当前物体的类别索引号
            cls_index = int(det_cls_arr[i])
            #使用索引号作为键值访问字典 获取物体名称
            cls_obj = det_dict[cls_index]
            #获取当前物体的坐标信息
            x = det_xywh_arr[i][0]
            y = det_xywh_arr[i][1]
            w = det_xywh_arr[i][2]
            h = det_xywh_arr[i][3]
            #格式化打印锚框坐标信息
            print(f'{cls_obj}: x = {x:.2f} y = {y:.2f} w = {w:.2f} h = {h:.2f}')

    #网络通信初始化函数
    def network_init(self):
        #初始化客户端套接字
        self.client_socket = None
        #服务器地址和端口
        self.server_host = 'localhost'
        self.server_port = 8888
        #尝试连接服务器
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.server_host, self.server_port))
            print(f'已连接到服务器 {self.server_host}:{self.server_port}')
        except Exception as e:
            self.client_socket = None
            print(f'连接服务器失败：{e}')
            print('检测结果将不会发送到服务器')

    #检测结果数据打包函数 需要传入results类的对象
    def detection_data_pack(self, det_result):
        #创建数据字典用于存储检测结果
        detection_data = {
            'counts': {},  # 数量统计
            'boxes': []    # 锚框坐标信息
        }
        #获取存放检测对象的字典
        det_dict = det_result.names
        #获取检测对象的boxes属性
        det_boxes = det_result.boxes
        #获取检测结果中的类别索引号矩阵
        det_cls = det_boxes.cls
        #将类别索引号矩阵转换为能够正常提取成员的numpy数组
        det_cls_arr = det_cls.cpu().numpy()
        #统计unique传参内矩阵的元素 有两个返回值
        #第一个返回值是矩阵内出现的不同元素有哪些
        #第二个返回值是矩阵内对应元素的出现次数
        det_cls_unique_arr, det_cls_num_arr = np.unique(det_cls_arr, return_counts=True)
        #使用for循环遍历cls矩阵 把所有的物体类别数量统计添加到字典中
        size = int(len(det_cls_unique_arr))
        for i in range(size):
            #通过for循环的i值作为遍历cls矩阵的索引号
            cls_index = det_cls_unique_arr[i]
            #使用每一轮得到的索引号作为键值访问字典
            cls_obj = det_dict[int(cls_index)]
            #显示对应物体的个数
            cls_num = int(det_cls_num_arr[i])
            #将数量统计添加到字典中
            detection_data['counts'][cls_obj] = cls_num
        #获取锚框坐标信息 xywh格式（中心点x, 中心点y, 宽度, 高度）
        det_xywh = det_boxes.xywh
        #将坐标矩阵转换为numpy数组
        det_xywh_arr = det_xywh.cpu().numpy()
        #使用for循环遍历所有检测到的物体 将每个物体的坐标信息添加到列表中
        for i in range(len(det_cls_arr)):
            #获取当前物体的类别索引号
            cls_index = int(det_cls_arr[i])
            #使用索引号作为键值访问字典 获取物体名称
            cls_obj = det_dict[cls_index]
            #获取当前物体的坐标信息
            x = float(det_xywh_arr[i][0])
            y = float(det_xywh_arr[i][1])
            w = float(det_xywh_arr[i][2])
            h = float(det_xywh_arr[i][3])
            #将锚框坐标信息添加到列表中
            detection_data['boxes'].append({
                'class': cls_obj,
                'x': x,
                'y': y,
                'w': w,
                'h': h
            })
        #返回打包好的数据字典
        return detection_data

    #发送检测结果到服务器函数 需要传入打包好的检测数据
    def send_detection_data(self, detection_data):
        #判断客户端套接字是否已连接
        if self.client_socket:
            try:
                #将数据字典转换为JSON字符串
                data_json = json.dumps(detection_data, ensure_ascii=False)
                #将JSON字符串编码为字节
                data_bytes = data_json.encode('utf-8')
                #先发送数据长度（4字节）
                data_len = len(data_bytes)
                self.client_socket.send(data_len.to_bytes(4, byteorder='big'))
                #再发送实际数据
                self.client_socket.send(data_bytes)
                print('检测结果已发送到服务器')
            except Exception as e:
                print(f'发送数据到服务器失败：{e}')
                #如果发送失败 尝试重新连接
                try:
                    self.client_socket.close()
                except:
                    pass
                self.client_socket = None
                #尝试重新连接
                try:
                    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.client_socket.connect((self.server_host, self.server_port))
                    print(f'已重新连接到服务器 {self.server_host}:{self.server_port}')
                except:
                    print('重新连接服务器失败')

    #视频初始化函数
    def video_init(self):
        #视频图像显示定时器初始化
        self.video_timer = QTimer()
        self.video_timer.setInterval(1)
        self.video_timer.setTimerType(Qt.PreciseTimer)
        #视频选择信号与槽
        self.pushButton_video.clicked.connect(self.video_choose)
        #视频暂停/播放按钮信号与槽
        self.pushButton_video_pause.clicked.connect(self.video_pause_play)
        #定时器信号与槽
        self.video_timer.timeout.connect(self.video_image_detect)
        #视频进度条滑动信号与槽 绑定进度条值改变信号和视频帧设置函数
        self.horizontalSlider_video.valueChanged.connect(self.video_seek)
        #初始化视频暂停状态标志
        self.video_is_paused = False
        #初始化视频总帧数
        self.video_total_frames = 0
        #初始化当前视频帧位置
        self.video_current_frame = 0

    #视频选择函数
    def video_choose(self):
        #先获取视频文件路径 显示打开文件格式为mp4
        path = QFileDialog.getOpenFileName(filter='*.mp4')
        video_path = path[0]
        #判断用户是不是真的选择了视频
        if video_path:
            #如果选到了视频，才初始化对应的视频对象
            self.video = cv2.VideoCapture(video_path)
            #获取视频总帧数
            self.video_total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
            
            self.video_fps = self.video.get(cv2.CAP_PROP_FPS)
            self.video_timer.setInterval(int(1000 / self.video_fps))
            self.det_video_label.setText("fps: {:.2f}".format(self.video_fps))
            
            #设置视频进度条的最大值为视频总帧数
            self.horizontalSlider_video.setMaximum(self.video_total_frames)
            #初始化当前帧位置为0
            self.video_current_frame = 0
            #初始化暂停状态为False
            self.video_is_paused = False
            #更新进度条显示
            self.label_video_progress.setText(f'视频进度：0 / {self.video_total_frames}')
            #确保窗口大小不会因为视频内容而自动调整
            #保存当前窗口大小，防止自动调整
            current_size = self.size()
            self.setMinimumSize(current_size)
            #开启定时器 开始播放视频并检测
            self.video_timer.start()
        else:
            print('用户未选择视频')
            QMessageBox.information(self, "消息", "用户未选择视频")

    #视频暂停/播放函数
    def video_pause_play(self):
        #判断视频是否已经打开
        if hasattr(self, 'video') and self.video.isOpened():
            #如果视频正在播放（未暂停）
            if not self.video_is_paused:
                #暂停视频 停止定时器
                self.video_timer.stop()
                #获取当前视频播放到的帧数
                self.video_current_frame = int(self.video.get(cv2.CAP_PROP_POS_FRAMES))
                #设置暂停状态为True
                self.video_is_paused = True
                print(f'视频已暂停，当前帧：{self.video_current_frame}')
            #如果视频已经暂停
            else:
                #从暂停的帧位置继续播放
                #设置视频播放位置为暂停时的帧数
                self.video.set(cv2.CAP_PROP_POS_FRAMES, self.video_current_frame)
                #重新开启定时器
                self.video_timer.start()
                #设置暂停状态为False
                self.video_is_paused = False
                print(f'视频继续播放，从第{self.video_current_frame}帧开始')

    #视频进度条拖动函数
    def video_seek(self, frame_value):
        #判断视频是否已经打开
        if hasattr(self, 'video') and self.video.isOpened():
            #如果视频正在播放 需要先暂停
            if not self.video_is_paused:
                self.video_timer.stop()
                self.video_is_paused = True
            #设置视频播放位置为滑动条的当前值
            self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_value)
            #更新当前帧位置
            self.video_current_frame = frame_value
            #更新进度条显示
            self.label_video_progress.setText(f'视频进度：{frame_value} / {self.video_total_frames}')
            #读取当前帧并显示
            ret, arr = self.video.read()
            if ret:
                #将原始视频显示到左侧
                self.detection_img_show(arr, self.orig_video_label)
                #将图像矩阵进行检测
                result = self.model(source = arr, verbose = False, conf = self.model_conf)
                #提取带检测框的图像矩阵
                det_arr = result[0].plot()
                #右侧画布显示带检测框的检测视频
                self.detection_img_show(det_arr, self.det_video_label)
                #将检测结果返回值作为参数传给格式化打印函数
                self.detection_format_print(result[0])
                #将检测结果提取 作为参数进行锚框坐标格式化打印
                self.detection_box_format_print(result[0])
                #将检测结果打包并发送到服务器
                detection_data = self.detection_data_pack(result[0])
                self.send_detection_data(detection_data)

    #视频图像检测
    def video_image_detect(self):
        #读取视频对象的视频帧
        ret, arr = self.video.read()
        #先判断视频是不是读完了
        if ret:
            #获取当前视频播放到的帧数
            self.video_current_frame = int(self.video.get(cv2.CAP_PROP_POS_FRAMES))
            #更新进度条的值（不触发valueChanged信号，避免循环调用）
            self.horizontalSlider_video.blockSignals(True)
            self.horizontalSlider_video.setValue(self.video_current_frame)
            self.horizontalSlider_video.blockSignals(False)
            #更新进度条显示
            self.label_video_progress.setText(f'视频进度：{self.video_current_frame} / {self.video_total_frames}')
            #将原始视频显示到左侧
            self.detection_img_show(arr, self.orig_video_label)
            #将图像矩阵进行检测
            result = self.model(source = arr, verbose = False, conf = self.model_conf)
            #提取带检测框的图像矩阵
            det_arr = result[0].plot()
            #右侧画布显示带检测框的检测视频
            self.detection_img_show(det_arr, self.det_video_label)
            #将检测结果返回值作为参数传给格式化打印函数
            self.detection_format_print(result[0])
            #将检测结果提取 作为参数进行锚框坐标格式化打印
            self.detection_box_format_print(result[0])
            #将检测结果打包并发送到服务器
            detection_data = self.detection_data_pack(result[0])
            self.send_detection_data(detection_data)
        #如果ret为假 代表视频播完了 需要关闭定时器 清空显示画布
        else:
            self.video_timer.stop()
            self.video_is_paused = False
            self.orig_video_label.clear()
            self.det_video_label.clear()
            #清理保存的图像数据
            if self.orig_video_label in self.image_pixmaps:
                del self.image_pixmaps[self.orig_video_label]
            if self.det_video_label in self.image_pixmaps:
                del self.image_pixmaps[self.det_video_label]
            #恢复窗口最小尺寸限制，允许手动调整
            self.setMinimumSize(0, 0)

#main函数
if __name__ == "__main__":
    #要先准备一个QApplication对象
    app = QApplication(sys.argv)
    #实例化一个ui对象
    ui = mainWindow()
    #调用show函数 显示界面
    ui.show()
    #使用事件循环机制让程序不退出
    app.exec()