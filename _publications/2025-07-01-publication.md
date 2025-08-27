---
layout: single
title: "Beyond Clouds: Global glacial lake mapping combining sentinel-1 and sentinel-2 remote sensing data and geo-foundational model"
collection: publications
category: manuscripts
status: "Under-Review"
paperurl: ""
citation: "Kaushik, S., Tellman, B., Howat, I. (2025). Beyond Clouds: Global glacial lake mapping combining Sentinel-1 and Sentinel-2 remote sensing data and a geo-foundational model. (Under-Review)."
permalink: /publication/beyond-clouds/
show_date: false
---

{% include base_path %}

<p><strong>Status:</strong> Under-Review</p>

<figure style="text-align:center;">
  <img src="{{ '/images/DOFA.png' | relative_url }}" alt="Fine-tuning DOFA" style="width:60%;">
  <figcaption style="font-size:14px;color:gray;">
    Figure: Schematic illustration of fine-tuning DOFA geo-foundational model for glacial lake mapping using Glacial Lake-Bench.
  </figcaption>
</figure>

<figure style="text-align:center;">
  <img src="{{ '/images/GLB.png' | relative_url }}" alt="GLB coverage" style="width:60%;">
  <figcaption style="font-size:14px;color:gray;">
    Figure: Compilation of Glacial Lake-Bench across RGI regions. GLB consists of Sentinel-1 (VV, VH), Sentinel-2 (Blue, Green, Red, NIR, SWIR-11, SWIR-12, NDWI), and topographic layers (slope, elevation). The map shows the ratio between total lake area reported by Zhang et al. (2024) and lake area covered by GLB.
  </figcaption>
</figure>

<figure style="text-align:center;">
  <img src="{{ '/images/GLB_random.png' | relative_url }}" alt="Split map" style="width:60%;">
  <figcaption style="font-size:14px;color:gray;">
    Figure: Spatial distribution of training, testing, and validation sites globally.
  </figcaption>
</figure>

<figure style="text-align:center;">
  <img src="{{ '/images/challenge1.png' | relative_url }}" alt="Challenging cases" style="width:60%;">
  <figcaption style="font-size:14px;color:gray;">
    Figure: Example DOFA results on the Glacial Lake-Challenge set: clouds, frozen lakes, shadows, and very small lakes (panel e).
  </figcaption>
</figure>
