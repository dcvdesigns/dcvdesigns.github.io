---
title: Home
layout: page
---
# Custom 3D Prints

Welcome to **DCV Designs**. Browse recent work below.

## Featured
<div class="card-grid">
  {% assign featured = site.portfolio | sort: 'date' | reverse | slice: 0, 6 %}
  {% for item in featured %}
  <article class="card">
    {% if item.photos and item.photos[0] %}
      <img src="{{ item.photos[0] }}" alt="{{ item.title }}">
    {% endif %}
    <div class="pad">
      <h3><a href="{{ item.url }}">{{ item.title }}</a></h3>
      <p>{{ item.summary }}</p>
    </div>
  </article>
  {% endfor %}
</div>