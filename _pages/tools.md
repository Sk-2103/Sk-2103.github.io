---
layout: single
title: "Tools"
permalink: /tools/
author_profile: true
---

{% include base_path %}

{% for post in site.tools reversed %}
<article class="tool">
  <h2 id="{{ post.slug }}">{{ post.title }}</h2>
  {{ post.content }}
</article>
<hr />
{% endfor %}
