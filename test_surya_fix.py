
from surya.detection import DetectionPredictor
from surya.recognition import RecognitionPredictor
from surya.foundation import FoundationPredictor
from PIL import Image
import os

# usage paths
data_path = "data"
image_path = os.path.join(data_path, "Image.jpeg")

if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
    # try to find any image in data
    files = os.listdir(data_path)
    images = [f for f in files if f.endswith(('.jpeg', '.jpg', '.png'))]
    if images:
        image_path = os.path.join(data_path, images[0])
        print(f"Using {image_path} instead.")
    else:
        print("No images found.")
        exit(1)

try:
    image = Image.open(image_path)
    
    det_predictor = DetectionPredictor()
    rec_predictor = RecognitionPredictor(FoundationPredictor())
    
    # default task name is likely ocr with boxes or similar.
    # checking schema will confirm.
    # For now trying without task_names or with default if simple call works.
    
    predictions = rec_predictor([image], det_predictor=det_predictor)
    
    for result in predictions[0].text_lines:
        print(result.text)

except Exception as e:
    print(f"Error: {e}")
