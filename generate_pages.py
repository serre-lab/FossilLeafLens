import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

cu_df = pd.read_excel("../Florissant_CUmetadata.xlsx")
flfo_df = pd.read_excel("../Florissant_FLFOmetadata.xls")

cols_cu = ['InstPrefix+Catalog #', 'Family', 'Genus', 'Species']
cols_flfo = ['Class 2, Kingdom', 'Sci. Name, Obj/Science', 'Identified By', 'Geo Unit', 'Description']

cu_df = cu_df.groupby('Inventory Number (CU filename)')[cols_cu].agg(
    lambda x: [v for v in x if isinstance(v, str)]
).reset_index()

flfo_df = flfo_df.groupby('Catalog #')[cols_flfo].agg(
    lambda x: [v for v in x if isinstance(v, str)]
).reset_index()

flfo_df['Catalog #'] = flfo_df['Catalog #'].apply(lambda x: x.split(' ')[-1])

# Constants
NUM_IMAGES = 943
PROJECT_DIR = "./"
DOCS_DIR = os.path.join(PROJECT_DIR, "docs")
IMAGES_DIR = os.path.join(DOCS_DIR, "images")
MKDOCS_YML = os.path.join(PROJECT_DIR, "mkdocs.yml")

Unknown_IMAGE_URL = "https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/{}/image.jpg"
Unknown_CONCEPT_URL = "https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_{}/{}"

Known_IMAGE_URL = "https://storage.googleapis.com/{}.jpg"
Known_LEAF_IMAGE_URL = "https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/{}/{}"

Unidentified_IMAGE_URL = "https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/{}.jpg"
Unidentified_CONCEPT_URL = "https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_{}/{}"

FEATURE_VIS_URL = "https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_{}_fv.webp"
CONCEPT_INFO = "https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20{}/"
CLASS_INFO = "https://fel-thomas.github.io/Leaf-Lens/classes/{}/"
# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)

# Load image names from JSON
with open("image_names2.json", "r") as file:
    image_names = json.load(file)

with open("image2_predictions.json", 'r') as file:
    image_predictions = json.load(file)

with open("unidentified_image_names.json", "r") as file:
    unidentified_image_names = json.load(file)

with open("unidentified_fossil_predictions.json", "r") as file:
    unidentified_image_predictions = json.load(file)

with open("unknown_closest.json", "r") as file:
    unknown_closest = json.load(file)

with open("unidentified_closest.json", "r") as file:
    unidentified_closest = json.load(file)

with open("closest_extant_examples_checkpoint_gpu.json", "r") as file:
    closest_extant_examples = json.load(file)

with open("closest_extant_examples_gpu.json", "r") as file:
    closest_extant_examples_uni = json.load(file)

# Create a new dictionary with just the image name as key
simplified_dict = {}

for raw_key, value in closest_extant_examples.items():
    # Extract image name from the messy key
    try:
        # Step 1: Convert raw_key string to actual Python list string (if needed)
        raw_key = raw_key.replace("\n", ",")
        cleaned_key = eval(raw_key)  # Not safe for untrusted input, but okay for controlled data

        # Step 2: Extract image name from the full path
        image_path = cleaned_key[0]
        image_name = image_path.strip().split("/")[-1].split(".")[0] # Get only the filename

        simplified_dict[image_name] = value

    except Exception as e:
        print(f"Skipping malformed key: {raw_key} due to error: {e}")

simplified_dict_uni = {}

