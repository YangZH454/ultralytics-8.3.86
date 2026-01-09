# -*- coding: utf-8 -*-
import socket
import json
import threading
from datetime import datetime
import sys

class DetectionServer:
    def __init__(self, argv):
        #服务器地址和端口
        self.host = argv[1] if len(argv) > 1 else 'localhost'
        self.port = int(argv[2]) if len(argv) > 2 else 8888
        #创建服务器套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #设置套接字选项 允许地址重用
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #绑定地址和端口
        self.server_socket.bind((self.host, self.port))
        #开始监听 最大连接数为5
        self.server_socket.listen(5)
        #存储检测结果历史记录
        self.detection_history = []
        print(f'服务器已启动，监听地址：{self.host}:{self.port}')

    #处理客户端连接的函数
    def handle_client(self, client_socket, client_address):
        print(f'客户端已连接：{client_address}')
        try:
            while True:
                #先接收4字节的数据长度
                data_len_bytes = client_socket.recv(4)
                #如果接收到的数据为空 说明客户端断开连接
                if not data_len_bytes:
                    break
                #将4字节转换为整数 获取数据长度
                data_len = int.from_bytes(data_len_bytes, byteorder='big')
                #接收实际数据
                data_bytes = b''
                while len(data_bytes) < data_len:
                    chunk = client_socket.recv(data_len - len(data_bytes))
                    if not chunk:
                        break
                    data_bytes += chunk
                #如果接收到的数据长度正确
                if len(data_bytes) == data_len:
                    #将字节数据解码为JSON字符串
                    data_json = data_bytes.decode('utf-8')
                    #将JSON字符串解析为字典
                    detection_data = json.loads(data_json)
                    #处理接收到的检测数据
                    self.process_detection_data(detection_data, client_address)
        except Exception as e:
            print(f'处理客户端 {client_address} 时发生错误：{e}')
        finally:
            #关闭客户端套接字
            client_socket.close()
            print(f'客户端 {client_address} 已断开连接')

    #处理检测数据的函数
    def process_detection_data(self, detection_data, client_address):
        #获取当前时间戳
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #创建检测记录
        detection_record = {
            'timestamp': timestamp,
            'client': client_address,
            'counts': detection_data.get('counts', {}),
            'boxes': detection_data.get('boxes', [])
        }
        #将检测记录添加到历史记录中
        self.detection_history.append(detection_record)
        #打印检测结果
        print(f'\n========== 检测结果 [{timestamp}] ==========')
        print(f'客户端：{client_address}')
        #打印数量统计
        print('--- 数量统计 ---')
        counts = detection_data.get('counts', {})
        if counts:
            for obj_name, count in counts.items():
                print(f'{obj_name}的数量：{count}')
        else:
            print('未检测到物体')
        #打印锚框坐标信息
        print('--- 锚框坐标信息 ---')
        boxes = detection_data.get('boxes', [])
        if boxes:
            for box in boxes:
                obj_name = box.get('class', 'unknown')
                x = box.get('x', 0)
                y = box.get('y', 0)
                w = box.get('w', 0)
                h = box.get('h', 0)
                print(f'{obj_name}: x = {x:.2f} y = {y:.2f} w = {w:.2f} h = {h:.2f}')
        else:
            print('未检测到锚框')
        print('=' * 50)
        #如果历史记录超过100条 删除最早的记录
        if len(self.detection_history) > 100:
            self.detection_history.pop(0)

    #启动服务器函数
    def start(self):
        print('等待客户端连接...')
        try:
            while True:
                #接受客户端连接
                client_socket, client_address = self.server_socket.accept()
                #为每个客户端创建新线程处理
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address)
                )
                #设置线程为守护线程
                client_thread.daemon = True
                #启动线程
                client_thread.start()
        except KeyboardInterrupt:
            print('\n服务器正在关闭...')
        finally:
            #关闭服务器套接字
            self.server_socket.close()
            print('服务器已关闭')

#main函数
if __name__ == "__main__":
    #创建服务器实例
    server = DetectionServer(sys.argv)
    #启动服务器
    server.start()

