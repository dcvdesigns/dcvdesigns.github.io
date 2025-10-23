---
title: Portfolio
layout: page
permalink: /portfolio/
---

{%- assign now_epoch = site.time | date: "%s" | plus: 0 -%}
{%- assign items_all = site.portfolio | default: site.collections['portfolio'].docs -%}
{%- assign items_all = items_all | sort: 'date' | reverse -%}

{%- comment -%} Filter {%- endcomment -%}
<div class="portfolio-filter">
  <label for="cat-filter" class="sr-only">Filter by category</label>

  {%- comment -%} Build a unique category list from visible (non-future) items {%- endcomment -%}
  {%- assign cat_string = "|" -%}
  <select id="cat-filter">
    <option value="all">All categories</option>
    {%- for i in items_all -%}
      {%- assign pub = i.publish_on | default: i.date -%}
      {%- assign pub_epoch = pub | date: "%s" | plus: 0 -%}
      {%- if pub_epoch == 0 -%}{% assign pub_epoch = now_epoch %}{% endif %}
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
      {%- assign pub_epoch = pub | date: "%s" | plus: 0 -%}
      {%- if pub_epoch == 0 -%}{% assign pub_epoch = now_epoch %}{% endif %}
      {%- if pub_epoch <= now_epoch and (i.category == nil or i.category == "") -%}
        {%- assign has_uncat = true -%}
      {%- endif -%}
    {%- endfor -%}
    {%- if has_uncat -%}
      <option value="uncategorized">Uncategorized</option>
    {%- endif -%}
  </select>
</div>

{%- comment -%} Temporary debug: show how many items pass the date filter {%- endcomment -%}
{%- assign visible = 0 -%}
{%- for item in items_all -%}
  {%- assign pub = item.publish_on | default: item.date -%}
  {%- assign pub_epoch = pub | date: "%s" | plus: 0 -%}
  {%- if pub_epoch == 0 -%}{%- assign pub_epoch = now_epoch -%}{%- endif -%}
  {%- if pub_epoch <= now_epoch -%}
    {%- assign visible = visible | plus: 1 -%}
  {%- endif -%}
{%- endfor -%}
<p class="debug-note" style="font:12px/1.4 monospace;color:#64748b;margin:.25rem 0 1rem;">Debug: {{ visible }} visible of {{ items_all | size }} total portfolio items.</p>

<ul class="debug-list" style="font:14px/1.5 system-ui;margin:.25rem 0 1rem;color:#334155;list-style:disc;padding-left:1.25rem;">
  {%- for i in items_all -%}
    {%- assign pub = i.publish_on | default: i.date -%}
    {%- assign pub_epoch = pub | date: "%s" | plus: 0 -%}
    {%- if pub_epoch == 0 -%}{% assign pub_epoch = now_epoch %}{% endif %}
    {%- if pub_epoch <= now_epoch -%}
      <li>{{ i.title }}</li>
    {%- endif -%}
  {%- endfor -%}
</ul>

{%- comment -%} Grid {%- endcomment -%}
<div class="card-grid" id="portfolio-grid">
  {%- for item in items_all -%}
    {%- assign pub = item.publish_on | default: item.date -%}
    {%- assign pub_epoch = pub | date: "%s" | plus: 0 -%}
    {%- if pub_epoch == 0 -%}{% assign pub_epoch = now_epoch %}{% endif %}
    {%- if pub_epoch <= now_epoch -%}
      {%- assign catval = item.category | default: 'Uncategorized' -%}
      <article class="card" data-category="{{ catval | downcase }}">
        {%- assign full = item.photos | first -%}
        {%- assign thumb = full | replace: '/assets/img/', '/assets/thumbs/' -%}
        {%- if full -%}
          <a
            class="gallery-item"
            href="{{ full | relative_url }}"
            data-full="{{ full | relative_url }}"
            data-alt="{{ item.title | escape }}"
            data-caption="{{ item.summary | escape }}"
            aria-label="Open image"
          >
            <img
              src="{{ thumb | relative_url }}"
              alt="{{ item.title | escape }}"
              loading="lazy"
              decoding="async"
              width="800"
              height="800"
            >
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