for raw_key, value in closest_extant_examples_uni.items():
    # Extract image name from the messy key
    try:
        # Step 1: Convert raw_key string to actual Python list string (if needed)
        raw_key = raw_key.replace("\n", ",")
        cleaned_key = eval(raw_key)  # Not safe for untrusted input, but okay for controlled data

        # Step 2: Extract image name from the full path
        image_path = cleaned_key[0]
        image_name = image_path.strip().split("/")[-1].split(".")[0] # Get only the filename

        simplified_dict_uni[image_name] = value

    except Exception as e:
        print(f"Skipping malformed key: {raw_key} due to error: {e}")
    


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - {image_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(to bottom, #f8f9fa 0%, #ffffff 100%);
            color: #1a1a1a;
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 30px 60px;
        }}

        .header {{
            text-align: center;
            margin-bottom: 50px;
            padding-bottom: 30px;
            border-bottom: 1px solid #e8e8e8;
        }}

        h1 {{
            font-size: 32px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 15px;
            letter-spacing: -0.5px;
        }}

        h2 {{
            font-size: 24px;
            font-weight: 600;
            color: #1a1a1a;
            margin: 40px 0 20px;
            letter-spacing: -0.3px;
        }}

        h3 {{
            font-size: 20px;
            font-weight: 600;
            color: #2a2a2a;
            margin: 35px 0 15px;
        }}

        a {{
            color: #2563eb;
            text-decoration: none;
            transition: all 0.2s ease;
        }}

        a:hover {{
            color: #1d4ed8;
            text-decoration: underline;
        }}

        .info-card {{
            background: #ffffff;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 35px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        }}

        .info-section {{
            margin-bottom: 25px;
        }}

        .info-section:last-child {{
            margin-bottom: 0;
        }}

        .info-label {{
            font-size: 14px;
            font-weight: 600;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}

        .info-value {{
            font-size: 18px;
            color: #1a1a1a;
            font-weight: 500;
        }}

        .predictions {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }}

        .prediction-link {{
            display: inline-block;
            padding: 6px 14px;
            background: #f8f9fa;
            border-radius: 6px;
            font-size: 15px;
            color: #2563eb;
            font-weight: 500;
            transition: all 0.2s ease;
        }}

        .prediction-link:hover {{
            background: #e9ecef;
            text-decoration: none;
            transform: translateY(-1px);
        }}

        .fossil-image-section {{
            text-align: center;
            margin-bottom: 50px;
        }}

        .fossil-image-section img {{
            max-width: 100%;
            width: 300px;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            cursor: pointer;
        }}

        .fossil-image-section img:hover {{
            transform: scale(1.08);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
        }}

        .similar-specimens-section {{
            margin-bottom: 50px;
        }}

        .similar-images-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 25px;
            margin-top: 25px;
        }}

        .similar-image-container {{
            text-align: center;
            position: relative;
        }}

        .similar-image {{
            width: 100%;
            aspect-ratio: 1;
            object-fit: cover;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }}

        .similar-image:hover {{
            transform: translateY(-8px) scale(1.08);
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.15);
            z-index: 10;
        }}

        .image-caption {{
            margin-top: 10px;
            font-size: 12px;
            color: #666;
            line-height: 1.4;
            word-wrap: break-word;
        }}

        .concept-container {{
            display: flex;
            flex-direction: column;
            gap: 40px;
            margin-top: 30px;
        }}

        .concept-card {{
            background: #ffffff;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            transition: all 0.3s ease;
        }}

        .concept-card:hover {{
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            transform: translateY(-2px);
        }}

        .concept-images {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 25px;
            margin-bottom: 15px;
            position: relative;
        }}

        .concept-images img {{
            width: 400px;
            height: 400px;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }}

        .concept-images img:hover {{
            transform: scale(1.1);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            z-index: 10;
        }}

        .concept-caption {{
            text-align: center;
            font-size: 15px;
            color: #4a4a4a;
            line-height: 1.6;
        }}

        .concept-caption em {{
            color: #2563eb;
            font-style: italic;
            font-weight: 500;
        }}

        .metadata-links {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .metadata-link {{
            display: inline-block;
            padding: 8px 16px;
            background: #f8f9fa;
            border-radius: 6px;
            font-size: 14px;
            color: #4a4a4a;
            transition: all 0.2s ease;
        }}

        .metadata-link:hover {{
            background: #e9ecef;
            text-decoration: none;
            color: #1a1a1a;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 30px 20px 50px;
            }}

            h1 {{
                font-size: 26px;
            }}

            h2 {{
                font-size: 20px;
            }}

            .similar-images-grid {{
                grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
                gap: 15px;
            }}

            .concept-images {{
                flex-direction: column;
                gap: 15px;
            }}

            .concept-images img {{
                width: 100%;
                max-width: 400px;
                height: auto;
            }}

            .metadata-links {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Fossil Leaf Identification</h1>
            <div class="info-value" style="font-size: 16px; color: #666;">Catalog Number: {image_name}</div>
        </div>

        <div class="info-card">
            <div class="info-section">
                <div class="info-label">Primary Catalog Number</div>
                <div class="info-value">{value1}</div>
            </div>
            
            <div class="info-section">
                <div class="info-label">Metadata Resources</div>
                <div class="metadata-links">
                    <a href="https://docs.google.com/spreadsheets/d/1IxU4YjUBWdJyolYbKlNUQetb7sDlN3sV/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true" target="_blank" class="metadata-link">Florissant CU Metadata</a>
                    <a href="https://docs.google.com/spreadsheets/d/1FIeJoNFIOy22oGVMDgrBZ94EWQ9OZqGLprjPYZRJuLY/edit?usp=sharing" target="_blank" class="metadata-link">Florissant FLFO Metadata</a>
                </div>
            </div>

            <div class="info-section">
                <div class="info-label">Top 5 Predictions</div>
                <div class="predictions">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class1}/" target="_blank" class="prediction-link">{class1}</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class2}/" target="_blank" class="prediction-link">{class2}</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class3}/" target="_blank" class="prediction-link">{class3}</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class4}/" target="_blank" class="prediction-link">{class4}</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class5}/" target="_blank" class="prediction-link">{class5}</a>
                </div>
            </div>
        </div>

        <div class="fossil-image-section">
            <h2>Fossil Sample</h2>
            <a href="{main_image}" target="_blank"><img src="{main_image}" alt="Fossil Image"></a>
        </div>

        <div class="similar-specimens-section">
            <h2>Similar Leaf Fossil Specimens</h2>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="{sm1}" target="_blank"><img class="similar-image" src="{sm1}" alt="Similar fossil specimen"></a>
                    <div class="image-caption">{sm1_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm2}" target="_blank"><img class="similar-image" src="{sm2}" alt="Similar fossil specimen"></a>
                    <div class="image-caption">{sm2_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm3}" target="_blank"><img class="similar-image" src="{sm3}" alt="Similar fossil specimen"></a>
                    <div class="image-caption">{sm3_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm4}" target="_blank"><img class="similar-image" src="{sm4}" alt="Similar fossil specimen"></a>
                    <div class="image-caption">{sm4_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm5}" target="_blank"><img class="similar-image" src="{sm5}" alt="Similar fossil specimen"></a>
                    <div class="image-caption">{sm5_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm6}" target="_blank"><img class="similar-image" src="{sm6}" alt="Similar fossil specimen"></a>
                    <div class="image-caption">{sm6_name}</div>
                </div>
            </div>

            <h3>Similar Extant Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="{sm1l}" target="_blank"><img class="similar-image" src="{sm1l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm1l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm2l}" target="_blank"><img class="similar-image" src="{sm2l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm2l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm3l}" target="_blank"><img class="similar-image" src="{sm3l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm3l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm4l}" target="_blank"><img class="similar-image" src="{sm4l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm4l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm5l}" target="_blank"><img class="similar-image" src="{sm5l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm5l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm6l}" target="_blank"><img class="similar-image" src="{sm6l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm6l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm7l}" target="_blank"><img class="similar-image" src="{sm7l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm7l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm8l}" target="_blank"><img class="similar-image" src="{sm8l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm8l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm9l}" target="_blank"><img class="similar-image" src="{sm9l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm9l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm10l}" target="_blank"><img class="similar-image" src="{sm10l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm10l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm11l}" target="_blank"><img class="similar-image" src="{sm11l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm11l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm12l}" target="_blank"><img class="similar-image" src="{sm12l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm12l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm13l}" target="_blank"><img class="similar-image" src="{sm13l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm13l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm14l}" target="_blank"><img class="similar-image" src="{sm14l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm14l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm15l}" target="_blank"><img class="similar-image" src="{sm15l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm15l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm16l}" target="_blank"><img class="similar-image" src="{sm16l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm16l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm17l}" target="_blank"><img class="similar-image" src="{sm17l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm17l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm18l}" target="_blank"><img class="similar-image" src="{sm18l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm18l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm19l}" target="_blank"><img class="similar-image" src="{sm19l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm19l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm20l}" target="_blank"><img class="similar-image" src="{sm20l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm20l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm21l}" target="_blank"><img class="similar-image" src="{sm21l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm21l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm22l}" target="_blank"><img class="similar-image" src="{sm22l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm22l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm23l}" target="_blank"><img class="similar-image" src="{sm23l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm23l_name}</div>
                </div>
                <div class="similar-image-container">
                    <a href="{sm24l}" target="_blank"><img class="similar-image" src="{sm24l}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{sm24l_name}</div>
                </div>
            </div>
        </div>

        <div>
            <h2>Concepts</h2>
            <div class="concept-container">
                {concept_images}
            </div>
        </div>
    </div>
