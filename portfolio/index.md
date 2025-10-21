---
title: Portfolio
layout: page
permalink: /portfolio/
---
Explore recent 3D-printed builds — illuminated decor, signage, and one-of-a-kind custom commissions.

<div class="card-grid">
  {% assign items = site.portfolio | sort: 'date' | reverse %}
  {% for item in items %}
    <article class="card">
      {% if item.photos and item.photos[0] %}
        <img src="{{ item.photos[0] | relative_url }}" alt="{{ item.title }}">
      {% endif %}
      <div class="pad">
        <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        <p>{{ item.summary }}</p>
      </div>
    </article>
  {% endfor %}
</div>