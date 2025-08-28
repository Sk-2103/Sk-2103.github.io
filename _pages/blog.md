---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---

{% include base_path %}

{% for post in site.posts reversed %}
<article>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="page__meta">{{ post.date | date: "%B %-d, %Y" }}</p>
  {{ post.content }}
  <hr />
</article>
{% endfor %}
