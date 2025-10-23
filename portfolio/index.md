---
title: Portfolio
layout: page
permalink: /portfolio/
---

{%- assign items = site.portfolio | default: site.collections['portfolio'].docs -%}
{%- assign items = items | sort: 'date' | reverse -%}

<div class="card-grid" id="portfolio-grid">
  {%- for item in items -%}
    <article class="card">
      {%- assign full = item.photos | first -%}
      {%- if full -%}
        {%- assign thumb = full | replace: '/assets/img/', '/assets/thumbs/' -%}
        <a class="gallery-item"
           href="{{ full | relative_url }}"
           data-full="{{ full | relative_url }}"
           data-alt="{{ item.title | escape }}"
           data-caption="{{ item.summary | default: '' | escape }}"
           aria-label="Open image">
          <img
            src="{{ thumb | relative_url }}"
            alt="{{ item.title | escape }}"
            loading="lazy"
            decoding="async"
            width="800"
            height="800"
            onerror="this.onerror=null;this.src='{{ full | relative_url }}'"
          >
        </a>
      {%- endif -%}
      <div class="pad">
        <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        {%- if item.summary -%}<p>{{ item.summary }}</p>{%- endif -%}
      </div>
    </article>
  {%- endfor -%}
</div>