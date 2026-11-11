---
title: "FloodDuo: A Dual Foundation-Encoder Architecture for Generalizable High-Resolution Flood Mapping"
collection: publications
category: manuscripts
permalink: /publication/floodduo
date: 2026-11-11
venue: "ISPRS Journal of Photogrammetry and Remote Sensing"
paperurl: "https://doi.org/10.1016/j.isprsjprs.2026.10.041"
codeurl: "https://github.com/Sk-2103/FloodDuo"
citation: "Kaushik, S., Tellman, B., Weng, Q. (2026). FloodDuo: A Dual Foundation-Encoder Architecture for Generalizable High-Resolution Flood Mapping. ISPRS Journal of Photogrammetry and Remote Sensing. https://doi.org/10.1016/j.isprsjprs.2026.10.041"
---

<p><strong>Status:</strong> Published in <a href="https://doi.org/10.1016/j.isprsjprs.2026.10.041" target="_blank" rel="noopener">ISPRS Journal of Photogrammetry and Remote Sensing</a> · <a href="https://github.com/Sk-2103/FloodDuo" target="_blank" rel="noopener">Code</a> · <a href="https://huggingface.co/Sk-21/FloodDuo" target="_blank" rel="noopener">Model (Hugging Face)</a></p>

<figure style="text-align: center;">
  <img src="{{ '/images/floodduo_architecture.png' | relative_url }}" alt="FloodDuo dual-encoder architecture" style="width: 75%;">
  <figcaption style="font-size: 14px; color: gray;">
    Figure: FloodDuo pairs two frozen foundation-model encoders — DINOv3-L (RGB) for spatial/boundary detail and Clay v1.5 (4-band) for spectral discrimination — each adapted with lightweight trainable modules, merged through a disagreement-gated fusion, and decoded with LinkNet into the final flood mask.
  </figcaption>
</figure>

<figure style="text-align: center;">
  <img src="{{ '/images/floodduo_predictions.png' | relative_url }}" alt="FloodDuo predictions compared to U-Net, DOFA, and TerraMind" style="width: 85%;">
  <figcaption style="font-size: 14px; color: gray;">
    Figure: Representative held-out FloodPlanet predictions (Nigeria, US-Oklahoma, Ghana) comparing FloodDuo against U-Net, DOFA, and TerraMind, with per-tile IoU shown.
  </figcaption>
</figure>

<div class="paper-abstract">
  <h3>Abstract</h3>
  <p>FloodDuo maps open water in high-resolution (3 m, 4-band B/G/R/NIR PlanetScope) post-flood imagery by pairing two frozen vision foundation-model encoders that carry complementary information: DINOv3-L (RGB) for sharp spatial/boundary detail, and Clay v1.5 (all four bands) for wavelength-conditioned spectral discrimination. Each frozen backbone is adapted with lightweight trainable modules — an in-block frequency-domain Earth-Adapter, plus post-hoc atrous-convolution and pyramid-pooling adapters — and the two branches are merged through a disagreement-gated fusion whose per-pixel Jensen-Shannon divergence doubles as a label-free reliability map, before a LinkNet decoder produces the full-resolution mask. Only ~65M parameters are trained against ~614M frozen. Evaluated under leave-one-region-out cross-validation across 19 FloodPlanet regions and 14 Urban Flood Observation (UFO) event sites — a protocol that exposes the cross-region generalization gap a conventional random split hides — FloodDuo achieves 0.728 IoU on FloodPlanet and 0.819 IoU on UFO, outperforming the strongest single-encoder geospatial foundation model baseline by 2.8–3.0 points and a from-scratch U-Net by 3.7–8.0 points.</p>
</div>
