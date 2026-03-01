
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens</title>
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
            max-width: 850px;
            margin: 0 auto;
            padding: 20px 40px 80px;
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
            padding-bottom: 40px;
            border-bottom: 1px solid #e8e8e8;
        }

        h1 {
            font-size: 38px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 15px;
            letter-spacing: -0.5px;
        }

        .subtitle {
            font-size: 18px;
            color: #666;
            font-style: italic;
            font-weight: 400;
        }

        .header-partners {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 28px 48px;
            margin-top: 24px;
            font-size: 16px;
        }

        .header-partners a {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            color: #1a1a1a;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s, opacity 0.2s;
        }

        .header-partners a:hover {
            color: #2563eb;
            opacity: 0.9;
        }

        .header-partners img {
            height: 32px;
            width: auto;
            display: block;
        }

        .citation-section {
            margin-top: 60px;
            padding-top: 40px;
            border-top: 1px solid #e8e8e8;
        }

        .citation-section h3 {
            margin-bottom: 12px;
        }

        .citation-section > p:first-of-type {
            color: #4a4a4a;
            font-size: 15px;
            margin-bottom: 16px;
        }

        .citation-box {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 28px 32px;
            margin-top: 8px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        }

        .citation-text {
            font-family: 'Courier New', Courier, monospace;
            font-size: 15px;
            line-height: 1.7;
            margin: 0;
            color: #1e293b;
            letter-spacing: 0.02em;
        }

        .citation-note {
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid #e2e8f0;
            font-size: 14px;
            color: #64748b;
            font-style: italic;
        }

        .demo-section {
            margin: 50px 0 60px;
            text-align: center;
        }

        .demo-gif {
            width: 100%;
            max-width: 450px;
            margin: 0 auto;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease;
        }

        .demo-gif:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
        }

        .demo-gif img {
            width: 100%;
            height: auto;
            display: block;
        }

        .section {
            margin-bottom: 45px;
        }

        h3 {
            font-size: 24px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 20px;
            margin-top: 40px;
            letter-spacing: -0.3px;
        }

        h4 {
            font-size: 20px;
            font-weight: 600;
            color: #2a2a2a;
            margin-bottom: 12px;
            margin-top: 32px;
        }

        h5 {
            font-size: 16px;
            font-weight: 600;
            color: #4a4a4a;
            margin-bottom: 10px;
            margin-top: 24px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-size: 12px;
        }

        p {
            color: #4a4a4a;
            margin-bottom: 20px;
            font-size: 16px;
            line-height: 1.75;
        }

        a {
            color: #2563eb;
            text-decoration: none;
            border-bottom: 1px solid rgba(37, 99, 235, 0.2);
            transition: all 0.2s ease;
        }

        a:hover {
            color: #1d4ed8;
            border-bottom-color: #1d4ed8;
        }

        ul, ol {
            margin-left: 24px;
            margin-bottom: 20px;
            color: #4a4a4a;
        }

        li {
            margin-bottom: 12px;
            font-size: 16px;
            line-height: 1.7;
        }

        ul ul {
            margin-top: 8px;
            margin-bottom: 0;
        }

        .intro-text {
            font-size: 16px;
            line-height: 1.8;
            color: #4a4a4a;
        }

        .feature-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: white;
            font-size: 16px;
            font-weight: 700;
            border-radius: 8px;
            margin-right: 12px;
        }

        .section-beyond .feature-badge {
            background: transparent;
            color: inherit;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.2);
        }

        .feature-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            border-left: 4px solid #2563eb;
            transition: all 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }

        .highlight-box {
            background: linear-gradient(135deg, #f0fdf4 0%, #e8faf0 100%);
            border-left: 4px solid #22c55e;
            padding: 20px 24px;
            margin: 30px 0;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(34, 197, 94, 0.1);
        }

        .highlight-box p {
            margin-bottom: 0;
            color: #2a2a2a;
            font-size: 17px;
        }

        .feedback-option {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            border-radius: 6px;
            font-weight: 500;
            font-size: 14px;
            margin: 4px;
        }

        .feedback-option.plausible {
            background-color: #d1fae5;
            color: #065f46;
            border: 1px solid #6ee7b7;
        }

        .feedback-option.impossible {
            background-color: #fee2e2;
            color: #991b1b;
            border: 1px solid #fca5a5;
        }

        .feedback-option.not-sure {
            background-color: #fef3c7;
            color: #92400e;
            border: 1px solid #fcd34d;
        }

        .feedback-option.not-applicable {
            background-color: #f3f4f6;
            color: #4b5563;
            border: 1px solid #d1d5db;
        }

        .section li {
            padding: 8px 0;
            transition: all 0.2s ease;
        }

        .funding-section {
            margin-top: 60px;
            padding-top: 40px;
            border-top: 1px solid #e8e8e8;
        }

        .funding-logo {
            text-align: center;
            margin: 20px 0;
        }

        .funding-logo img {
            max-width: 200px;
            height: auto;
            opacity: 0.9;
            transition: opacity 0.2s ease;
        }

        .funding-logo img:hover {
            opacity: 1;
        }

        .section li:hover {
            transform: translateX(4px);
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px 24px 60px;
            }

            h1 {
                font-size: 30px;
            }

            .subtitle {
                font-size: 16px;
            }

            .authors-section {
                font-size: 14px;
            }

            .authors {
                font-size: 14px;
            }

            .affiliations {
                font-size: 13px;
            }

            h3 {
                font-size: 22px;
            }

            h4 {
                font-size: 18px;
            }
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>Fossil Leaf Lens</h1>
        <p class="subtitle">A showcase of deep learning predictions for fossil leaf identification</p>
        <div class="header-partners">
            <a href="https://serre-lab.github.io/LeafLens/" target="_blank" rel="noopener">
                <img src="images/leaflenslogo.png" alt="">
                <span>Leaf Lens</span>
            </a>
            <a href="https://huggingface.co/spaces/Serrelab/fossil_app" target="_blank" rel="noopener">
                <img src="images/huggingfacelogo.png" alt="">
                <span>Deep Learning Tool</span>
            </a>
        </div>
    </div>

    <div class="demo-section">
        <div class="demo-gif">
            <img src="images/fossil.gif" alt="Leaf Lens Navigation Guide">
        </div>
    </div>

    <div class="section">
        <h3>Welcome to Fossil Leaf Lens</h3>
        <p class="intro-text">We are excited to share the fruits of years of research and innovation aimed at solving one of paleobotany's most challenging puzzles: identifying fossil angiosperm leaves. These organs are often abundant yet notoriously difficult to classify, especially in the absence of organic attachments or cuticles, due to their complexity, variation, and the often limited quality and quantity of available images.</p>
        
        <p>Through the power of AI and computer vision, we have developed a deep learning model that synthesizes photorealistic fossil images from extant cleared and x-rayed leaves, increasing the sample size of "fossil" image collections for training. As explained in our accompanying manuscript (<a href="www.google.com" target="_blank">coming soon</a>), this approach allows machine identifications of fossil and extant leaves at the family level, the starting point for most investigations, with levels of accuracy sufficient to provide useful suggestions for experts.</p>
        
        <p>Initially, to limit the immense variation in leaf preservation among fossil sites, we present the tool for leaf fossils from a single, extraordinarily well-studied and photo-documented site: Florissant Fossil Beds, late Eocene of Colorado. The images were gathered over many years by Dr. Herbert Meyer (retired, National Parks Service) and assistants from museums around the world, as explained by Meyer et al. <a href="https://doi.org/10.1130/2008.2435(11)" target="_blank">2008</a> (GSA Special Papers 435) and Wilf et al. <a href="https://doi.org/10.3897/phytokeys.187.72350" target="_blank">2021</a> (PhytoKeys), who made a vetted subset of Florissant fossils available as part of a large <a href="https://doi.org/10.25452/figshare.plus.14980698.v2" target="_blank">image collection</a> of living and fossil leaves.</p>
        
        <p>The accompanying manuscript explores machine identifications of vetted Florissant fossils from the Wilf et al. 2021 dataset. On this website, we show the broader potential of the method by sharing the results of our model for hundreds of hard-to-identify fossil leaves from Florissant that were not included in the 2021 vetted subset, including both unidentified specimens and those attributed previously to botanical names that are now uncertain. The model's training images include the vetted Florissant images and all the cleared and x-rayed leaf images described in Wilf et al. 2021. We hope that this tool will stimulate new research into the world-famous Florissant flora, as we work to generalize the algorithms to apply to other fossil sites.</p>
        
        </div>

    <div class="section section-beyond">
        <h3>Beyond this site</h3>
        <div class="feature-card" style="border-left-color: #f59e0b;">
            <h4><span class="feature-badge"><img src="images/huggingfacelogo.png" alt="" style="height: 20px; width: auto;"></span>Use the tool</h4>
            <p>To run the deep learning model on your own fossil leaf images, use our <strong><a href="https://huggingface.co/spaces/Serrelab/fossil_app" target="_blank" rel="noopener">Hugging Face app</a></strong>. It is the interactive interface to the same model whose predictions we display on this website.</p>
            <p><a href="https://huggingface.co/spaces/Serrelab/fossil_app" target="_blank" rel="noopener" style="font-weight: 600;">→ Open the Hugging Face app</a></p>
        </div>
        <div class="feature-card" style="border-left-color: #800000;">
            <h4><span class="feature-badge"><img src="images/leaflenslogo.png" alt="" style="height: 20px; width: auto;"></span>Explore concepts on the full dataset</h4>
            <p><strong><a href="https://serre-lab.github.io/LeafLens/" target="_blank" rel="noopener">Leaf Lens</a></strong> lets you explore the concepts the model learned across the entire training set: UMAP visualizations of families and concepts, concept pages, and family-level interpretability. Use it to dig into how the model organizes and uses visual features for classification.</p>
            <p><a href="https://serre-lab.github.io/LeafLens/" target="_blank" rel="noopener" style="font-weight: 600;">→ Go to Leaf Lens</a></p>
        </div>
    </div>

    <div class="section">
        <h3>Browsing predictions on this site</h3>

        <div class="feature-card">
            <h4><span class="feature-badge">1</span>Predicted Fossil Identifications</h4>
            <p>Use <strong>Predicted Fossil Identifications</strong> in the navigation bar to open the list of specimens. Click a specimen to see details and model predictions about the specimens, including: catalog numbers, model predictions (family-level), similar specimens from the training set, and the concepts the model used for that specimen.</p>
            <p>You can easily find additional metadata for the specimens, including prior identifications, from their filenames (CU- or FLFO- prefix), with these metadata tables kindly provided by Dr. Meyer (see Wilf et al. 2021 for more information about these two image sets):</p>
            <ul>
                <li><a href="https://docs.google.com/spreadsheets/d/1MVLtYOfBZZojKW3B-LHKmD0kI0f8kAY1JtaAuBs47i4/edit?usp=sharing" target="_blank">Florissant CU Metadata</a></li>
                <li><a href="https://docs.google.com/spreadsheets/d/1y4eec8r3oBROz6wzvJWLLcl9w4GdGq8MBoWjLIUzRx0/edit?usp=sharing" target="_blank">Florissant FLFO Metadata</a></li>
            </ul>
        </div>
    </div>

    <div class="section">
        <h3>Disclaimers</h3>
        
        <div class="feature-card" style="border-left-color: #f59e0b;">
            <p><strong>Please note:</strong></p>
            <ul>
            <li>While our dataset is extensive, many fossil samples are badly preserved and may lack the detail needed for accurate classification. In addition, although the images were manually filtered several years ago to remove most that are inappropriate, there remain many images of monocots and non-angiosperms (which are severely undersampled in the training dataset), reproductive organs (likewise), and non-plant fossils (feathers, fish, and so on). We recommend simply skipping these poorly preserved or inapplicable specimens to ensure more reliable results.</li>
            <li>This tool is intended to assist paleobotanists by suggesting potentially overlooked identifications with supporting visualizations. It can accelerate discovery when used wisely, but it is no substitute for botanical and paleobotanical expertise. In practice, we find many machine suggestions helpful, but even inaccurate suggestions provide novel insights into fossil-leaf morphology through the Leaf Lens heat maps.</li>
            <li>Finally, please be aware that the model can only predict families that are in its training dataset, listed <a href="https://docs.google.com/document/d/178X6Stw9_J4k-Ib9lp8eWAH8tUv86rtg8VBqZPeVuWw/edit?usp=sharing" target="_blank">here</a>.</li>
            </ul>
        </div>
        
        <div class="highlight-box">
            <p><em>We invite you to browse the predictions and to cite our paper when you use this resource or the associated model.</em></p>
        </div>
    </div>

    <div class="section funding-section">
        <h3>Acknowledgments</h3>
        
        <div class="feature-card">
            <div class="funding-logo">
                <img src="images/nsf.png" alt="National Science Foundation">
            </div>
            
            <p>This material is based upon work supported by the U.S. <strong>National Science Foundation</strong> under Award No. <strong>EAR-1925481</strong> (T.S.) and <strong>EAR-1925755</strong> (P.W.), and by <strong>ANR-3IA Artificial and Natural Intelligence Toulouse Institute</strong> (<strong>ANR-19-PI3A-0004</strong>).</p>
            
            <p><em>Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.</em></p>
            
            <p>Computing support was provided by the Center for Computation and Visualization (CCV) at Brown University (via NIH Office of the Director grant S10OD025181). We also acknowledge Google's Cloud TPU hardware resources via the TensorFlow Research Cloud (TFRC) program.</p>
        </div>
    </div>

    <div class="section citation-section">
        <h3>Citation</h3>
        <p>Please cite our primary article when using this resource or the associated model:</p>
        <div class="citation-box">
            <p class="citation-text">Rodriguez, I.F., Fel, T., Gaonkar, G., Vaishnav, M., Meyer, H., Wilf, P., &amp; Serre, T. (2025). Advancing Paleobotany with AI-guided Expert Fossil Leaf Identification.</p>
            <p class="citation-note">Manuscript in preparation, please cite the primary article once published.</p>
        </div>
    </div>

</div>

</body>
</html>

