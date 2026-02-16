import os
import json
import pandas as pd

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


na_fossils_dict = set()
def aggregate_data(data):
    for specimen in data:
        specimen_name = specimen["Fossil Name"]
        user_selection = specimen["User Selection"]
        if user_selection == "Not Applicable":
            na_fossils_dict.add(specimen_name)

files_names = os.listdir("NA_fossils")
for file_name in files_names:
    with open(os.path.join("NA_fossils", file_name), "r") as file:
        data = json.load(file)
        aggregate_data(data)

# Create a new dictionary with just the image name as key
def simplify_dict(raw_dict):
    """Extract image name from messy keys and create simplified dictionary."""
    simplified = {}
    for raw_key, value in raw_dict.items():
        try:
            raw_key = raw_key.replace("\n", ",")
            cleaned_key = eval(raw_key)  # Not safe for untrusted input, but okay for controlled data
            image_path = cleaned_key[0]
            image_name = image_path.strip().split("/")[-1].split(".")[0]
            simplified[image_name] = value
        except Exception as e:
            print(f"Skipping malformed key: {raw_key} due to error: {e}")
    return simplified

simplified_dict = simplify_dict(closest_extant_examples)
simplified_dict_uni = simplify_dict(closest_extant_examples_uni)
    


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
            <h1>Predicted Fossil Identifications</h1>
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
                {similar_known_html}
            </div>

            <h2>Similar Extant Leaf Specimens</h2>
            <div class="similar-images-grid">
                {similar_extant_html}
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
PAGES_DIR = os.path.join(DOCS_DIR, "pages/")
os.makedirs(PAGES_DIR, exist_ok=True)

def extract_index(key):
    """Extract numeric index from key like 'CU_123' or 'FLFO_456'."""
    x = key.split("_")
    try:
        return int(x[1])
    except:
        digit = ""
        for char in x[1]:
            if '0' <= char <= '9':
                digit += char
            else:
                break
        return int(digit) if digit else None

def get_metadata(key, root, index, cu_df, flfo_df):
    """Get metadata for a given key."""
    if root == "CU":
        row_values = cu_df[cu_df['Inventory Number (CU filename)'] == index]
        if len(row_values) > 0:
            row_dict = row_values.to_dict(orient='records')[0]
            return 'InstPrefix+Catalog #', ", ".join(row_dict['InstPrefix+Catalog #'])
    else:
        row_values = flfo_df[flfo_df['Catalog #'] == str(index)]
        if len(row_values) > 0:
            row_dict = row_values.to_dict(orient='records')[0]
            return "Catalog #", "FLFO " + row_dict['Catalog #']
    return 'Primary catalog number', ' '

def generate_concept_images(key, value, concept_url_template):
    """Generate HTML for concept images."""
    value.sort(key=lambda x: int(x.split("_")[1]))
    return "\n".join([
        f'''<div class="concept-card">
                <div class="concept-images">
                    <a href="{concept_url_template.format(key, value[j])}" target="_blank">
                        <img src="{concept_url_template.format(key, value[j])}" alt="Concept Image {j+1}">
                    </a>
                    <a href="{CONCEPT_INFO.format(value[j].split("_")[-1][:-4])}" target="_blank">
                        <img src="{FEATURE_VIS_URL.format(value[j].split("_")[-1][:-4])}" alt="Feature Visualization {j+1}">
                    </a>
                </div>
                <div class="concept-caption"><a href="{CONCEPT_INFO.format(value[j].split("_")[-1][:-4])}" target="_blank"><em>Concept: {value[j].split("_")[-1][:-4]}</em></a> - Rank: {value[j].split("_")[-2]}</div>
            </div>''' for j in range(len(value))
    ])

def generate_similar_known_html(closest_data, max_images=6):
    """Generate HTML for similar known fossil specimens."""
    known_image_urls = [
        (file_path.split("/")[-1], Known_IMAGE_URL.format(file_path))
        for file_path in closest_data["closest_filenames"]
        if 'cupressaceae' not in file_path.lower() and 'dryopteridaceae' not in file_path.lower()
    ]
    if known_image_urls:
        return "\n".join([
            f'''<div class="similar-image-container">
                    <a href="{url}" target="_blank"><img class="similar-image" src="{url}" alt="Similar fossil specimen"></a>
                    <div class="image-caption">{name}</div>
                </div>'''
            for name, url in known_image_urls[:max_images]
        ])
    else:
        return '<div class="image-caption" style="grid-column: 1 / -1; text-align: center; color: #666;">No similar images found.</div>'

