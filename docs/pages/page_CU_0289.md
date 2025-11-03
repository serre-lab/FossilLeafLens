
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - CU_0289</title>
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
            <div class="info-value" style="font-size: 16px; color: #666;">Catalog Number: CU_0289</div>
        </div>

        <div class="info-card">
            <div class="info-section">
                <div class="info-label">Primary Catalog Number</div>
                <div class="info-value">UCM-18555</div>
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
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ochnaceae/" target="_blank" class="prediction-link">Ochnaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank" class="prediction-link">Viburnaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Marantaceae/" target="_blank" class="prediction-link">Marantaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank" class="prediction-link">Rosaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Chloranthaceae/" target="_blank" class="prediction-link">Chloranthaceae</a>
                </div>
            </div>
        </div>

        <div class="fossil-image-section">
            <h2>Fossil Sample</h2>
            <a href="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0289/image.jpg" target="_blank"><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0289/image.jpg" alt="Fossil Image"></a>
        </div>

        <div class="similar-specimens-section">
            <h2>Similar Leaf Fossil Specimens</h2>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002860.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002860.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002860</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002491B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002491B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002491B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_CU_0338cu1.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_CU_0338cu1.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Viburnaceae_Sambucus_newtoni_Florissant_CU_0338cu1</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_CU_0883cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_CU_0883cu.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Viburnaceae_Sambucus_newtoni_Florissant_CU_0883cu</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Salicaceae/Salicaceae_Populus_crassa_Florissant_FLFO_003476B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Salicaceae/Salicaceae_Populus_crassa_Florissant_FLFO_003476B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Salicaceae_Populus_crassa_Florissant_FLFO_003476B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002492A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Viburnaceae/Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002492A.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Viburnaceae_Sambucus_newtoni_Florissant_FLFO_002492A</div>
                </div>
            </div>

            <h3>Similar Extant Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Photinia_glabra_NMNS_T0052.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Photinia_glabra_NMNS_T0052.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Photinia_glabra_NMNS_T0052</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Bonnetiaceae/Bonnetiaceae_Bonnetia_stricta_Wolfe_Wolfe_9306.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Bonnetiaceae/Bonnetiaceae_Bonnetia_stricta_Wolfe_Wolfe_9306.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Bonnetiaceae_Bonnetia_stricta_Wolfe_Wolfe_9306</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Clusiaceae/Clusiaceae_Clusia_palmicida_Wolfe_Wolfe_11002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Clusiaceae/Clusiaceae_Clusia_palmicida_Wolfe_Wolfe_11002.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Clusiaceae_Clusia_palmicida_Wolfe_Wolfe_11002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lythraceae/Lythraceae_Sonneratia_alba_Wolfe_Wolfe_2856.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lythraceae/Lythraceae_Sonneratia_alba_Wolfe_Wolfe_2856.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Lythraceae_Sonneratia_alba_Wolfe_Wolfe_2856</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Potentilla_villosa_Hickey_Hickey_3900.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Potentilla_villosa_Hickey_Hickey_3900.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Potentilla_villosa_Hickey_Hickey_3900</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Bonnetiaceae/Bonnetiaceae_Ploiarium_alternifolium_Wolfe_Wolfe_3269a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Bonnetiaceae/Bonnetiaceae_Ploiarium_alternifolium_Wolfe_Wolfe_3269a.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Bonnetiaceae_Ploiarium_alternifolium_Wolfe_Wolfe_3269a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Chloranthaceae/Chloranthaceae_Hedyosmum_montanum_Hickey_Hickey_6348_1.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Chloranthaceae/Chloranthaceae_Hedyosmum_montanum_Hickey_Hickey_6348_1.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Chloranthaceae_Hedyosmum_montanum_Hickey_Hickey_6348_1</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Papaveraceae/Papaveraceae_Fumaria_judaica_Hickey_Hickey_6702.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Papaveraceae/Papaveraceae_Fumaria_judaica_Hickey_Hickey_6702.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Papaveraceae_Fumaria_judaica_Hickey_Hickey_6702</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Proteaceae/Proteaceae_Grevillea_ilicifolia_Wolfe_Wolfe_12529.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Proteaceae/Proteaceae_Grevillea_ilicifolia_Wolfe_Wolfe_12529.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Proteaceae_Grevillea_ilicifolia_Wolfe_Wolfe_12529</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Marantaceae/Marantaceae_Calathea_sp_Hickey_Hickey_3131.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Marantaceae/Marantaceae_Calathea_sp_Hickey_Hickey_3131.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Marantaceae_Calathea_sp_Hickey_Hickey_3131</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Bonnetiaceae/Bonnetiaceae_Bonnetia_neblinae_Wolfe_Wolfe_9304.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Bonnetiaceae/Bonnetiaceae_Bonnetia_neblinae_Wolfe_Wolfe_9304.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Bonnetiaceae_Bonnetia_neblinae_Wolfe_Wolfe_9304</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apocynaceae/Apocynaceae_Vallesia_dichotoma_Hickey_Hickey_1405.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apocynaceae/Apocynaceae_Vallesia_dichotoma_Hickey_Hickey_1405.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Apocynaceae_Vallesia_dichotoma_Hickey_Hickey_1405</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Onagraceae/Onagraceae_Hauya_heydeana_Wolfe_Wolfe_760.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Onagraceae/Onagraceae_Hauya_heydeana_Wolfe_Wolfe_760.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Onagraceae_Hauya_heydeana_Wolfe_Wolfe_760</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Salicaceae/Salicaceae_Salix_babylonica_NMNS_T2336.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Salicaceae/Salicaceae_Salix_babylonica_NMNS_T2336.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Salicaceae_Salix_babylonica_NMNS_T2336</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rubiaceae/Rubiaceae_Ceratopyxis_verbenacea_Wolfe_Wolfe_5702.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rubiaceae/Rubiaceae_Ceratopyxis_verbenacea_Wolfe_Wolfe_5702.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rubiaceae_Ceratopyxis_verbenacea_Wolfe_Wolfe_5702</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apiaceae/Apiaceae_Apiopetalum_velutinum_Wolfe_Wolfe_15561a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Apiaceae/Apiaceae_Apiopetalum_velutinum_Wolfe_Wolfe_15561a.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Apiaceae_Apiopetalum_velutinum_Wolfe_Wolfe_15561a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Thymelaeaceae/Thymelaeaceae_Daphnopsis_bonplandiana_Wolfe_Wolfe_3408.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Thymelaeaceae/Thymelaeaceae_Daphnopsis_bonplandiana_Wolfe_Wolfe_3408.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Thymelaeaceae_Daphnopsis_bonplandiana_Wolfe_Wolfe_3408</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Proteaceae/Proteaceae_Beauprea_balansae_Wolfe_Wolfe_6584b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Proteaceae/Proteaceae_Beauprea_balansae_Wolfe_Wolfe_6584b.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Proteaceae_Beauprea_balansae_Wolfe_Wolfe_6584b</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Marantaceae/Marantaceae_Maranta_affruiziana_Hickey_Hickey_6326_2.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Marantaceae/Marantaceae_Maranta_affruiziana_Hickey_Hickey_6326_2.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Marantaceae_Maranta_affruiziana_Hickey_Hickey_6326_2</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Malus_sylvestris_Hickey_Hickey_3737.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Malus_sylvestris_Hickey_Hickey_3737.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Malus_sylvestris_Hickey_Hickey_3737</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Machaerium_riparium_Wolfe_Wolfe_30643a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Machaerium_riparium_Wolfe_Wolfe_30643a.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fabaceae_Machaerium_riparium_Wolfe_Wolfe_30643a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Nephelium_connatum_Wolfe_Wolfe_12805.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Nephelium_connatum_Wolfe_Wolfe_12805.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Sapindaceae_Nephelium_connatum_Wolfe_Wolfe_12805</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Nitrariaceae/Nitrariaceae_Peganum_harmala_Hickey_Hickey_1682.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Nitrariaceae/Nitrariaceae_Peganum_harmala_Hickey_Hickey_1682.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Nitrariaceae_Peganum_harmala_Hickey_Hickey_1682</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cercocarpus_montanus_Wolfe_Wolfe_1486a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rosaceae/Rosaceae_Cercocarpus_montanus_Wolfe_Wolfe_1486a.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_montanus_Wolfe_Wolfe_1486a</div>
                </div>
            </div>
        </div>

        <div>
            <h2>Concepts</h2>
            <div class="concept-container">
                <div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_1_231.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_1_231.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20231/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_231_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 231</em> - Rank: 1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_2_1606.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_2_1606.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201606/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1606_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1606</em> - Rank: 2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_3_81.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_3_81.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2081/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_81_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 81</em> - Rank: 3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_4_489.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_4_489.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20489/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_489_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 489</em> - Rank: 4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_5_1123.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_5_1123.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201123/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1123_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1123</em> - Rank: 5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_6_1832.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_6_1832.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201832/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1832_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1832</em> - Rank: 6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_7_1427.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_7_1427.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201427/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1427_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1427</em> - Rank: 7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_8_1563.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_8_1563.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201563/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1563_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1563</em> - Rank: 8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_9_1884.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_9_1884.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201884/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1884_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1884</em> - Rank: 9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_10_563.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0289/concept_10_563.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20563/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_563_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 563</em> - Rank: 10</div>
            </div>
            </div>
        </div>
    </div>
</body>
</html>
