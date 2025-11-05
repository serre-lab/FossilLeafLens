# Fossil Leaf Lens

> A machine learning tool to help paleobotanists identify leaf fossils

<p align="center">
  <a href="https://serre-lab.github.io/LeafLens/">
    <img src="https://img.shields.io/badge/Visit-Leaf%20Lens-2e7d32?style=for-the-badge&logo=leaflet&logoColor=white">
  </a>
  &nbsp;&nbsp;
  <a href="https://serre-lab.github.io/FossilLeafLens/">
    <img src="https://img.shields.io/badge/Visit-Fossil%20Leaf%20Lens-5e4a2e?style=for-the-badge&logo=microscope&logoColor=white">
  </a>
</p>

<p align="center">
  Explore concepts and family classification | Identify unknown fossils
</p>

---

## Authors

<p align="center">
  Ivan Felipe Rodriguez<sup>1🌿</sup>,
  Thomas Fel<sup>1,2🌿</sup>,
  Gaurav Gaonkar<sup>1</sup>,
  Mohit Vaishnav<sup>1</sup>,
  Herbert Meyer<sup>3</sup>, <br>
  Peter Wilf<sup>4</sup>,
  Thomas Serre<sup>1🍂</sup>
</p>

<p align="center">
  <a href="https://serre.lab.brown.edu/"><img src="docs/images/brown.png" height="30"></a>
  &nbsp;&nbsp;
  <a href="https://kempnerinstitute.harvard.edu/"><img src="docs/images/harvard.png" height="30"></a>
  &nbsp;&nbsp;
  <a href="https://www.nps.gov/flfo/index.htm"><img src="docs/images/nps.png" height="30"></a>
  &nbsp;&nbsp;
  <a href="https://www.upenn.edu/"><img src="docs/images/penn.png" height="30"></a>
</p>

<p align="left">
  <sup>1</sup> Center for Computational Brain Science, Brown University
  <br>
  <sup>2</sup> Kempner Institute, Harvard University
  <br>
  <sup>3</sup> Florissant Fossil Beds National Monument, National Park Service
  <br>
  <sup>4</sup> Department of Geosciences, Pennsylvania State University
  <br><br>
  🌿 Joint first authors&nbsp;&nbsp;|&nbsp;&nbsp;🍂 Corresponding author
</p>

---

## Overview

Fossil Leaf Lens is a web application that addresses one of paleobotany's most challenging puzzles: identifying fossil angiosperm leaves. These organs are often abundant yet notoriously difficult to classify, especially in the absence of organic attachments or cuticles, due to their complexity, variation, and the often limited quality and quantity of available images.

Through the power of AI and computer vision, we have developed a deep learning model that synthesizes photorealistic fossil images from extant cleared and x-rayed leaves, increasing the sample size of "fossil" image collections for training. This approach allows machine identifications of fossil and extant leaves at the family level—the starting point for most investigations—with levels of accuracy sufficient to provide useful suggestions for experts.

## Website Features

![Fossil Leaf Lens Navigation Guide](docs/images/fossil.gif)

*Interactive navigation guide showing how to use the Fossil Leaf Lens website*

### 1. Predicted Fossil Identification

Explore predicted fossil identifications through detailed webpages for each specimen. Each page includes:

- **Fossil Information Card**: Dataset catalog number, primary catalog number, and model predictions
- **Similar Specimens**: Images from the training dataset most similar to the specimen
- **Concepts**: Visual patterns the model uses for classification, corresponding to diagnostic leaf architecture traits

#### Metadata Resources

- [Florissant CU Metadata](https://docs.google.com/spreadsheets/d/1IxU4YjUBWdJyolYbKlNUQetb7sDlN3sV/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true)
- [Florissant FLFO Metadata](https://docs.google.com/spreadsheets/d/1FIeJoNFIOy22oGVMDgrBZ94EWQ9OZqGLprjPYZRJuLY/edit?usp=sharing)

### 2. Feedback Table

The feedback table allows expert paleobotanists to evaluate model predictions:

- View unidentified fossil specimens with images
- Review top 5 model predictions for each specimen
- Provide feedback using color-coded options:
  - **Plausible**: One or more families are likely correct
  - **Impossible**: No predictions make sense
  - **Not Sure**: Further study needed
  - **Not Applicable**: Specimen doesn't belong

---

## Dataset

The project focuses on leaf fossils from the **Florissant Fossil Beds** (late Eocene, Colorado), one of the world's most well-studied and photo-documented fossil sites. The images were gathered over many years by Dr. Herbert Meyer (retired, National Parks Service) and assistants from museums around the world.

### References

- Meyer et al. (2008). GSA Special Papers 435. [DOI: 10.1130/2008.2435(11)](https://doi.org/10.1130/2008.2435(11))
- Wilf et al. (2021). PhytoKeys. [DOI: 10.3897/phytokeys.187.72350](https://doi.org/10.3897/phytokeys.187.72350)
- Image Collection: [DOI: 10.25452/figshare.plus.14980698.v2](https://doi.org/10.25452/figshare.plus.14980698.v2)

---

## Usage

### For Paleobotanists

1. Navigate to the [Fossil Leaf Lens website](https://serre-lab.github.io/FossilLeafLens/)
2. Browse predicted fossil identifications from the navigation menu
3. Review individual specimen pages with detailed predictions
4. Use the Feedback Table to evaluate and provide feedback on predictions
5. Download your feedback as a JSON file and send to: [ivan_felipe_rodriguez@brown.edu](mailto:ivan_felipe_rodriguez@brown.edu)

---

## Limitations & Disclaimers

- The dataset includes many fossil samples that are badly preserved and may lack detail needed for accurate classification
- Some images may include monocots, non-angiosperms, reproductive organs, or non-plant fossils that are undersampled in the training dataset
- The model can only predict families present in its training dataset ([list available here](https://docs.google.com/document/d/178X6Stw9_J4k-Ib9lp8eWAH8tUv86rtg8VBqZPeVuWw/edit?usp=sharing))
- We recommend skipping poorly preserved or inapplicable specimens

---

## Contact

For questions, feedback, or collaboration inquiries, please contact:

**Ivan Felipe Rodriguez**  
📧 [ivan_felipe_rodriguez@brown.edu](mailto:ivan_felipe_rodriguez@brown.edu)  
🏛️ Brown University

---

## Citation

If you use Fossil Leaf Lens in your research, please cite:

Rodriguez, I.F., Fel, T., Gaonkar, G., Vaishnav, M., Meyer, H., Wilf, P., & Serre, T. (2025). Decoding Fossil Leaves with Artificial Intelligence: An application to the Florissant Formation.

```bibtex
@article{rodriguez2025fossils,
  title  = {Decoding Fossil Leaves with Artificial Intelligence: 
            An application to the Florissant Formation},
  author = {Rodriguez, Ivan Felipe and Fel, Thomas and Gaonkar, Gaurav and 
            Vaishnav, Mohit and Meyer, Herbert and Wilf, Peter and Serre, Thomas},
  year   = {2025}
}
```

---

**We invite you to explore this innovative blend of paleobotany and artificial intelligence, and to join us in refining the art and science of fossil leaf identification!** 🌿🔬

