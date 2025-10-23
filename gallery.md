---
title: Gallery
layout: page
permalink: /gallery/
---

{%- assign today = site.time | date: "%Y-%m-%d" -%}

{%- comment -%} Safe items array even if _data/gallery.yml missing {%- endcomment -%}
{%- assign items = site.data.gallery -%}
{%- if items == nil -%}{%- assign items = "" | split: "|" -%}{%- endif -%}

{%- assign items = items | sort: "publish_on" | reverse -%}

<div class="card-grid gallery-grid">
  {%- for item in items -%}
    {%- assign pub = item.publish_on | date: "%Y-%m-%d" -%}
    {%- if item.publish_on == nil or item.publish_on == "" or pub <= today -%}
      <a
        class="card gallery-item"
        href="{{ item.image | relative_url }}"
        data-full="{{ item.image | relative_url }}"
        data-alt="{{ item.alt | escape }}"
        data-caption="{{ item.caption | escape }}"
        aria-label="Open image"
      >
        <div class="gallery-thumb">
          {% if item.category %}
            <span class="badge-cat">{{ item.category }}</span>
          {% endif %}
          <img src="{{ item.image | relative_url }}" alt="{{ item.alt | default: '' }}">
        </div>
      </a>
    {%- endif -%}
  {%- endfor -%}
</div>