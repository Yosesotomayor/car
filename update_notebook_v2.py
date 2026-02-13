
import json
import os

notebook_path = "/Users/yosesotomayor/Desktop/car/src/notebooks/main.ipynb"

with open(notebook_path, "r") as f:
    nb = json.load(f)

# The code to replace (this is the code I inserted in previous step, checking for it)
old_code_snippet_1 = "from surya.foundation import FoundationPredictor"

# New code for 0.13.1
new_code = [
    "# same but with suryaOCR (0.13.1 compatible)\n",
    "from surya.detection import DetectionPredictor\n",
    "from surya.recognition import RecognitionPredictor\n",
    "from PIL import Image\n",
    "\n",
    "langs = [\"spa\"] # Specify languages\n",
    "det_predictor = DetectionPredictor()\n",
    "rec_predictor = RecognitionPredictor()\n",
    "\n",
    "try:\n",
    "    if 'image_path' in locals():\n",
    "        pil_image = Image.open(image_path)\n",
    "    elif 'paths' in locals():\n",
    "        pil_image = Image.open(paths['data_path'] / 'Image.jpeg')\n",
    "    else:\n",
    "        # Fallback for safe execution if run out of order\n",
    "        from pathlib import Path\n",
    "        pil_image = Image.open(Path('data/Image.jpeg').absolute())\n",
    "\n",
    "    # 0.13.1 API: rec_predictor(images, image_langs, det_predictor=...)\n",
    "    # image_langs is list of list of languages\n",
    "    predictions = rec_predictor([pil_image], [langs], det_predictor=det_predictor)\n",
    "\n",
    "    for result in predictions[0].text_lines:\n",
    "        print(result.text)\n",
    "except Exception as e:\n",
    "    print(f\"Error: {e}\")\n"
]

found = False
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        # Check if it's the cell we modified previously OR the original cell if I am wrong about state
        # I remember I modified it to include FoundationPredictor.
        if "RecognitionPredictor" in source: 
             # Use a robust check: find the cell that imports surya
             if "from surya" in source:
                 cell["source"] = new_code
                 found = True
                 break

if found:
    with open(notebook_path, "w") as f:
        json.dump(nb, f, indent=1)
    print("Notebook updated successfully for 0.13.1.")
else:
    print("Could not find the cell to update.")
