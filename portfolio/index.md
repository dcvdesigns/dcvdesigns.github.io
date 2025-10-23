---
title: Portfolio
layout: page
permalink: /portfolio/
---

{%- assign now_epoch = site.time | date: "%s" -%}

<!-- Filter -->
<div class="portfolio-filter">
  <label for="cat-filter" class="sr-only">Filter by category</label>

  {%- comment -%} Build a unique category list from visible (non-future) items {%- endcomment -%}
  {%- assign cat_string = "|" -%}
  {%- assign items_all = site.portfolio | sort: 'date' | reverse -%}
  <select id="cat-filter">
    <option value="all">All categories</option>
    {%- for i in items_all -%}
      {%- assign pub = i.publish_on | default: i.date -%}
      {%- assign pub_epoch = pub | date: "%s" -%}
      {%- if pub_epoch <= now_epoch and i.category and i.category != "" -%}
        {%- assign needle = "|" | append: i.category | append: "|" -%}
        {%- unless cat_string contains needle -%}
          {%- assign cat_string = cat_string | append: i.category | append: "|" -%}
          <option value="{{ i.category | downcase }}">{{ i.category }}</option>
        {%- endunless -%}
      {%- endif -%}
    {%- endfor -%}
    {%- assign has_uncat = false -%}
    {%- for i in items_all -%}
      {%- assign pub = i.publish_on | default: i.date -%}
      {%- assign pub_epoch = pub | date: "%s" -%}
      {%- if pub_epoch <= now_epoch and (i.category == nil or i.category == "") -%}
        {%- assign has_uncat = true -%}
      {%- endif -%}
    {%- endfor -%}
    {%- if has_uncat -%}
      <option value="uncategorized">Uncategorized</option>
    {%- endif -%}
  </select>
</div>

<!-- Grid -->
<div class="card-grid" id="portfolio-grid">
  {%- assign items_all = site.portfolio | sort: 'date' | reverse -%}
  {%- for item in items_all -%}
    {%- assign pub = item.publish_on | default: item.date -%}
    {%- assign pub_epoch = pub | date: "%s" -%}
    {%- if pub_epoch <= now_epoch -%}
      {%- assign catval = item.category | default: 'Uncategorized' -%}
      <article class="card" data-category="{{ catval | downcase }}">
        {%- assign thumb = item.photos | first -%}
        {%- if thumb -%}
          <a
            class="gallery-item"
            href="{{ thumb | relative_url }}"
            data-full="{{ thumb | relative_url }}"
            data-alt="{{ item.title | escape }}"
            data-caption="{{ item.summary | escape }}"
            aria-label="Open image"
          >
            <img src="{{ thumb | relative_url }}" alt="{{ item.title }}">
          </a>
        {%- endif -%}
        <div class="pad">
          <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
          <p>{{ item.summary }}</p>
          {%- if item.category -%}
            <p class="mini-cat"><span class="tag">{{ item.category }}</span></p>
          {%- endif -%}
        </div>
      </article>
    {%- endif -%}
  {%- endfor -%}
</div>