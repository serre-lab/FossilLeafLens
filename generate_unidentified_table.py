import json

IMAGE_URL = "https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/{}.jpg"
UNKNOWN_IMAGE_URL = "https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/{}/image.jpg"

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - Feedback Table</title>
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

        .page-header {{
            text-align: center;
            padding: 40px 20px 30px;
            margin-bottom: 20px;
            border-bottom: 1px solid #e8e8e8;
        }}

        .page-header h1 {{
            font-size: 36px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
        }}

        .page-header p {{
            font-size: 16px;
            color: #666;
            margin-top: 10px;
        }}

        .container {{
            max-width: 1600px;
            margin: 0 auto;
            padding: 20px;
        }}

        .table-wrapper {{
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            overflow: hidden;
        }}

        .table-container {{
            width: 100%;
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        thead th {{
            position: sticky;
            top: 0;
            background: linear-gradient(to bottom, #2563eb 0%, #1d4ed8 100%);
            color: white;
            padding: 14px 10px;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            text-align: center;
            z-index: 10;
        }}

        tbody tr {{
            border-bottom: 1px solid #e8e8e8;
        }}

        tbody tr:hover {{
            background-color: #f8f9fa;
        }}

        td {{
            padding: 12px 10px;
            text-align: center;
            font-size: 13px;
            color: #4a4a4a;
            vertical-align: middle;
        }}

        .serial-number {{
            font-weight: 600;
            color: #666;
            text-align: center;
        }}

        .fossil-name {{
            min-width: 150px;
        }}

        .fossil-name a {{
            color: #2563eb;
            text-decoration: none;
            font-weight: 500;
        }}

        .fossil-name a:hover {{
            color: #1d4ed8;
            text-decoration: underline;
        }}

        .fossil-image {{
            padding: 8px;
        }}

        .fossil-image img {{
            max-width: 150px;
            max-height: 120px;
            width: auto;
            height: auto;
            object-fit: contain;
            border-radius: 4px;
        }}

        .predictions {{
            max-width: 200px;
            text-align: left;
            font-size: 12px;
            line-height: 1.4;
        }}

        .predictions a {{
            display: inline;
            color: #2563eb;
            text-decoration: none;
        }}

        .predictions a:hover {{
            color: #1d4ed8;
        }}

        .radio-group {{
            display: flex;
            flex-direction: column;
            gap: 4px;
            align-items: flex-start;
        }}

        .radio-group label {{
            cursor: pointer;
            font-size: 11px;
            color: #4a4a4a;
            display: flex;
            align-items: center;
            gap: 4px;
            padding: 2px 4px;
            transition: color 0.2s ease;
        }}

        .radio-group label:hover {{
            color: #1a1a1a;
        }}

        /* Simplified color-coded labels - minimal styling for performance */
        .radio-group label:has(input[value="Plausible"]) {{
            color: #065f46;
        }}

        .radio-group label:has(input[value="Impossible"]) {{
            color: #991b1b;
        }}

        .radio-group label:has(input[value="Not Sure"]) {{
            color: #92400e;
        }}

        .radio-group label:has(input[value="Not Applicable"]) {{
            color: #666;
        }}

        /* Selected state styling */
        .radio-group label:has(input:checked) {{
            font-weight: 600;
        }}

        /* Simplified row completion indicator */
        tbody tr:has(input:checked) {{
            border-left: 3px solid #22c55e !important;
        }}

        .radio-group input[type="radio"] {{
            cursor: pointer;
            margin-right: 4px;
            accent-color: #2563eb;
        }}

        /* Legend/legend styling */
        .feedback-legend {{
            display: none;
        }}

        .fixed-button {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(to bottom, #2563eb 0%, #1d4ed8 100%);
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
            transition: all 0.3s ease;
            z-index: 1000;
        }}

        .fixed-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
        }}

        .md-sidebar.md-sidebar--secondary {{
            width: 0px !important;
        }}

        /* Responsive adjustments */
        @media (max-width: 1200px) {{
            td {{
                font-size: 12px;
                padding: 10px 8px;
            }}

            .fossil-image img {{
                max-width: 120px;
                max-height: 100px;
            }}
        }}

        @media (max-width: 768px) {{
            .page-header {{
                padding: 30px 15px 20px;
            }}

            .page-header h1 {{
                font-size: 28px;
            }}

            thead th {{
                font-size: 11px;
                padding: 12px 8px;
            }}

            td {{
                font-size: 11px;
                padding: 10px 6px;
            }}

            .fossil-image img {{
                max-width: 100px;
                max-height: 80px;
            }}

            .fixed-button {{
                bottom: 20px;
                right: 20px;
                padding: 12px 20px;
                font-size: 13px;
            }}
        }}

        @media (max-width: 480px) {{
            thead th {{
                font-size: 10px;
                padding: 10px 6px;
            }}

            td {{
                font-size: 10px;
                padding: 8px 4px;
            }}

            .fossil-image img {{
                max-width: 70px;
                max-height: 60px;
            }}
        }}
    </style>
</head>
<body>
<div class="page-header">
    <h1>Fossil Leaf Lens Feedback</h1>
    <p>Please provide feedback on the predicted fossil identifications</p>
</div>

<div class="container">
    <div class="table-wrapper">
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th style="width: 5%;">No.</th>
                        <th style="width: 15%;">Fossil Name</th>
                        <th style="width: 10%;">Image</th>
                        <th style="width: 35%;">Top 5 Predictions</th>
                        <th style="width: 35%;">Feedback</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
    </div>
</div>

<button class="fixed-button" onclick="downloadJSON()">📥 Download Responses</button>

<script>
    function downloadJSON() {{
        let rows = document.querySelectorAll("tbody tr");
        let data = [];

        rows.forEach((row, index) => {{
            let cells = row.querySelectorAll("td");
            let fossilName = cells[1].innerText;
            let selected = null;
            let radios = row.querySelectorAll('input[type="radio"]');
            radios.forEach(radio => {{ if (radio.checked) {{ selected = radio.value; }} }});

            data.push({{
                "Serial Number": index + 1,
                "Fossil Name": fossilName,
                "User Selection": selected
            }});
        }});

        let blob = new Blob([JSON.stringify(data, null, 2)], {{ type: "application/json" }});
        let a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "unidentified_fossil_responses.json";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }}
</script>
</body>
</html>
"""


with open("image2_predictions.json", 'r') as file:
    unknown_image_predictions = json.load(file)


with open("unidentified_fossil_predictions.json", 'r') as file:
    image_predictions = json.load(file)



# Generate table rows dynamically
table_rows = ""

for index, (key, value) in enumerate(unknown_image_predictions.items(), start=1):
    predictions_html = ", ".join([f'<a href="https://fel-thomas.github.io/Leaf-Lens/classes/{p}/" target="_blank">{p}</a>' for p in value])
    row = f"""
        <tr>
            <td class="serial-number">{index}</td>
            <td class="fossil-name"><a href="https://serre-lab.github.io/FossilLeafLens/pages/page_{key}/" target="_blank">{key}</a></td>
            <td class="fossil-image"><img src="{UNKNOWN_IMAGE_URL.format(key)}" alt="Fossil Image"></td>
            <td><div class="predictions">{predictions_html}</div></td>
            <td>
                <div class="radio-group">
                    <label><input type="radio" name="row{index}" value="Plausible"> Plausible</label>
                    <label><input type="radio" name="row{index}" value="Impossible"> Impossible</label>
                    <label><input type="radio" name="row{index}" value="Not Sure"> Not Sure</label>
                    <label><input type="radio" name="row{index}" value="Not Applicable"> Not Applicable</label>
                </div>
            </td>
        </tr>
        """

    table_rows += row
total_unknown_images = len(unknown_image_predictions)
for index, (key, value) in enumerate(image_predictions.items(), start=1):
    index = total_unknown_images + index
    predictions_html = ", ".join([f'<a href="https://fel-thomas.github.io/Leaf-Lens/classes/{p}/" target="_blank">{p}</a>' for p in value])
    row = f"""
    <tr>
        <td class="serial-number">{index}</td>
        <td class="fossil-name"><a href="https://serre-lab.github.io/FossilLeafLens/pages/page_{key}/" target="_blank">{key}</a></td>
        <td class="fossil-image"><img src="{IMAGE_URL.format(key)}" alt="Fossil Image"></td>
        <td><div class="predictions">{predictions_html}</div></td>
        <td>
            <div class="radio-group">
                <label><input type="radio" name="row{index}" value="Plausible"> Plausible</label>
                <label><input type="radio" name="row{index}" value="Impossible"> Impossible</label>
                <label><input type="radio" name="row{index}" value="Not Sure"> Not Sure</label>
                <label><input type="radio" name="row{index}" value="Not Applicable"> Not Applicable</label>
            </div>
        </td>
    </tr>
    """
    table_rows += row

# Create the final HTML file
html_content = html_template.format(table_rows=table_rows)

# Save to an HTML file
with open("./docs/unidentified_table.md", "w") as f:
    f.write(html_content)

print("HTML file generated: unidentified_table.md")