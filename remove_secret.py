
import json
import os

notebook_path = "/Users/yosesotomayor/Desktop/car/src/notebooks/main.ipynb"

with open(notebook_path, "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = cell["source"]
        new_source = []
        modified = False
        for line in source:
            if "sk_live_" in line:
                # Replace the hardcoded key with environment variable lookup
                # line looks like: "client = StructOCR(\"sk_live_...\")\n"
                new_line = "client = StructOCR(os.getenv(\"STRUCT_OCR_API_KEY\"))\n"
                new_source.append(new_line)
                modified = True
            else:
                new_source.append(line)
        
        if modified:
            cell["source"] = new_source
            # Add os and load_dotenv if not present in the imports of this cell or elsewhere
            # Actually, let's just add it to the first cell for safety
            break

# Add load_dotenv to the first cell
first_cell = nb["cells"][0]
if first_cell["cell_type"] == "code":
    source = first_cell["source"]
    if "import os\n" not in source and "import os" not in "".join(source):
        source.insert(0, "import os\n")
        source.insert(0, "from dotenv import load_dotenv\n")
        source.insert(2, "load_dotenv()\n")
        first_cell["source"] = source

with open(notebook_path, "w") as f:
    json.dump(nb, f, indent=1)

print("Notebook updated: removed hardcoded secret and added load_dotenv.")
