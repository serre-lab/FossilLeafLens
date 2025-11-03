
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - CU_0459cu</title>
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
            <div class="info-value" style="font-size: 16px; color: #666;">Catalog Number: CU_0459cu</div>
        </div>

        <div class="info-card">
            <div class="info-section">
                <div class="info-label">Primary Catalog Number</div>
                <div class="info-value">UCMP-3668</div>
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
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank" class="prediction-link">Fagaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank" class="prediction-link">Ulmaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank" class="prediction-link">Rosaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank" class="prediction-link">Sapindaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank" class="prediction-link">Meliaceae</a>
                </div>
            </div>
        </div>

        <div class="fossil-image-section">
            <h2>Fossil Sample</h2>
            <a href="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0459cu/image.jpg" target="_blank"><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0459cu/image.jpg" alt="Fossil Image"></a>
        </div>

        <div class="similar-specimens-section">
            <h2>Similar Leaf Fossil Specimens</h2>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_CU_0680.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_CU_0680.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_CU_0680</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003078B_[1].jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003078B_[1].jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003078B_[1]</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003553.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003553.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003553</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004569.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004569.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004569</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004222B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004222B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_004222B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003356.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003356.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_003356</div>
                </div>
            </div>

            <h3>Similar Extant Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Erythrina_lanata_Wolfe_Wolfe_16463b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Erythrina_lanata_Wolfe_Wolfe_16463b.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Erythrina_lanata_Wolfe_Wolfe_16463b</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_mongolica_NMNS_U1096.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_mongolica_NMNS_U1096.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_mongolica_NMNS_U1096</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lauraceae/Lauraceae_Litsea_umbellata_NMNS_U0769.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lauraceae/Lauraceae_Litsea_umbellata_NMNS_U0769.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Lauraceae_Litsea_umbellata_NMNS_U0769</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_canariensis_NMNS_U1074.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_canariensis_NMNS_U1074.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_canariensis_NMNS_U1074</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_rubra_NMNS_T0117.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_rubra_NMNS_T0117.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_rubra_NMNS_T0117</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lamiaceae/Lamiaceae_Holmskioldia_sanguinea_NMNS_T2293.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lamiaceae/Lamiaceae_Holmskioldia_sanguinea_NMNS_T2293.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Lamiaceae_Holmskioldia_sanguinea_NMNS_T2293</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Stadmannia_oppositifolia_Wing_Wing_694-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Stadmannia_oppositifolia_Wing_Wing_694-001.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Sapindaceae_Stadmannia_oppositifolia_Wing_Wing_694-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Betulaceae/Betulaceae_Corylus_maxima_Wolfe_Wolfe_12188.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Betulaceae/Betulaceae_Corylus_maxima_Wolfe_Wolfe_12188.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Betulaceae_Corylus_maxima_Wolfe_Wolfe_12188</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apocynaceae/Apocynaceae_Kopsia_singapurensis_NMNS_T0675.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apocynaceae/Apocynaceae_Kopsia_singapurensis_NMNS_T0675.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Apocynaceae_Kopsia_singapurensis_NMNS_T0675</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Meliaceae/Meliaceae_Aglaia_mariannensis_Hickey_Hickey_2318.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Meliaceae/Meliaceae_Aglaia_mariannensis_Hickey_Hickey_2318.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Meliaceae_Aglaia_mariannensis_Hickey_Hickey_2318</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Salicaceae/Salicaceae_Poliothyrsis_sinensis_Wolfe_Wolfe_1105a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Salicaceae/Salicaceae_Poliothyrsis_sinensis_Wolfe_Wolfe_1105a.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Salicaceae_Poliothyrsis_sinensis_Wolfe_Wolfe_1105a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_mongolica_NMNS_U1072.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_mongolica_NMNS_U1072.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_mongolica_NMNS_U1072</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_acuta_NMNS_U1022.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_acuta_NMNS_U1022.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_acuta_NMNS_U1022</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Urticaceae/Urticaceae_Myrianthus_arboreus_Wolfe_Wolfe_14372.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Urticaceae/Urticaceae_Myrianthus_arboreus_Wolfe_Wolfe_14372.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Urticaceae_Myrianthus_arboreus_Wolfe_Wolfe_14372</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_radiata_NMNS_T2745.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_radiata_NMNS_T2745.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_radiata_NMNS_T2745</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_virginiana_NMNS_T0668.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_virginiana_NMNS_T0668.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_virginiana_NMNS_T0668</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Juglandaceae/Juglandaceae_Carya_alba_NMNS_U0310.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Juglandaceae/Juglandaceae_Carya_alba_NMNS_U0310.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Juglandaceae_Carya_alba_NMNS_U0310</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Betulaceae/Betulaceae_Corylus_ferox_NMNS_T2306.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Betulaceae/Betulaceae_Corylus_ferox_NMNS_T2306.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Betulaceae_Corylus_ferox_NMNS_T2306</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Thibaudia_macrocalyx_Wing_Wing_485-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Thibaudia_macrocalyx_Wing_Wing_485-002.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Ericaceae_Thibaudia_macrocalyx_Wing_Wing_485-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Ellipeiopsis_cherrevensis_Wolfe_Wolfe_15486.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Ellipeiopsis_cherrevensis_Wolfe_Wolfe_15486.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Annonaceae_Ellipeiopsis_cherrevensis_Wolfe_Wolfe_15486</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Polygalaceae/Polygalaceae_Badiera_oblongata_Wolfe_Wolfe_9568.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Polygalaceae/Polygalaceae_Badiera_oblongata_Wolfe_Wolfe_9568.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Polygalaceae_Badiera_oblongata_Wolfe_Wolfe_9568</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lamiaceae/Lamiaceae_Tectona_grandis_NMNS_T1587.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lamiaceae/Lamiaceae_Tectona_grandis_NMNS_T1587.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Lamiaceae_Tectona_grandis_NMNS_T1587</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Castanopsis_diversifolia_Hickey_Hickey_626a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Castanopsis_diversifolia_Hickey_Hickey_626a.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Castanopsis_diversifolia_Hickey_Hickey_626a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_fulva_NMNS_T2736.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_fulva_NMNS_T2736.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_fulva_NMNS_T2736</div>
                </div>
            </div>
        </div>

        <div>
            <h2>Concepts</h2>
            <div class="concept-container">
                <div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_1_227.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_1_227.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20227/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_227_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 227</em> - Rank: 1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_2_560.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_2_560.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20560/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_560_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 560</em> - Rank: 2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_3_614.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_3_614.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20614/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_614_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 614</em> - Rank: 3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_4_563.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_4_563.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20563/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_563_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 563</em> - Rank: 4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_5_1520.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_5_1520.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201520/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1520_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1520</em> - Rank: 5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_6_1202.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_6_1202.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201202/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1202_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1202</em> - Rank: 6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_7_1596.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_7_1596.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201596/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1596_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1596</em> - Rank: 7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_8_792.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_8_792.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20792/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_792_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 792</em> - Rank: 8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_9_1079.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_9_1079.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201079/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1079_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1079</em> - Rank: 9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_10_969.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0459cu/concept_10_969.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20969/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_969_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 969</em> - Rank: 10</div>
            </div>
            </div>
        </div>
    </div>
</body>
</html>
