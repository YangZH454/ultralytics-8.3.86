from ultralytics import YOLO
import multiprocessing
# model(source='./datasets/BVN.mp4')  # run inference on an image or video file(s)
# results = model.val()  # evaluate model performance on the validation set
# model(source=0,show=True)
def main():
    model = YOLO('yolo11n.pt')  # load a pretrained model (recommended for training)
    model.train(data='test0.yaml', 
                epochs=200,
                imgsz=640, 
                workers=16, 
                batch = 16,
                optimizer = 'SGD',
                lr0 = 0.01,
                lrf = 0.1,
                patience = 50,
                cos_lr = True,
                close_mosaic = 20,
                )
    print()
    model.save('test0.pt')

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Windows 必加
    main()
    

