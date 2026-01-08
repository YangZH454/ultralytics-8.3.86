from ultralytics import YOLO

#无论要训练一个识别什么物体的模型 模型的内部架构都是一样的
model = YOLO("yolo11n.pt")

#模型训练
model.train(
    #yaml配置文件路径
    data="mymodel.yaml",
    #训练轮数 默认100轮 此处可以减小训练轮数
    epochs=50,
    #降低数据加载的工作进程数量 避免windows系统下的多进程数据加载报错
    workers=0,
)

