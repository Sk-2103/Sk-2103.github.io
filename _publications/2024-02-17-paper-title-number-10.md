---
title: "Automatic extraction of glacial lakes from Landsat imagery using deep learning across the Third Pole"
collection: publications
category: manuscripts
permalink: /publication/2024-02-01-automatic-glacial-lake-extraction
date: 2024-02-01
venue: "Remote Sensing of Environment"
paperurl: "https://doi.org/10.1016/j.rse.2024.114413"
citation: "Tang, Q., Zhang, G., Yao, T., Wieland, M., Liu, L., & Kaushik, S. (2024). Automatic extraction of glacial lakes from Landsat imagery using deep learning across the Third Pole. Remote Sensing of Environment."
---

<figure style="text-align: center;">
    <img src="../images/RSE.jpg" alt="Landslide Susceptibility Assessment" style="width: 60%;">
    <figcaption style="font-size: 14px; color: gray;">
        Figure: Glacial lakes in the TPR in 2020. a–p) The elevation distribution of glacial lakes for various sub-regions and the entire TPR, q) the distribution of glacial lake number and area (km2) on a 1o × 1o grid, where the circle sizes represent number, and the colors are area.
    </figcaption>
</figure>

<style>
  /* Page-scoped abstract size tweak */
  .paper-abstract { font-size: 0.8rem; line-height: 1.6; }
  .paper-abstract h3 { font-size: 1.0rem; margin-top: .5rem; }
</style>

<div class="paper-abstract">
  <h3>Abstract</h3>
  <p>The Tibetan Plateau and surroundings, commonly referred to as the Third Pole region, has the largest ice store outside the Arctic and Antarctic regions. Glacial lakes in the Third Pole region are expanding rapidly as glaciers thin and retreat. The Landsat satellite series is the most popular for mapping glacial lakes, benefiting from long-term archived data and suitable spatial resolution (30 m since ∼1990). However, the homogeneous mapping of high-quality, large-scale, and multi-temporal glacial lake inventories using Landsat imagery relies heavily on visual inspection and manual editing due to mountain shadows, wet ice, frozen lakes, and snow cover on lake boundaries, which is time consuming and labour-intensive. Deep learning methods have been applied to glacial lake extraction in the Third Pole and other regions, yet these methods are either concentrated on small test sites without large-scale applications or in polar regions. In this study, several classical deep convolutional neural networks were evaluated, and the DeepLabv3+ with Mobilenetv3 backbone performed best, with a high accuracy of mean intersection over union (mIoU) of 94.8 % and a low loss error of 0.4 %. The proposed method demonstrated robustness in challenging conditions such as mountain shadows, frozen or partially frozen lakes, wet ice and river contact, all without requiring extensive manual correction. Compared with manual delineation, the model's prediction has a precision rate of 86 %, recall rate of 85 %, and F1-score of 85 %. The area extracted by the model shows a strong correlation with the manual delineation (r2 = 0.97, slope = 0.94) and a high intersection over union (IoU > 0.8) of the predicted areas. A test of large-scale glacial lake mapping based on the developed automated model in 2020 across the Third Pole region shows the robust performance with 29,429 glacial lakes larger than 0.0054 km2 with a total area of ∼1779.9 km2 (including non-glacier-fed lakes). The model trained in this study can be fine-tuned for large-scale mapping of glacial lakes in other mountain regions worldwide.</p>
</div>
