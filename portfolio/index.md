---
title: Portfolio
layout: page
permalink: /portfolio/
---

{%- assign items = site.portfolio | default: site.collections['portfolio'].docs -%}
{%- assign items = items | sort: 'date' | reverse -%}

<p class="debug-note" style="font:12px/1.4 monospace;color:#64748b;margin:.25rem 0 1rem;">
  (Temporary) Portfolio titles fallback below — grid rendered underneath.
</p>
<ul>
  {%- for item in items -%}
    <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
  {%- endfor -%}
</ul>

<div class="card-grid" id="portfolio-grid">
  {%- for item in items -%}
    <article class="card">
      {%- assign full = item.photos | first -%}
      {%- if full -%}
        <img
          src="{{ full | relative_url }}"
          alt="{{ item.title | escape }}"
          loading="lazy"
          decoding="async"
          width="800"
          height="800"
        >
      {%- else -%}
        <div style="aspect-ratio:1/1;display:grid;place-items:center;border:1px solid var(--color-border);background:#f8fafc;color:#64748b;">
          No image
        </div>
      {%- endif -%}
      <div class="pad">
        <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        {%- if item.summary -%}<p>{{ item.summary }}</p>{%- endif -%}
      </div>
    </article>
  {%- endfor -%}
</div>