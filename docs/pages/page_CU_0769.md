
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - CU_0769</title>
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
            <div class="info-value" style="font-size: 16px; color: #666;">Catalog Number: CU_0769</div>
        </div>

        <div class="info-card">
            <div class="info-section">
                <div class="info-label">Primary Catalog Number</div>
                <div class="info-value">USNM-387580</div>
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
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank" class="prediction-link">Sapindaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank" class="prediction-link">Rosaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank" class="prediction-link">Oleaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank" class="prediction-link">Ulmaceae</a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank" class="prediction-link">Polygonaceae</a>
                </div>
            </div>
        </div>

        <div class="fossil-image-section">
            <h2>Fossil Sample</h2>
            <a href="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0769/image.jpg" target="_blank"><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0769/image.jpg" alt="Fossil Image"></a>
        </div>

        <div class="similar-specimens-section">
            <h2>Similar Leaf Fossil Specimens</h2>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_terminalis_Florissant_FLFO_006928.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_terminalis_Florissant_FLFO_006928.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Sapindaceae_Cardiospermum_terminalis_Florissant_FLFO_006928</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_terminalis_Florissant_CU_0849.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_terminalis_Florissant_CU_0849.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Sapindaceae_Cardiospermum_terminalis_Florissant_CU_0849</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Athyana_haydenii_Florissant_FLFO_006727B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Athyana_haydenii_Florissant_FLFO_006727B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Sapindaceae_Athyana_haydenii_Florissant_FLFO_006727B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_sp_Florissant_FLFO_008582A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_sp_Florissant_FLFO_008582A.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Sapindaceae_Cardiospermum_sp_Florissant_FLFO_008582A</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Athyana_haydenii_Florissant_FLFO_009652B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Athyana_haydenii_Florissant_FLFO_009652B.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Sapindaceae_Athyana_haydenii_Florissant_FLFO_009652B</div>
                </div>
<div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_terminalis_Florissant_CU_0528cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Sapindaceae/Sapindaceae_Cardiospermum_terminalis_Florissant_CU_0528cu.jpg" alt="Similar fossil specimen"></a>
                    <div class="image-caption">Sapindaceae_Cardiospermum_terminalis_Florissant_CU_0528cu</div>
                </div>
            </div>

            <h3>Similar Extant Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_depressipes_NMNS_T2665.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_depressipes_NMNS_T2665.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_depressipes_NMNS_T2665</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_greggii_NMNS_T2712.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_greggii_NMNS_T2712.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_greggii_NMNS_T2712</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_devia_NMNS_T2666.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_devia_NMNS_T2666.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_devia_NMNS_T2666</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_eduardi_NMNS_T2669.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_eduardi_NMNS_T2669.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_eduardi_NMNS_T2669</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_douglasii_NMNS_T2439.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_douglasii_NMNS_T2439.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_douglasii_NMNS_T2439</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_sororia_NMNS_T2698.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_sororia_NMNS_T2698.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_sororia_NMNS_T2698</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_hypoxantha_NMNS_T2740.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_hypoxantha_NMNS_T2740.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_hypoxantha_NMNS_T2740</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_repanda_NMNS_T2690.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_repanda_NMNS_T2690.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_repanda_NMNS_T2690</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_cedrosensis_NMNS_T2659.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_cedrosensis_NMNS_T2659.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_cedrosensis_NMNS_T2659</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_seemannii_NMNS_T2724.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_seemannii_NMNS_T2724.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_seemannii_NMNS_T2724</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_toumeyi_NMNS_T2701.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_toumeyi_NMNS_T2701.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_toumeyi_NMNS_T2701</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rutaceae/Rutaceae_Ruta_graveolens_NMNS_T2167.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rutaceae/Rutaceae_Ruta_graveolens_NMNS_T2167.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Rutaceae_Ruta_graveolens_NMNS_T2167</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_falcata_NMNS_T2432.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_falcata_NMNS_T2432.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_falcata_NMNS_T2432</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_rugosa_NMNS_T2438.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_rugosa_NMNS_T2438.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_rugosa_NMNS_T2438</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_chapmanii_NMNS_T2371.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_chapmanii_NMNS_T2371.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_chapmanii_NMNS_T2371</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_dumosa_NMNS_T2433.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_dumosa_NMNS_T2433.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_dumosa_NMNS_T2433</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_oxyodon_NMNS_T2475.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_oxyodon_NMNS_T2475.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_oxyodon_NMNS_T2475</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_diversifolia_NMNS_T2709.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_diversifolia_NMNS_T2709.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_diversifolia_NMNS_T2709</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ulmaceae/Ulmaceae_Ulmus_lanceifolia_NMNS_T2531.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ulmaceae/Ulmaceae_Ulmus_lanceifolia_NMNS_T2531.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Ulmaceae_Ulmus_lanceifolia_NMNS_T2531</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_deserticola_NMNS_T2726.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_deserticola_NMNS_T2726.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_deserticola_NMNS_T2726</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_grisea_NMNS_T2435.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_grisea_NMNS_T2435.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_grisea_NMNS_T2435</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_benthamii_NMNS_T2707.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_benthamii_NMNS_T2707.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_benthamii_NMNS_T2707</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_myrtifolia_NMNS_T2472.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_myrtifolia_NMNS_T2472.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_myrtifolia_NMNS_T2472</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_xdysophylla_NMNS_T2734.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_xdysophylla_NMNS_T2734.jpg" alt="Similar extant leaf"></a>
                    <div class="image-caption">Fagaceae_Quercus_xdysophylla_NMNS_T2734</div>
                </div>
            </div>
        </div>

        <div>
            <h2>Concepts</h2>
            <div class="concept-container">
                <div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_1_227.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_1_227.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20227/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_227_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 227</em> - Rank: 1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_2_1745.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_2_1745.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201745/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1745_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1745</em> - Rank: 2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_3_1018.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_3_1018.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201018/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1018_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1018</em> - Rank: 3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_4_1320.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_4_1320.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201320/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1320_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1320</em> - Rank: 4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_5_114.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_5_114.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20114/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_114_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 114</em> - Rank: 5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_6_16.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_6_16.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2016/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_16_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 16</em> - Rank: 6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_7_1966.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_7_1966.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201966/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1966_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 1966</em> - Rank: 7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_8_968.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_8_968.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20968/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_968_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 968</em> - Rank: 8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_9_777.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_9_777.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20777/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_777_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 777</em> - Rank: 9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_10_614.png" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts_viridis/fossil_CU_0769/concept_10_614.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20614/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_614_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em>Concept: 614</em> - Rank: 10</div>
            </div>
            </div>
        </div>
    </div>
</body>
</html>
