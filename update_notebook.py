
import json
import os

notebook_path = "/Users/yosesotomayor/Desktop/car/src/notebooks/main.ipynb"

with open(notebook_path, "r") as f:
    nb = json.load(f)

# The code to replace
old_code_snippet = "from surya.ocr import run_ocr"

# The new code
new_code = [
    "# same but with suryaOCR\n",
    "from surya.detection import DetectionPredictor\n",
    "from surya.recognition import RecognitionPredictor\n",
    "from surya.foundation import FoundationPredictor\n",
    "from PIL import Image\n",
    "\n",
    "langs = [\"spa\"] # Specify languages\n",
    "det_predictor = DetectionPredictor()\n",
    "rec_predictor = RecognitionPredictor(FoundationPredictor())\n",
    "\n",
    "# Ensure image_path is defined or reload it if needed (assuming it is defined in previous cells)\n",
    "# If image_path is a check_paths object, we might need to load it.\n",
    "# Based on previous cells: image_path = paths['data_path'] / 'Image.jpeg'\n",
    "if 'image_path' in locals() and not isinstance(image_path, Image.Image):\n",
    "    try:\n",
    "        image = Image.open(image_path)\n",
    "    except:\n",
    "        # Fallback if image_path is not a path or file\n",
    "        pass\n",
    "else:\n",
    "    # Attempt to load if we have the path string or object\n",
    "    # This part is tricky without running context, but let's assume image_path from cell 4 context\n",
    "    pass\n",
    "\n",
    "# The user code used [image_path], but surya 0.17.1 expects list of images or similar.\n",
    "# Check if available variables allow direct usage.\n",
    "# Let's use a safe approach assuming image_path is a Path object from pathlib\n",
    "try:\n",
    "    if 'image' not in locals():\n",
    "        image = Image.open(image_path)\n",
    "    predictions = rec_predictor([image], [langs], det_predictor=det_predictor)\n",
    "\n",
    "    for result in predictions[0].text_lines:\n",
    "        print(result.text)\n",
    "except Exception as e:\n",
    "    print(f\"Error running surya: {e}\")\n"
]

# Simplified new code that matches the user's coding style and variables more closely
# The user had:
# predictions = run_ocr([image_path], [langs], det_model, det_processor, rec_model, rec_processor)
# image_path was defined in cell 4 as: image_path = paths['data_path'] / 'Image.jpeg'

final_new_code = [
    "# same but with suryaOCR\n",
    "from surya.detection import DetectionPredictor\n",
    "from surya.recognition import RecognitionPredictor\n",
    "from surya.foundation import FoundationPredictor\n",
    "from PIL import Image\n",
    "\n",
    "langs = [\"spa\"] # Specify languages\n",
    "det_predictor = DetectionPredictor()\n",
    "rec_predictor = RecognitionPredictor(FoundationPredictor())\n",
    "\n",
    "try:\n",
    "    # image_path is a Path object from cell 4\n",
    "    pil_image = Image.open(image_path)\n",
    "    predictions = rec_predictor([pil_image], [langs], det_predictor=det_predictor)\n",
    "\n",
    "    for result in predictions[0].text_lines:\n",
    "        print(result.text)\n",
    "except NameError:\n",
    "    print(\"image_path not defined. Please run previous cells.\")\n",
    "except Exception as e:\n",
    "    print(f\"Error: {e}\")\n"
]


found = False
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if old_code_snippet in source:
            cell["source"] = final_new_code
            found = True
            break

if found:
    with open(notebook_path, "w") as f:
        json.dump(nb, f, indent=1) # using indent=1 to match similar style or just compact
    print("Notebook updated successfully.")
else:
    print("Could not find the cell to update.")
