!pip install ultralytics
from ultralytics import YOLO

#here we should modify with a test set, a dataset never seen before.
images_path = '/content/drive/MyDrive/AI_project/test3/dataset/images/test_e2/'

model = YOLO('/content/drive/MyDrive/AI_project/test3/dataset/runs/yolo8_14Jan_v1/train/weights/best.pt')
results = model.predict(
    source=images_path,
    save=True,  # save images with predictions
    project='/content/drive/MyDrive/AI_project/test3/dataset/runs/yolo8_14Jan_v1',  # base folder
    name='predictions',  # subfolder inside the project folder
    exist_ok=True  # overwrite if folder exists
