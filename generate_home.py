import json

html_template = """
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

        .authors-section {
            margin: 25px 0;
            font-size: 15px;
            line-height: 1.8;
            color: #4a4a4a;
        }

        .authors {
            margin-bottom: 15px;
        }

        .joint-note {
            font-size: 13px;
            color: #666;
            font-style: italic;
            margin: 10px 0 15px;
        }

        .affiliations {
            font-size: 14px;
            color: #666;
            line-height: 1.6;
        }

        .affiliations strong {
            color: #1a1a1a;
            font-weight: 600;
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
        <p class="subtitle">A machine learning tool to help paleobotanists identify leaf fossils</p>
        
        <div class="authors-section">
            <div class="authors">
                Ivan Felipe Rodriguez🌿 <sup><strong>1</strong></sup>, Thomas Fel🌿 <sup><strong>2</strong></sup>, Gaurav Gaonkar <sup><strong>1</strong></sup>, Mohit Vaishnav <sup><strong>1</strong></sup>,<br>
                Herbert Meyer <sup><strong>4</strong></sup>, Peter Wilf <sup><strong>3</strong></sup> & Thomas Serre🍂<sup><strong>1</strong></sup>
            </div>
            <div class="joint-note">🌿 Joint first authors&nbsp;&nbsp;|&nbsp;&nbsp;🍂 Corresponding author</div>
            <div class="affiliations">
                <sup><strong>1</strong></sup> Brown University,
                <sup><strong>2</strong></sup> Kempner Institute, Harvard University,<br>
                <sup><strong>3</strong></sup> Pennsylvania State University,
                <sup><strong>4</strong></sup> Florissant Fossil Beds, National Park Service
            </div>
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
        
        <p>We are eager to hear from the expert community. Your feedback will help us gauge how many of these classifications are plausible and where further exploration is needed. We look forward to your input in advancing this exciting field!</p>
    </div>

    <div class="section">
        <h3>Website Features</h3>

        <div class="feature-card">
            <h4><span class="feature-badge">1</span>Predicted Fossil Identification</h4>
            <p>You can explore the predicted fossil identifications by clicking on the "Predicted Fossil Identification" link in the navigation bar. This will open a list of fossil specimens. Clicking on a specimen will open a detailed webpage with a predicted fossil information card. This card includes the following information: Dataset catalog number, primary catalog number, model predictions, similar specimens, and concepts.</p>
            
            <h5>Fossil Identification Card</h5>
            <p>In this identification card, you will find details about the Fossil specimen, including its repository number. You can easily find additional metadata for the specimens, including prior identifications, from their filenames (CU- or FLFO- prefix), with these metadata tables kindly provided by Dr. Meyer (see Wilf et al. 2021 for more information about these two image sets):</p>
            <ul>
                <li><a href="https://docs.google.com/spreadsheets/d/1IxU4YjUBWdJyolYbKlNUQetb7sDlN3sV/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true" target="_blank">Florissant CU Metadata</a></li>
                <li><a href="https://docs.google.com/spreadsheets/d/1FIeJoNFIOy22oGVMDgrBZ94EWQ9OZqGLprjPYZRJuLY/edit?usp=sharing" target="_blank">Florissant FLFO Metadata</a></li>
            </ul>
            
            <h5>Similar Specimens</h5>
            <p>Below this you will find the images from our training dataset that are most similar to the provided specimen, with informative filenames as detailed by Wilf et al. 2021.</p>
            
            <h5>Concepts</h5>
            <p>Finally, you will find the concepts that were utilized by the model in the classification process. These concepts are parts of the images that are useful for family identification through the dataset. In this context, concepts are visual or structural patterns in the specimen that the model uses for classification. These often, though not always obviously, correspond to diagnostic leaf architecture traits used in traditional taxonomy, such as leaf margins, venation, symmetry, etc. The concepts are a rich source of potential taxonomically informative characters (see Spagnuolo et al. <a href="https://doi.org/10.1002/ajb2.1842" target="_blank">2022</a>, Intl. J. Plant Sci.) You can also click on them to explore more details about the concept and other families where it occurs.</p>
        </div>
        <div class="feature-card">
            <h4><span class="feature-badge">2</span>Feedback Table</h4>
            <p>The table displays a list of unidentified fossils. Each row contains:</p>
            <ul>
                <li>Image filename (clickable hyperlink; some images are closeups of others)</li>
                <li>Fossil image of the given specimen</li>
                <li>Top five predictions (clickable hyperlink to concept page for the indicated plant family)</li>
                <li>Feedback options: Use the color-coded buttons to mark each prediction as <span class="feedback-option plausible">Plausible</span>, <span class="feedback-option impossible">Impossible</span>, <span class="feedback-option not-sure">Not Sure</span>, or <span class="feedback-option not-applicable">Not Applicable</span>. Please simply skip over poorly preserved or inapplicable specimens (see Disclaimers below for details).</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <h3>The Feedback Procedure</h3>
        <p>You can interact with each fossil prediction by:</p>
        
        <div class="feature-card">
            <p><strong>1. For each row you can mark any of the following interactions:</strong></p>
            <ul>
                <li><span class="feedback-option plausible">Plausible</span> - In your best judgement, one or multiple of the families proposed can be actually the family of the specimen.</li>
                <li><span class="feedback-option impossible">Impossible</span> - No way! None of the predictions make sense for this specimen.</li>
                <li><span class="feedback-option not-sure">Not Sure</span> - You don't recognize the features of all the top-5 families offered by the system, and further study is needed.</li>
                <li><span class="feedback-option not-applicable">Not Applicable</span> - The specimen doesn't belong in the dataset (e.g., non-dicot leaf, too degraded, or not a leaf fossil).</li>
            </ul>
        </div>

        <div class="feature-card">
            <p><strong>2. Response Tracking</strong></p>
            <ul>
                <li>Use the <span style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: white; padding: 4px 12px; border-radius: 6px; font-weight: 500;">📥 Download Responses</span> button (bottom right) to save your choices as a JSON file.</li>
                <li><strong>Important:</strong> Download before closing the website to avoid losing responses.</li>
            </ul>
        </div>

        <div class="feature-card">
            <p><strong>3. Resuming Your Work</strong></p>
            <ul>
                <li>You can resume work using serial numbers during your next visit.</li>
            </ul>
        </div>

        <div class="feature-card">
            <p><strong>4. Sending your feedback:</strong> Your feedback on any portion of the dataset is greatly appreciated. Feel free to send the downloaded JSON file to <a href="mailto:ivan_felipe_rodriguez@brown.edu">ivan_felipe_rodriguez@brown.edu</a></p>
        </div>
    </div>

    <div class="section">
        <h3>Disclaimers</h3>
        
        <div class="feature-card" style="border-left-color: #f59e0b;">
            <p><strong>Please note:</strong> While our dataset is extensive, many fossil samples are badly preserved and may lack the detail needed for accurate classification. In addition, although the images were manually filtered several years ago to remove most that are inappropriate, there remain many images of monocots and non-angiosperms (which are severely undersampled in the training dataset), reproductive organs (likewise), and non-plant fossils (feathers, fish, and so on). We recommend simply skipping these poorly preserved or inapplicable specimens to ensure more reliable results.</p>
        </div>

        <div class="feature-card">
            <p>Finally, please be aware that the model can only predict families that are in its training dataset, listed <a href="https://docs.google.com/document/d/178X6Stw9_J4k-Ib9lp8eWAH8tUv86rtg8VBqZPeVuWw/edit?usp=sharing" target="_blank">here</a>.</p>
        </div>
        
        <div class="highlight-box">
            <p><em>We invite you to explore this innovative blend of paleobotany and artificial intelligence, and to join us in refining the art and science of fossil leaf identification!</em></p>
        </div>
    </div>

</div>

</body>
</html>

"""

# Save to an HTML file
with open("./docs/index.md", "w") as f:
    f.write(html_template)

print("HTML file generated: index.md")