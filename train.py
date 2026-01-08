from ultralytics import YOLO
import multiprocessing
# model(source='./datasets/BVN.mp4')  # run inference on an image or video file(s)
# results = model.val()  # evaluate model performance on the validation set
# model(source=0,show=True)
def main():
    model = YOLO('yolo11n.pt')  # load a pretrained model (recommended for training)
    model.train(data='emotion.yml', 
                epochs=80,
                imgsz=512, 
                workers=12, 
                batch = 32,
                optimizer = 'SGD',
                lr0 = 0.02,
                patience = 50,
                close_mosaic = 0,
                mixup = 0.0,
                mosaic = 0.5,
                amp = True
                )
    print()
    model.save('emotion.pt')

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Windows 必加
    main()
    

