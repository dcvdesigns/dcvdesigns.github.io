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

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;border:2px dashed #ef4444;padding:12px;background:#fff9f9;" id="portfolio-grid-test">
  {%- for item in items -%}
    <article style="border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 2px 8px rgba(0,0,0,.04)">
      {%- assign full = item.photos | first -%}
      {%- if full -%}
        <img
          src="{{ full | relative_url }}"
          alt="{{ item.title | escape }}"
          loading="lazy"
          decoding="async"
          width="800"
          height="800"
          style="display:block;width:100%;height:auto;aspect-ratio:1/1;object-fit:cover"
        >
      {%- else -%}
        <div style="aspect-ratio:1/1;display:grid;place-items:center;border-top:1px solid #e5e7eb;background:#f8fafc;color:#64748b;">No image</div>
      {%- endif -%}
      <div style="padding:12px 12px 14px">
        <h3 style="margin:.25rem 0 .35rem;font:600 16px/1.3 system-ui, -apple-system, Segoe UI, Roboto, sans-serif">
          <a href="{{ item.url | relative_url }}" style="text-decoration:none;color:#0f172a">{{ item.title }}</a>
        </h3>
        {%- if item.summary -%}
          <p style="margin:0;color:#64748b;font:400 14px/1.5 system-ui, -apple-system, Segoe UI, Roboto, sans-serif">{{ item.summary }}</p>
        {%- endif -%}
      </div>
    </article>
  {%- endfor -%}
</div>