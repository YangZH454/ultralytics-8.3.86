#导入YOLO模块
from ultralytics import YOLO

#初始化用于图像检测的模型 括号内写模型文件的路径
model = YOLO("runs/detect/train/weights/best.pt")

#把检测源作为参数传参给model
model(source="datasets/BVN.mp4", save=True, show=True)