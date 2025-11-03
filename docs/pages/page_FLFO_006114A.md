
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - FLFO_006114A</title>
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
            <div class="info-value" style="font-size: 16px; color: #666;">Catalog Number: FLFO_006114A</div>
        </div>

        <div class="info-card">
            <div class="info-section">
                <div class="info-label">Primary Catalog Number</div>
                <div class="info-value">FLFO 6114</div>
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
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank" class="prediction-link">Vitaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank" class="prediction-link">Malvaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank" class="prediction-link">Sapindaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank" class="prediction-link">Hamamelidaceae</a>
                </div>
            </div>
        </div>

        <div class="fossil-image-section">
            <h2>Fossil Sample</h2>
            <a href="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006114A/image.jpg" target="_blank"><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006114A/image.jpg" alt="Fossil Image"></a>
        </div>

        <div class="similar-specimens-section">
            <h2>Similar Leaf Fossil Specimens</h2>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_sp_Florissant_FLFO_006827B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_sp_Florissant_FLFO_006827B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Crataegus_sp_Florissant_FLFO_006827B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_010074A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_010074A.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_010074A</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0645cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0645cu.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Crataegus_copeana_Florissant_CU_0645cu</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Amelanchier_scudderi_Florissant_CU_0309.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Amelanchier_scudderi_Florissant_CU_0309.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Amelanchier_scudderi_Florissant_CU_0309</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_001798A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_001798A.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_001798A</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_006664A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_006664A.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Rosa_sp_Florissant_FLFO_006664A</div>
                </div>
            </div>

            <h3>Similar Extant Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Rosa_carolina_Hickey_Hickey_3910.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Rosa_carolina_Hickey_Hickey_3910.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Rosa_carolina_Hickey_Hickey_3910</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Castanopsis_philippensis_Hickey_Hickey_632a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Castanopsis_philippensis_Hickey_Hickey_632a.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Castanopsis_philippensis_Hickey_Hickey_632a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Hibiscus_laevis_Wolfe_Wolfe_796.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Hibiscus_laevis_Wolfe_Wolfe_796.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Malvaceae_Hibiscus_laevis_Wolfe_Wolfe_796</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Altingiaceae/Altingiaceae_Liquidambar_acalycina_Wing_Wing_993-003.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Altingiaceae/Altingiaceae_Liquidambar_acalycina_Wing_Wing_993-003.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Altingiaceae_Liquidambar_acalycina_Wing_Wing_993-003</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apiaceae/Apiaceae_Bowlesia_palmata_Hickey_Hickey_2803.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apiaceae/Apiaceae_Bowlesia_palmata_Hickey_Hickey_2803.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Apiaceae_Bowlesia_palmata_Hickey_Hickey_2803</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Menispermaceae/Menispermaceae_Tinospora_crispa_Wolfe_Wolfe_1149b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Menispermaceae/Menispermaceae_Tinospora_crispa_Wolfe_Wolfe_1149b.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Menispermaceae_Tinospora_crispa_Wolfe_Wolfe_1149b</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_alba_Hickey_Hickey_6910_4.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_alba_Hickey_Hickey_6910_4.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_alba_Hickey_Hickey_6910_4</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_lyrata_Axelrod_Axelrod_34.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_lyrata_Axelrod_Axelrod_34.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_lyrata_Axelrod_Axelrod_34</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_humilis_Hickey_Hickey_3676.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_humilis_Hickey_Hickey_3676.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Cotoneaster_humilis_Hickey_Hickey_3676</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Pyrus_dimorphophylla_Hickey_Hickey_3700.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Pyrus_dimorphophylla_Hickey_Hickey_3700.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Pyrus_dimorphophylla_Hickey_Hickey_3700</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_racemiflora_Hickey_Hickey_3683.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cotoneaster_racemiflora_Hickey_Hickey_3683.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Cotoneaster_racemiflora_Hickey_Hickey_3683</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Castanopsis_jucunda_Hickey_Hickey_142.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Castanopsis_jucunda_Hickey_Hickey_142.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Castanopsis_jucunda_Hickey_Hickey_142</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Malus_yunnanensis_Hickey_Hickey_3731.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Malus_yunnanensis_Hickey_Hickey_3731.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Malus_yunnanensis_Hickey_Hickey_3731</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cercis_racemosa_Wolfe_Wolfe_15784b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cercis_racemosa_Wolfe_Wolfe_15784b.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Cercis_racemosa_Wolfe_Wolfe_15784b</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_lyrata_Hickey_Hickey_6301.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_lyrata_Hickey_Hickey_6301.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_lyrata_Hickey_Hickey_6301</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Vitaceae/Vitaceae_Vitis_coignetiae_Axelrod_Axelrod_643.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Vitaceae/Vitaceae_Vitis_coignetiae_Axelrod_Axelrod_643.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Vitaceae_Vitis_coignetiae_Axelrod_Axelrod_643</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Parrotia_persica_NMNS_U1188.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Parrotia_persica_NMNS_U1188.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Parrotia_persica_NMNS_U1188</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rutaceae/Rutaceae_Zanthoxylum_harmsianum_Hickey_Hickey_5846.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rutaceae/Rutaceae_Zanthoxylum_harmsianum_Hickey_Hickey_5846.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rutaceae_Zanthoxylum_harmsianum_Hickey_Hickey_5846</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_margarita_Hickey_Hickey_1253_1.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_margarita_Hickey_Hickey_1253_1.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_margarita_Hickey_Hickey_1253_1</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Hamamelidaceae/Hamamelidaceae_Hamamelis_japonica_Wing_Wing_974-006.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Hamamelidaceae/Hamamelidaceae_Hamamelis_japonica_Wing_Wing_974-006.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Hamamelidaceae_Hamamelis_japonica_Wing_Wing_974-006</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Rubus_cordifolia_Hickey_Hickey_3848.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Rubus_cordifolia_Hickey_Hickey_3848.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Rubus_cordifolia_Hickey_Hickey_3848</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Rollinia_intermedia_Wolfe_Wolfe_9526.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Rollinia_intermedia_Wolfe_Wolfe_9526.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Rollinia_intermedia_Wolfe_Wolfe_9526</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapotaceae/Sapotaceae_Lucuma_glycyphloea_Hickey_Hickey_4924.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapotaceae/Sapotaceae_Lucuma_glycyphloea_Hickey_Hickey_4924.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Sapotaceae_Lucuma_glycyphloea_Hickey_Hickey_4924</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Menispermaceae/Menispermaceae_Disciphania_calocarpa_Wolfe_Wolfe_5571.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Menispermaceae/Menispermaceae_Disciphania_calocarpa_Wolfe_Wolfe_5571.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Menispermaceae_Disciphania_calocarpa_Wolfe_Wolfe_5571</div>
                </div>
            </div>
        </div>

        <div>
            <h2>Concepts</h2>
            <div class="concept-container">
                <div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_1_1520.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_1_1520.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201520/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1520_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1520</em> - Rank: 1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_2_226.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_2_226.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20226/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_226_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 226</em> - Rank: 2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_3_938.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_3_938.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20938/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_938_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 938</em> - Rank: 3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_4_1272.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_4_1272.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201272/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1272_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1272</em> - Rank: 4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_5_690.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_5_690.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20690/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_690_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 690</em> - Rank: 5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_6_1202.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_6_1202.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201202/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1202_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1202</em> - Rank: 6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_7_1703.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_7_1703.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201703/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1703_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1703</em> - Rank: 7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_8_1766.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_8_1766.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201766/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1766_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1766</em> - Rank: 8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_9_765.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_9_765.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20765/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_765_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 765</em> - Rank: 9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_10_1544.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_FLFO_006114A/concept_10_1544.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201544/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1544_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1544</em> - Rank: 10</div>
            </div>
            </div>
        </div>
    </div>
</body>
</html>
