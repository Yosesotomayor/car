
import json

notebook_path = '/Users/yosesotomayor/Desktop/car/src/notebooks/main.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

found = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        for i, line in enumerate(source):
            if 'servicios_basicos = text.split("Servicios Básicos")[1].' in line and '.split("\\n")[0]' in line:
                print(f"Found target line in cell id {cell.get('id', 'unknown')}: {line.strip()}")
                # Replace the line with the new logic
                # The line structure is likely: "    servicios_basicos = text.split("Servicios Básicos")[1].strip().split("\n")[0]\n"
                # We want: "    servicios_basicos = text.split("Servicios Básicos")[1].strip().split("\n")[0].rstrip(',')\n"
                
                # To be safe, let's just reconstruct the line with proper indentation
                indentation = line[:line.find('servicios_basicos')]
                new_line = indentation + 'servicios_basicos = text.split("Servicios Básicos")[1].strip().split("\\n")[0].rstrip(\',\')\n'
                
                source[i] = new_line
                found = True
                break
    if found:
        break

if found:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Notebook updated successfully.")
else:
    print("Target line not found.")
