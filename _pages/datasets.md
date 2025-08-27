---
layout: single
title: "Datasets"
permalink: /datasets/
author_profile: true
---

{% include base_path %}

{% for post in site.datasets reversed %}
<article class="dataset">
  <h2 id="{{ post.slug }}">{{ post.title }}</h2>
  {{ post.content }}
</article>
<hr />
{% endfor %}
