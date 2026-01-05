---
layout: single
title: "DL4EO: A Unified Python Framework for Preparing Multi-Source Remote Sensing Data for any Segmentation Task"
collection: publications
category: manuscripts
permalink: /publication/2025-06-10-publication
show_date: false
paperurl: ""
citation: "Kaushik, S., Tellman, B. (2025). DL4EO: A Unified Python Framework for Preparing Multi-Source Remote Sensing Data for any Segmentation Task. (Under-Review)."
---

{% include base_path %}

<p><strong>Status:</strong> Under-Review</p>

<figure style="text-align: center;">
  <img src="{{ '/images/dl4eo_1.png' | relative_url }}" alt="DL4EO overall workflow" style="width: 60%;">
  <figcaption style="font-size: 14px; color: gray;">
    Figure: Overall workflow of the DL4EO package, subdivided into four parts:
    (1) acquiring and processing Sentinel-2, (2) acquiring and processing topographic layers,
    (3) acquiring and processing Sentinel-1, and (4) mask/label generation and image normalization.
  </figcaption>
</figure>

<figure style="text-align: center;">
  <img src="{{ '/images/dl4eo_2.png' | relative_url }}" alt="DL4EO example usage for glacial lake segmentation" style="width: 60%;">
  <figcaption style="font-size: 14px; color: gray;">
    Figure: Example DL4EO use case generating multi-source remote sensing inputs
    for glacial lake segmentation in Central Europe.
  </figcaption>
</figure>

<figure style="text-align: center;">
  <img src="{{ '/images/dl4eo_3.png' | relative_url }}" alt="DL4EO Python code example" style="width: 60%;">
  <figcaption style="font-size: 14px; color: gray;">
    Figure: Python example for generating training and validation datasets for Earth Observation segmentation tasks.
  </figcaption>
</figure>

<div class="paper-abstract">
  <h3>Abstract</h3>
  <p>Deep Learning (DL) has transformed Earth Observation (EO) tasks such as vegetation mapping, building detection, and water body monitoring by enabling fast and reliable spatiotemporal analysis. Yet, global-scale applications remain limited due to the un-availability of readily available datasets and complexity involved in processing planetary scale datasets. To address this, we present DL4EO, a Python package that simplifies the preparation of remote sensing data for deep learning. It automatically downloads and processes Sentinel-1 (RTC), Sentinel-2 (Level 2C), and Copernicus DEM data, generating consistent image-label pairs of user-defined size without requiring credentials. As an input, package requires a base directory, date range, cloud cover threshold, area of interest (AOI), and a shapefile of the target feature. To acquire Sentinel-1 RTC data, DL4EO selects the closest available image based on the corresponding Sentinel-2 acquisition. It handles projection, resampling, and alignment to produce globally consistent datasets. The final output consists of user define size (e.g., 256×256) images with 11 bands: Blue, Green, Red, NIR, SWIR1, SWIR2, spectral band (e.g., Normalized Difference Water Index: NDWI), Slope, Elevation, VV, and VH and corresponding label mask, target feature with pixel value 1 and rest 0. This fully automated dataset preparation pipeline supports scalable and efficient deep learning applications in Earth observation.</p>
</div>
