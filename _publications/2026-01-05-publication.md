---
title: "Prithvi-Complimentary Adaptive Fusion Encoder (CAFE): unlocking full-potential for flood inundation mapping"
collection: publications
category: manuscripts
permalink: /publication/2026-01-05-publication
date: 2026-01-05
venue: "WACV (CV4EO-Workshop)"
paperurl: "https://arxiv.org/abs/2601.02315"
citation: "Kaushik Saurabh, Maurya Lalit, Tellman Beth (2026). Prithvi-Complimentary Adaptive Fusion Encoder (CAFE): unlocking full-potential for flood inundation mapping (CV4EO-Workshop)"
---
<figure style="text-align: center;">
    <img src="../images/CAFE.png" alt="Landslide Susceptibility Assessment" style="width: 60%;">
    <figcaption style="font-size: 14px; color: gray;">
        Figure: Overview of  Prithvi-CAFE architecture.
    </figcaption>
</figure>



<div class="paper-abstract">
  <h3>Abstract</h3>
  <p>Geo-Foundation Models (GFMs), have proven effective in
diverse downstream applications, including semantic segmentation,
classification, and regression tasks. However,
in case of flood mapping using Sen1Flood11 dataset as a
downstream task, GFMs struggles to outperform the baseline
U-Net, highlighting model’s limitation in capturing
critical local nuances. To address this, we present the
Prithvi-Complementary Adaptive Fusion Encoder (CAFE),
which integrate Prithvi GFM pretrained encoder with a
parallel CNN residual branch enhanced by Convolutional
Attention Modules (CAM). Prithvi-CAFE enables fast and
efficient fine-tuning through adapters in Prithvi and performs
multi-scale, multi-level fusion with CNN features,
capturing critical local details while preserving long-range
dependencies. We achieve state-of-the-art results on two
comprehensive flood mapping datasets: Sen1Flood11 and
FloodPlanet. On Sen1Flood11 test data, Prithvi-CAFE
(IoU 83.41) outperforms the original Prithvi (IoU 82.50)
and other major GFMs (TerraMind 82.90, DOFA 81.54,
spectralGPT: 81.02). The improvement is even more pronounced
on the hold-out test site, where Prithvi-CAFE
achieves an IoU of 81.37 compared to the baseline UNet
(70.57) and original Prithvi (72.42). On FloodPlanet,
Prithvi-CAFE also surpasses the baseline U-Net and other
GFMs, achieving an IoU of 64.70 compared to U-Net
(60.14), Terramind (62.33), DOFA (59.15) and Prithvi 2.0
(61.91). Our proposed simple yet effective Prithvi-CAFE
demonstrates strong potential for improving segmentation
tasks where multi-channel and multi-modal data provide
complementary information and local details are critical. </p>
</div>