def generate_similar_extant_html(leaf_image_urls, max_images=15):
    """Generate HTML for similar extant leaf specimens."""
    # Filter out None URLs and empty names
    leaf_image_urls = [(name, url) for name, url in leaf_image_urls if url is not None and name]
    if leaf_image_urls:
        return "\n".join([
            f'''<div class="similar-image-container">
                    <a href="{url}" target="_blank"><img class="similar-image" src="{url}" alt="Similar extant leaf"></a>
                    <div class="image-caption">{name}</div>
                </div>'''
            for name, url in leaf_image_urls[:max_images]
        ])
    else:
        return '<div class="image-caption" style="grid-column: 1 / -1; text-align: center; color: #666;">No similar extant leaf images found.</div>'

def generate_page(key, value, predictions, closest_data, concept_url_template, image_url_template, 
                  simplified_dict, simplified_dict_uni, cu_df, flfo_df, pages_dir):
    """Generate a single page for a fossil specimen."""
    if key in na_fossils_dict:
        return
    
    x = key.split("_")
    root = x[0]
    index = extract_index(key)
    if index is None:
        return
    
    info1, value1 = get_metadata(key, root, index, cu_df, flfo_df)
    class1, class2, class3, class4, class5 = predictions[key]
    
    concept_images = generate_concept_images(key, value, concept_url_template)
    similar_known_html = generate_similar_known_html(closest_data)
    
    # Get extant leaf images
    try:
        leaf_image_urls = [
            (fs['filename'].split(".")[0], Known_LEAF_IMAGE_URL.format(fs['filename'].split("_")[0], fs['filename']))
            for fs in simplified_dict[key]
            if 'cupressaceae' not in fs['filename'].lower() and 'dryopteridaceae' not in fs['filename'].lower()
        ]
    except:
        leaf_image_urls = [
            (fs.split(".")[0], Known_LEAF_IMAGE_URL.format(fs.split("_")[0], fs))
            for fs in simplified_dict_uni[key]
            if 'cupressaceae' not in fs.lower() and 'dryopteridaceae' not in fs.lower()
        ]
    
    similar_extant_html = generate_similar_extant_html(leaf_image_urls)
    
    html_content = html_template.format(
        image_name=f"{key}",
        class1=class1,
        class2=class2,
        class3=class3,
        class4=class4,
        class5=class5,
        info1='Primary catalog number',
        value1=value1,
        main_image=image_url_template.format(key),
        similar_known_html=similar_known_html,
        similar_extant_html=similar_extant_html,
        concept_images=concept_images
    )
    
    page_path = os.path.join(pages_dir, f"page_{key}.md")
    print(page_path)
    with open(page_path, "w") as f:
        f.write(html_content)

# Generate pages for unknown images
for key, value in image_names.items():
    print(key, key.split("_"))
    generate_page(
        key, value, image_predictions, unknown_closest[key],
        Unknown_CONCEPT_URL, Unknown_IMAGE_URL,
        simplified_dict, simplified_dict_uni,
        cu_df, flfo_df, PAGES_DIR
    )

# Generate pages for unidentified images
for key, value in unidentified_image_names.items():
    print(key, key.split("_"))
    generate_page(
        key, value, unidentified_image_predictions, unidentified_closest[key],
        Unidentified_CONCEPT_URL, Unidentified_IMAGE_URL,
        simplified_dict, simplified_dict_uni,
        cu_df, flfo_df, PAGES_DIR
    )

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
    f.write("  - <b>Predicted Fossil Identifications</b>:\n")
    index = 1
    for key in image_predictions.keys():
        if key in na_fossils_dict:
            continue
        f.write(f"    - {index}. {key}: pages/page_{key}.md\n")
        index += 1
    for key in unidentified_image_predictions.keys():
        if key in na_fossils_dict:
            continue
        f.write(f"    - {index}. {key}: pages/page_{key}.md\n")
        index += 1
