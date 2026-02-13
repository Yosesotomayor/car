
from surya.detection import DetectionPredictor
from surya.recognition import RecognitionPredictor
from PIL import Image
import os

images = [f for f in os.listdir("data") if f.endswith(".jpeg") or f.endswith(".jpg")]
if not images:
    print("No images found in data/")
    exit(0)

image_path = os.path.join("data", images[0])
pil_image = Image.open(image_path)
langs = ["spa"]

det_predictor = DetectionPredictor()
rec_predictor = RecognitionPredictor()

try:
    predictions = rec_predictor([pil_image], [langs], det_predictor=det_predictor)
    for result in predictions[0].text_lines:
        print(result.text)
    print("Success!")
except Exception as e:
    print(f"Failed: {e}")
