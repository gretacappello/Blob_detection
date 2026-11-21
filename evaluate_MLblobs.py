!pip install -q ultralytics
from ultralytics import YOLO

# Path to your WISPR-I single frames
images_path = '/path/to/your/images/'

# Path to the trained model
model = YOLO('/path/to/best.pt')

# Modify parameters according to your needs :)
results = model.predict(
    source=images_path,
    imgsz=1024,
    conf=0.3,       # minimum confidence score to keep a detection. 
    iou=0.7,        # NMS IoU: overlapping boxes above this are merged into one
    save=True,      # save images with predicted boxes
    save_txt=True,  # save box coordinates as .txt files
    save_conf=True, # include the confidence score in the .txt files
    project='/path/to/output/',
    name='predictions',
    exist_ok=True
)
