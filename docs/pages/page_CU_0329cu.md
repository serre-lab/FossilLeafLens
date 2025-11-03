
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - CU_0329cu</title>
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
            <div class="info-value" style="font-size: 16px; color: #666;">Catalog Number: CU_0329cu</div>
        </div>

        <div class="info-card">
            <div class="info-section">
                <div class="info-label">Primary Catalog Number</div>
                <div class="info-value">UCM-18587</div>
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
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank" class="prediction-link">Betulaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank" class="prediction-link">Rosaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank" class="prediction-link">Sapindaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank" class="prediction-link">Fabaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank" class="prediction-link">Fagaceae</a>
                </div>
            </div>
        </div>

        <div class="fossil-image-section">
            <h2>Fossil Sample</h2>
            <a href="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0329cu/image.jpg" target="_blank"><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0329cu/image.jpg" alt="Fossil Image"></a>
        </div>

        <div class="similar-specimens-section">
            <h2>Similar Leaf Fossil Specimens</h2>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Betulaceae/Betulaceae_Paracarpinus_fraterna_Florissant_FLFO_010899.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Betulaceae/Betulaceae_Paracarpinus_fraterna_Florissant_FLFO_010899.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Betulaceae_Paracarpinus_fraterna_Florissant_FLFO_010899</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0776cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0776cu.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Crataegus_copeana_Florissant_CU_0776cu</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_sp_Florissant_FLFO_009135A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_sp_Florissant_FLFO_009135A.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_sp_Florissant_FLFO_009135A</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0420cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Crataegus_copeana_Florissant_CU_0420cu.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Rosaceae_Crataegus_copeana_Florissant_CU_0420cu</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_006221B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_006221B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_006221B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004010.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004010.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004010</div>
                </div>
            </div>

            <h3>Similar Extant Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Albizia_adinocephala_Wolfe_Wolfe_30165b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Albizia_adinocephala_Wolfe_Wolfe_30165b.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Albizia_adinocephala_Wolfe_Wolfe_30165b</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Juglandaceae/Juglandaceae_Carya_texana_Axelrod_Axelrod_469.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Juglandaceae/Juglandaceae_Carya_texana_Axelrod_Axelrod_469.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Juglandaceae_Carya_texana_Axelrod_Axelrod_469</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Saxifragaceae/Saxifragaceae_Tiarella_cordifolia_Hickey_Hickey_6715.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Saxifragaceae/Saxifragaceae_Tiarella_cordifolia_Hickey_Hickey_6715.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Saxifragaceae_Tiarella_cordifolia_Hickey_Hickey_6715</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Ruizodendron_ovale_Wing_Wing_111-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Ruizodendron_ovale_Wing_Wing_111-002.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Ruizodendron_ovale_Wing_Wing_111-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Oxymitra_lagunensis_Wing_Wing_304-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Oxymitra_lagunensis_Wing_Wing_304-002.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Oxymitra_lagunensis_Wing_Wing_304-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Meiogyne_hainanensis_Wing_Wing_267-003.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Meiogyne_hainanensis_Wing_Wing_267-003.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Meiogyne_hainanensis_Wing_Wing_267-003</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Berrya_cordifolia_Wing_Wing_519-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Berrya_cordifolia_Wing_Wing_519-002.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Malvaceae_Berrya_cordifolia_Wing_Wing_519-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Saxifragaceae/Saxifragaceae_Heuchera_chlorantha_Hickey_Hickey_3511.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Saxifragaceae/Saxifragaceae_Heuchera_chlorantha_Hickey_Hickey_3511.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Saxifragaceae_Heuchera_chlorantha_Hickey_Hickey_3511</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Mitrephora_thorelii_Wing_Wing_235-003.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Mitrephora_thorelii_Wing_Wing_235-003.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Mitrephora_thorelii_Wing_Wing_235-003</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Popowia_filamentosa_Wing_Wing_163-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Popowia_filamentosa_Wing_Wing_163-001.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Popowia_filamentosa_Wing_Wing_163-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_alba_Axelrod_Axelrod_23.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_alba_Axelrod_Axelrod_23.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_alba_Axelrod_Axelrod_23</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Cavendishia_axillaris_Wing_Wing_476-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Cavendishia_axillaris_Wing_Wing_476-002.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Ericaceae_Cavendishia_axillaris_Wing_Wing_476-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Hamamelidaceae/Hamamelidaceae_Fothergilla_monticola_Wing_Wing_963-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Hamamelidaceae/Hamamelidaceae_Fothergilla_monticola_Wing_Wing_963-001.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Hamamelidaceae_Fothergilla_monticola_Wing_Wing_963-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Vitaceae/Vitaceae_Vitis_lanata_Wolfe_Wolfe_8734.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Vitaceae/Vitaceae_Vitis_lanata_Wolfe_Wolfe_8734.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Vitaceae_Vitis_lanata_Wolfe_Wolfe_8734</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_alba_Axelrod_Axelrod_383.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_alba_Axelrod_Axelrod_383.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_alba_Axelrod_Axelrod_383</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Melodorum_fruticosum_Wing_Wing_284-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Melodorum_fruticosum_Wing_Wing_284-001.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Melodorum_fruticosum_Wing_Wing_284-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Sapranthus_campechianus_Wing_Wing_86-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Sapranthus_campechianus_Wing_Wing_86-002.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Sapranthus_campechianus_Wing_Wing_86-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rubiaceae/Rubiaceae_Cinchona_pubescens_Hickey_Hickey_4631.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rubiaceae/Rubiaceae_Cinchona_pubescens_Hickey_Hickey_4631.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rubiaceae_Cinchona_pubescens_Hickey_Hickey_4631</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Monanthotaxis_ferruginea_Wing_Wing_188-004.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Monanthotaxis_ferruginea_Wing_Wing_188-004.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Monanthotaxis_ferruginea_Wing_Wing_188-004</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Cananga_latifolium_Wing_Wing_129-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Cananga_latifolium_Wing_Wing_129-001.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Cananga_latifolium_Wing_Wing_129-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Betulaceae/Betulaceae_Betula_papyrifera_NMNS_T0408.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Betulaceae/Betulaceae_Betula_papyrifera_NMNS_T0408.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Betulaceae_Betula_papyrifera_NMNS_T0408</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Desmodium_aparines_Wolfe_Wolfe_30454.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Desmodium_aparines_Wolfe_Wolfe_30454.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Desmodium_aparines_Wolfe_Wolfe_30454</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Enantia_chlorantha_Wing_Wing_265-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Enantia_chlorantha_Wing_Wing_265-001.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Enantia_chlorantha_Wing_Wing_265-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Calliandra_trinervia_Wolfe_Wolfe_30272c.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Calliandra_trinervia_Wolfe_Wolfe_30272c.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Calliandra_trinervia_Wolfe_Wolfe_30272c</div>
                </div>
            </div>
        </div>

        <div>
            <h2>Concepts</h2>
            <div class="concept-container">
                <div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_1_1079.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_1_1079.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201079/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1079_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1079</em> - Rank: 1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_2_129.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_2_129.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20129/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_129_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 129</em> - Rank: 2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_3_735.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_3_735.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20735/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_735_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 735</em> - Rank: 3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_4_382.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_4_382.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20382/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_382_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 382</em> - Rank: 4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_5_48.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_5_48.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2048/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_48_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 48</em> - Rank: 5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_6_1884.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_6_1884.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201884/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1884_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1884</em> - Rank: 6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_7_1552.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_7_1552.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201552/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1552_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1552</em> - Rank: 7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_8_557.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_8_557.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20557/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_557_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 557</em> - Rank: 8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_9_533.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_9_533.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20533/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_533_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 533</em> - Rank: 9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_10_560.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0329cu/concept_10_560.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20560/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_560_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 560</em> - Rank: 10</div>
            </div>
            </div>
        </div>
    </div>
</body>
</html>
