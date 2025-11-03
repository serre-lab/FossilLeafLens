
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - FLFO_000528</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(to bottom, #f8f9fa 0%, #ffffff 100%);
            color: #1a1a1a;
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 30px 60px;
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
            padding-bottom: 30px;
            border-bottom: 1px solid #e8e8e8;
        }

        h1 {
            font-size: 32px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 15px;
            letter-spacing: -0.5px;
        }

        h2 {
            font-size: 24px;
            font-weight: 600;
            color: #1a1a1a;
            margin: 40px 0 20px;
            letter-spacing: -0.3px;
        }

        h3 {
            font-size: 20px;
            font-weight: 600;
            color: #2a2a2a;
            margin: 35px 0 15px;
        }

        a {
            color: #2563eb;
            text-decoration: none;
            transition: all 0.2s ease;
        }

        a:hover {
            color: #1d4ed8;
            text-decoration: underline;
        }

        .info-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 35px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        }

        .info-section {
            margin-bottom: 25px;
        }

        .info-section:last-child {
            margin-bottom: 0;
        }

        .info-label {
            font-size: 14px;
            font-weight: 600;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }

        .info-value {
            font-size: 18px;
            color: #1a1a1a;
            font-weight: 500;
        }

        .predictions {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }

        .prediction-link {
            display: inline-block;
            padding: 6px 14px;
            background: #f8f9fa;
            border-radius: 6px;
            font-size: 15px;
            color: #2563eb;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .prediction-link:hover {
            background: #e9ecef;
            text-decoration: none;
            transform: translateY(-1px);
        }

        .fossil-image-section {
            text-align: center;
            margin-bottom: 50px;
        }

        .fossil-image-section img {
            max-width: 100%;
            width: 300px;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .fossil-image-section img:hover {
            transform: scale(1.08);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
        }

        .similar-specimens-section {
            margin-bottom: 50px;
        }

        .similar-images-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 25px;
            margin-top: 25px;
        }

        .similar-image-container {
            text-align: center;
            position: relative;
        }

        .similar-image {
            width: 100%;
            aspect-ratio: 1;
            object-fit: cover;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }

        .similar-image:hover {
            transform: translateY(-8px) scale(1.08);
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.15);
            z-index: 10;
        }

        .image-caption {
            margin-top: 10px;
            font-size: 12px;
            color: #666;
            line-height: 1.4;
            word-wrap: break-word;
        }

        .concept-container {
            display: flex;
            flex-direction: column;
            gap: 40px;
            margin-top: 30px;
        }

        .concept-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            transition: all 0.3s ease;
        }

        .concept-card:hover {
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            transform: translateY(-2px);
        }

        .concept-images {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 25px;
            margin-bottom: 15px;
            position: relative;
        }

        .concept-images img {
            width: 400px;
            height: 400px;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }

        .concept-images img:hover {
            transform: scale(1.1);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            z-index: 10;
        }

        .concept-caption {
            text-align: center;
            font-size: 15px;
            color: #4a4a4a;
            line-height: 1.6;
        }

        .concept-caption em {
            color: #2563eb;
            font-style: italic;
            font-weight: 500;
        }

        .metadata-links {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .metadata-link {
            display: inline-block;
            padding: 8px 16px;
            background: #f8f9fa;
            border-radius: 6px;
            font-size: 14px;
            color: #4a4a4a;
            transition: all 0.2s ease;
        }

        .metadata-link:hover {
            background: #e9ecef;
            text-decoration: none;
            color: #1a1a1a;
        }

        @media (max-width: 768px) {
            .container {
                padding: 30px 20px 50px;
            }

            h1 {
                font-size: 26px;
            }

            h2 {
                font-size: 20px;
            }

            .similar-images-grid {
                grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
                gap: 15px;
            }

            .concept-images {
                flex-direction: column;
                gap: 15px;
            }

            .concept-images img {
                width: 100%;
                max-width: 400px;
                height: auto;
            }

            .metadata-links {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Fossil Leaf Identification</h1>
            <div class="info-value" style="font-size: 16px; color: #666;">Catalog Number: FLFO_000528</div>
        </div>

        <div class="info-card">
            <div class="info-section">
                <div class="info-label">Primary Catalog Number</div>
                <div class="info-value">FLFO 528</div>
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
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank" class="prediction-link">Rosaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank" class="prediction-link">Betulaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank" class="prediction-link">Ulmaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank" class="prediction-link">Salicaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank" class="prediction-link">Fabaceae</a>
                </div>
            </div>
        </div>

        <div class="fossil-image-section">
            <h2>Fossil Sample</h2>
            <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/FLFO_000528.jpg" target="_blank"><img src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/FLFO_000528.jpg" alt="Fossil Image"></a>
        </div>

        <div class="similar-specimens-section">
            <h2>Similar Leaf Fossil Specimens</h2>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Holodiscus_lisii_Florissant_FLFO_004791B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Holodiscus_lisii_Florissant_FLFO_004791B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Holodiscus_lisii_Florissant_FLFO_004791B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_nupta_Florissant_CU_0333.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_nupta_Florissant_CU_0333.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Crataegus_nupta_Florissant_CU_0333</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0647cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0647cu.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Crataegus_copeana_Florissant_CU_0647cu</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_sp_Florissant_FLFO_003242B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_sp_Florissant_FLFO_003242B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Quercus_sp_Florissant_FLFO_003242B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_CU_0701cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_CU_0701cu.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_CU_0701cu</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_002633A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_002633A.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_002633A</div>
                </div>
            </div>

            <h3>Similar Extant Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Oleaceae_Syringa_pubescens_NMNS_T1665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Oleaceae_Syringa_pubescens_NMNS_T1665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Oleaceae_Syringa_pubescens_NMNS_T1665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Oleaceae/Oleaceae_Syringa_pubescens_NMNS_T1665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Zygophyllaceae/Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Cassia_atomaria_Axelrod_Axelrod_409</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Oleaceae_Syringa_pubescens_NMNS_T1665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_integerrima_Hickey_Hickey_3665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Zygophyllaceae_Guaiacum_coulteri_Axelrod_Axelrod_437</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Pithecellobium_oblongum_Hickey_Hickey_4196.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Ericaceae_Sphyrospermum_majus_Wing_Wing_462-003</div>
                </div>
            </div>
        </div>

        <div>
            <h2>Concepts</h2>
            <div class="concept-container">
                <div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_1_1427.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_1_1427.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201427/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1427_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1427</em> - Rank: 1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_2_731.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_2_731.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20731/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_731_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 731</em> - Rank: 2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_3_1598.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_3_1598.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201598/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1598_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1598</em> - Rank: 3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_4_508.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_4_508.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20508/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_508_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 508</em> - Rank: 4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_5_462.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_5_462.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20462/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_462_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 462</em> - Rank: 5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_6_48.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_6_48.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2048/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_48_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 48</em> - Rank: 6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_7_1079.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_7_1079.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201079/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1079_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1079</em> - Rank: 7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_8_1181.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_8_1181.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201181/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1181_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1181</em> - Rank: 8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_9_560.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_9_560.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20560/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_560_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 560</em> - Rank: 9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_10_1020.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts_viridis/fossil_FLFO_000528/concept_10_1020.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201020/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1020_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1020</em> - Rank: 10</div>
            </div>
            </div>
        </div>
    </div>
</body>
</html>
