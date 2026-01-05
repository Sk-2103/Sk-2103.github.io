---
layout: single
title: "Debris covered glacier mapping using newly annotated multisource remote sensing data and geo-foundational model"
collection: publications
permalink: /publication/2025-10-12-publication
category: manuscripts
date: 2025-02-01
venue: "Science of Remote Sensing"
paperurl: "https://doi.org/10.1016/j.srs.2025.100319"
citation: "Kaushik, S.*, Maurya, L., Tellman, E., Zhang, G., & Dharpure, J. K. (2025). Advancing supraglacial debris mapping at a global scale using newly annotated remote sensing data and a geo-foundational model. (Under-Review)."
permalink: https://doi.org/10.1016/j.srs.2025.100319
show_date: false
---

{% include base_path %}

<figure style="text-align:center;">
  <img src="{{ '/images/glacier1.jpg' | relative_url }}" alt="Fine-tuning Prithvi GFM for supraglacial debris mapping" style="width:60%;">
  <figcaption style="font-size:14px;color:gray;">
    Figure: Correlation and IoU of supraglacial debris area between the Prithvi model and manually corrected ground-truth data.
  </figcaption>
</figure>

<figure style="text-align:center;">
  <img src="{{ '/images/glacier2.jpg' | relative_url }}" alt="Model comparison for supraglacial debris mapping" style="width:60%;">
  <figcaption style="font-size:14px;color:gray;">
    Figure: Comparison of different deep-learning models for supraglacial debris mapping.
  </figcaption>
</figure>

<div class="paper-abstract">
  <h3>Abstract</h3>
  <p>The automated mapping of debris covered glaciers remains challenging due to spectral similarity between supraglacial debris (on-glaciers) and periglacial debris (off-glaciers). Deep learning offers promising capabilities, yet the lack of high-quality publicly available datasets and limited exploration of optimal model architecture constrain progress in this domain. To address this, we introduce the Global Supraglacial Debris Cover Dataset (GSDD), consisting of 1876 images (∼49,000.00 km2) collected globally from diverse glacierized regions, including High Mountain Asia, Andes, Western Canada, Alaska, and Swiss Alps, to incorporate the heterogeneity of glacial features and environments. This multisource remote sensing dataset includes 10 spectral bands—Blue, Green, Red, Near-Infrared, Shortwave Infrared (SWIR1 & SWIR2), Normalized Difference Rock Index (NDRI), Slope, Elevation, and Velocity—providing critical information to distinguish glacier debris. To evaluate the efficacy of deep learning models for mapping glacier debris, we compare Prithvi Geo-Foundational Model (GFM) combined with multiple decoders, CNN-based models (UNet, Attention U-Net, and DeepLabv3+), a Vision Transformer-based model (TransNorm), and variant of the Prithvi GFM (i.e., UViT). Our results show Prithvi GFM with UperNet decoder outperformed all, achieving mIoU = 0.80 and F1-score = 0.91, surpassing DeepLabv3+ (0.71 mIoU), Attention U-Net (0.73), U-Net (0.72), TransNorm (0.71), and UViT (0.70). Our results demonstrate significant methodological advances in accurately mapping glacier termini, along with the identification of glacier snouts. Feature analysis identified the optimal band combination (B-G-NIR-SWIR-Slope-Elevation) for debris mapping. The GSDD dataset enables direct comparison, development, and evaluation of deep learning models, supporting advancement in fast and reliable automated glacier mapping.</p>
</div>