</body>
</html>
"""


# Generate Markdown pages with inline HTML
all_images = [image_names, unidentified_image_names]
Unknown_PAGES_DIR = os.path.join(DOCS_DIR, "pages/")
Unidentified_PAGES_DIR = os.path.join(DOCS_DIR, "pages/")
os.makedirs(Unknown_PAGES_DIR, exist_ok = True)
os.makedirs(Unidentified_PAGES_DIR, exist_ok = True)

for i, (key, value) in enumerate(image_names.items()):
    print(key, key.split("_"))
    x = key.split("_")
    root = x[0]
    try: 
        index = int(x[1])
    except:
        digit = ""
        n = len(x[1])
        for i in range(n):
            if 48 <= ord(x[1][i]) < 58:
                digit += x[1][i]
            else:
                break
        index = int(digit)

    info1 = info2 = info3 = info4 = "Not Found"
    value1 = value2 = value3 = value4 = ' '

    if root == "CU":
        row_values = cu_df[cu_df['Inventory Number (CU filename)'] == index]
        if len(row_values) > 0: 
            row_dict = row_values.to_dict(orient='records')[0]
            info1, value1 = 'InstPrefix+Catalog #', ", ".join(row_dict['InstPrefix+Catalog #'])
            # info2, value2 = 'Family', ", ".join(row_dict['Family'])
            # info3, value3 = 'Genus', ", ".join(row_dict['Genus'])
            # info4, value4 = 'Species', ", ".join(row_dict['Species'])
    else:
        row_values = flfo_df[flfo_df['Catalog #'] == str(index)]
        if len(row_values) > 0: 
            row_dict = row_values.to_dict(orient='records')[0]
            info1, value1 = "Catalog #", "FLFO " + row_dict['Catalog #']
            # info1, value1 = 'Class 2, Kingdom', ", ".join(row_dict['Class 2, Kingdom'])
            # info2, value2 = 'Sci. Name, Obj/Science', ", ".join(row_dict['Sci. Name, Obj/Science'])
            # info3, value3 = 'Geo Unit', ", ".join(row_dict['Geo Unit'])
            # info4, value4 = 'Description', ", ".join(row_dict['Description'])

    
    class1, class2, class3, class4, class5 = image_predictions[key]
    value.sort(key = lambda x : int(x.split("_")[1]))
    concept_images = "\n".join(
        [f'''<div class="concept-card">
                <div class="concept-images">
                    <a href="{Unknown_CONCEPT_URL.format(key, value[j])}" target="_blank">
                        <img src="{Unknown_CONCEPT_URL.format(key, value[j])}" alt="Concept Image {j+1}">
                    </a>
                    <a href="{CONCEPT_INFO.format(value[j].split("_")[-1][:-4])}" target="_blank">
                        <img src="{FEATURE_VIS_URL.format(value[j].split("_")[-1][:-4])}" alt="Feature Visualization {j+1}">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: {value[j].split("_")[-1][:-4]}</em> - Rank: {value[j].split("_")[-2]}</div>
            </div>''' for j in range(len(value))]
    )

    known_image_urls = [(file_path.split("/")[-1], Known_IMAGE_URL.format(file_path)) for file_path in unknown_closest[key]["closest_filenames"]]
    leaf_image_urls = [(fs['filename'].split(".")[0], Known_LEAF_IMAGE_URL.format(fs['filename'].split("_")[0], fs['filename'])) for fs in simplified_dict[key]]

    html_content = html_template.format(
        image_name=f"{key}",
        class1 = class1,
        class2 = class2,
        class3 = class3,
        class4 = class4,
        class5 = class5,
        info1  = 'Primary catalog number', 
        value1 = value1,
        # info2  = info2,
        # value2 = value2,
        # info3  = info3,
        # value3 = value3,
        # info4  = info4,
        # value4 = value4,
        main_image = Unknown_IMAGE_URL.format(key),
        
        sm1 = known_image_urls[0][1],
        sm2 = known_image_urls[1][1],
        sm3 = known_image_urls[2][1],
        sm4 = known_image_urls[3][1],
        sm5 = known_image_urls[4][1],    
        sm6 = known_image_urls[5][1],
    
        sm1_name = known_image_urls[0][0],
        sm2_name = known_image_urls[1][0],
        sm3_name = known_image_urls[2][0],
        sm4_name = known_image_urls[3][0],
        sm5_name = known_image_urls[4][0],
        sm6_name = known_image_urls[5][0],
        
        sm1l = leaf_image_urls[0][1],
        sm2l = leaf_image_urls[1][1],
        sm3l = leaf_image_urls[2][1],
        sm4l = leaf_image_urls[3][1],
        sm5l = leaf_image_urls[4][1],    
        sm6l = leaf_image_urls[5][1],
        sm7l = leaf_image_urls[6][1],
        sm8l = leaf_image_urls[7][1],
        sm9l = leaf_image_urls[8][1],
        sm10l = leaf_image_urls[9][1],
        sm11l = leaf_image_urls[10][1],  
        sm12l = leaf_image_urls[11][1],
        sm13l = leaf_image_urls[12][1],
        sm14l = leaf_image_urls[13][1],
        sm15l = leaf_image_urls[14][1],
        sm16l = leaf_image_urls[15][1],
        sm17l = leaf_image_urls[16][1],
        sm18l = leaf_image_urls[17][1],
        sm19l = leaf_image_urls[18][1],
        sm20l = leaf_image_urls[19][1],
        sm21l = leaf_image_urls[20][1],
        sm22l = leaf_image_urls[21][1],
        sm23l = leaf_image_urls[22][1],
        sm24l = leaf_image_urls[23][1],
  
        sm1l_name = leaf_image_urls[0][0],
        sm2l_name = leaf_image_urls[1][0],
        sm3l_name = leaf_image_urls[2][0],
        sm4l_name = leaf_image_urls[3][0],
        sm5l_name = leaf_image_urls[4][0],
        sm6l_name = leaf_image_urls[5][0],
        sm7l_name = leaf_image_urls[6][0],
        sm8l_name = leaf_image_urls[7][0],
        sm9l_name = leaf_image_urls[8][0],
        sm10l_name = leaf_image_urls[9][0],
        sm11l_name = leaf_image_urls[10][0],
        sm12l_name = leaf_image_urls[11][0],
        sm13l_name = leaf_image_urls[12][0],
        sm14l_name = leaf_image_urls[13][0],
        sm15l_name = leaf_image_urls[14][0],
        sm16l_name = leaf_image_urls[15][0],
        sm17l_name = leaf_image_urls[16][0],
        sm18l_name = leaf_image_urls[17][0],
        sm19l_name = leaf_image_urls[18][0],
        sm20l_name = leaf_image_urls[19][0],
        sm21l_name = leaf_image_urls[20][0],
        sm22l_name = leaf_image_urls[21][0],
        sm23l_name = leaf_image_urls[22][0],
        sm24l_name = leaf_image_urls[23][0],


        concept_images = concept_images
    )
    page_path = os.path.join(Unknown_PAGES_DIR, f"page_{key}.md")
    print(page_path)
    with open(page_path, "w") as f:
        f.write(html_content)

for i, (key, value) in enumerate(unidentified_image_names.items()):
    print(key, key.split("_"))
    x = key.split("_")
    root = x[0]
    try: 
        index = int(x[1])
    except:
        digit = ""
        n = len(x[1])
        for i in range(n):
            if 48 <= ord(x[1][i]) < 58:
                digit += x[1][i]
            else:
                break
        index = int(digit)



    class1, class2, class3, class4, class5 =unidentified_image_predictions[key]
    value.sort(key = lambda x : int(x.split("_")[1]))

    info1 = info2 = info3 = info4 = "Not Found"
    value1 = value2 = value3 = value4 = ' '

    if root == "CU":
        row_values = cu_df[cu_df['Inventory Number (CU filename)'] == index]
        if len(row_values) > 0: 
            row_dict = row_values.to_dict(orient='records')[0]
            info1, value1 = 'InstPrefix+Catalog #', ", ".join(row_dict['InstPrefix+Catalog #'])
            # info2, value2 = 'Family', ", ".join(row_dict['Family'])
            # info3, value3 = 'Genus', ", ".join(row_dict['Genus'])
            # info4, value4 = 'Species', ", ".join(row_dict['Species'])
    else:
        row_values = flfo_df[flfo_df['Catalog #'] == str(index)]
        if len(row_values) > 0: 

            row_dict = row_values.to_dict(orient='records')[0]
            # info1, value1 = 'Class 2, Kingdom', ", ".join(row_dict['Class 2, Kingdom'])
            info1, value1 = "Catalog #", "FLFO " + row_dict['Catalog #']
            # info2, value2 = 'Sci. Name, Obj/Science', ", ".join(row_dict['Sci. Name, Obj/Science'])
            # info3, value3 = 'Geo Unit', ", ".join(row_dict['Geo Unit'])
            # info4, value4 = 'Description', ", ".join(row_dict['Description'])

    concept_images = "\n".join(
        [f'''<div class="concept-card">
                <div class="concept-images">
                    <a href="{Unidentified_CONCEPT_URL.format(key, value[j])}" target="_blank">
                        <img src="{Unidentified_CONCEPT_URL.format(key, value[j])}" alt="Concept Image {j+1}">
                    </a>
                    <a href="{CONCEPT_INFO.format(value[j].split("_")[-1][:-4])}" target="_blank">
                        <img src="{FEATURE_VIS_URL.format(value[j].split("_")[-1][:-4])}" alt="Feature Visualization {j+1}">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: {value[j].split("_")[-1][:-4]}</em> - Rank: {value[j].split("_")[-2]}</div>
            </div>''' for j in range(len(value))]
    )

    known_image_urls = [(file_path.split("/")[-1], Known_IMAGE_URL.format(file_path)) for file_path in unidentified_closest[key]["closest_filenames"]]
    try:
        leaf_image_urls = [(fs['filename'].split(".")[0], Known_LEAF_IMAGE_URL.format(fs['filename'].split("_")[0], fs['filename'])) for fs in simplified_dict[key]]
    except:
        leaf_image_urls = [(fs.split(".")[0], Known_LEAF_IMAGE_URL.format(fs.split("_")[0], fs)) for fs in simplified_dict_uni[key]]
        for i in range(7, 25):
            leaf_image_urls.append(("", None))


    html_content = html_template.format(
        image_name=f"{key}",
        class1 = class1,
        class2 = class2,
        class3 = class3,
        class4 = class4,
        class5 = class5,
        info1  = 'Primary catalog number', 
        value1 = value1,
        # info2  = info2,
        # value2 = value2,
        # info3  = info3,
        # value3 = value3,
        # info4  = info4,
        # value4 = value4,
        main_image = Unidentified_IMAGE_URL.format(key),
        sm1 = known_image_urls[0][1],
        sm2 = known_image_urls[1][1],
        sm3 = known_image_urls[2][1],
        sm4 = known_image_urls[3][1],
        sm5 = known_image_urls[4][1], 
        sm6 = known_image_urls[5][1],
        sm1_name = known_image_urls[0][0],
        sm2_name = known_image_urls[1][0],
        sm3_name = known_image_urls[2][0],
        sm4_name = known_image_urls[3][0],
        sm5_name = known_image_urls[4][0],
        sm6_name = known_image_urls[5][0],

        sm1l = leaf_image_urls[0][1],
        sm2l = leaf_image_urls[1][1],
        sm3l = leaf_image_urls[2][1],
        sm4l = leaf_image_urls[3][1],
        sm5l = leaf_image_urls[4][1], 
        sm6l = leaf_image_urls[5][1],
        sm7l = leaf_image_urls[0][1],
        sm8l = leaf_image_urls[1][1],
        sm9l = leaf_image_urls[2][1],
        sm10l = leaf_image_urls[3][1],
        sm11l = leaf_image_urls[4][1],
        sm12l = leaf_image_urls[5][1],
        sm13l = leaf_image_urls[0][1],
        sm14l = leaf_image_urls[1][1],
        sm15l = leaf_image_urls[2][1],
        sm16l = leaf_image_urls[3][1],
        sm17l = leaf_image_urls[4][1],
        sm18l = leaf_image_urls[1][1],
        sm19l = leaf_image_urls[2][1],
        sm20l = leaf_image_urls[3][1],
        sm21l = leaf_image_urls[4][1],
        sm22l = leaf_image_urls[5][1],
        sm23l = leaf_image_urls[0][1],
        sm24l = leaf_image_urls[1][1],
        
     
        sm1l_name = leaf_image_urls[0][0],
        sm2l_name = leaf_image_urls[1][0],
        sm3l_name = leaf_image_urls[2][0],
        sm4l_name = leaf_image_urls[3][0],
        sm5l_name = leaf_image_urls[4][0],
        sm6l_name = leaf_image_urls[5][0],
        sm7l_name = leaf_image_urls[0][0],
        sm8l_name = leaf_image_urls[1][0],
        sm9l_name = leaf_image_urls[2][0],
        sm10l_name = leaf_image_urls[3][0],
        sm11l_name = leaf_image_urls[4][0],
        sm12l_name = leaf_image_urls[5][0],
        sm13l_name = leaf_image_urls[0][0],
        sm14l_name = leaf_image_urls[1][0],
        sm15l_name = leaf_image_urls[2][0],
        sm16l_name = leaf_image_urls[3][0],
        sm17l_name = leaf_image_urls[4][0],
        sm18l_name = leaf_image_urls[5][0],
        sm19l_name = leaf_image_urls[0][0],
        sm20l_name = leaf_image_urls[1][0],
        sm21l_name = leaf_image_urls[2][0],
        sm22l_name = leaf_image_urls[3][0],
        sm23l_name = leaf_image_urls[4][0],
        sm24l_name = leaf_image_urls[5][0],

        concept_images = concept_images
    )
    page_path = os.path.join(Unidentified_PAGES_DIR, f"page_{key}.md")
    print(page_path)
    with open(page_path, "w") as f:
        f.write(html_content)

# Generate MkDocs configuration
with open(MKDOCS_YML, "w") as f:
    f.write("site_name: Fossil Leaf Lens\n")
    f.write("theme:\n")
    f.write("  name: material\n")
    f.write("  logo: images/logo.png\n")
    f.write("  favicon: images/logo.png\n")
    f.write("  palette:\n")
    f.write("    primary: black\n")
    f.write("    accent: white\n")
    f.write("nav:\n")
    f.write("  - <b>Home</b>: index.md\n")
    # f.write("  - <b>Unknown Fossils</b>:\n")
    # f.write("    - '<b><i>Feedback Table</i></b> 📋': unknown_table.md\n")
    # for i, (key, value) in enumerate(image_predictions.items(), start = 1):
    #     f.write(f"    - {i}. {key}: pages/unknown/page_{key}.md\n")
    f.write("  - '<b>Feedback Table</b> 📋': unidentified_table.md\n")
    f.write("  - <b>Predicted fossil identifications</b>:\n")
    for i, (key, value) in enumerate(image_predictions.items(), start = 1):
        f.write(f"    - {i}. {key}: pages/page_{key}.md\n")
    total_unknown_images = len(image_predictions)
    for i, (key, value) in enumerate(unidentified_image_predictions.items(), start = 1):
        f.write(f"    - {i + total_unknown_images}. {key}: pages/page_{key}.md\n")

# # Create index page
# index_path = os.path.join(DOCS_DIR, "index.md")
# with open(index_path, "w") as f:
#     f.write("# Unidentified Fossil Predictions!\n\n")
#     f.write("Navigate through the sidebar to view all images.\n")
