---
title: Portfolio
layout: page
permalink: /portfolio/
---

{%- assign today = site.time | date: "%Y-%m-%d" -%}

<!-- Filter -->
<div class="portfolio-filter">
  <label for="cat-filter" class="sr-only">Filter by category</label>

  {%- comment -%} Build a unique category list from visible (non-future) items {%- endcomment -%}
  {%- assign cat_string = "|" -%}
  {%- assign items_all = site.portfolio | sort: 'date' | reverse -%}
  <select id="cat-filter">
    <option value="all">All categories</option>
    {%- for i in items_all -%}
      {%- assign pub = i.publish_on | default: i.date | date: "%Y-%m-%d" -%}
      {%- if pub <= today and i.category and i.category != "" -%}
        {%- assign needle = "|" | append: i.category | append: "|" -%}
        {%- unless cat_string contains needle -%}
          {%- assign cat_string = cat_string | append: i.category | append: "|" -%}
          <option value="{{ i.category | downcase }}">{{ i.category }}</option>
        {%- endunless -%}
      {%- endif -%}
    {%- endfor -%}
    {%- assign has_uncat = false -%}
    {%- for i in items_all -%}
      {%- assign pub = i.publish_on | default: i.date | date: "%Y-%m-%d" -%}
      {%- if pub <= today and (i.category == nil or i.category == "") -%}
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
    {%- assign pub = item.publish_on | default: item.date | date: "%Y-%m-%d" -%}
    {%- if pub <= today -%}
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

<!-- Lightbox modal (same structure as Gallery) -->
<div class="lightbox" id="lightbox" aria-hidden="true">
  <button class="lightbox-close" aria-label="Close">×</button>
  <div class="lightbox-inner">
    <img id="lightbox-img" alt="">
    <div class="lightbox-meta" id="lightbox-meta" hidden>
      <div class="lightbox-alt" id="lightbox-alt"></div>
      <div class="lightbox-caption" id="lightbox-caption"></div>
    </div>
  </div>
</div>

<script>
(function(){
  const lb = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  const meta = document.getElementById('lightbox-meta');
  const altEl = document.getElementById('lightbox-alt');
  const capEl = document.getElementById('lightbox-caption');
  const closeBtn = lb.querySelector('.lightbox-close');

  function open(src, altText, caption){
    img.src = src;
    img.alt = altText || '';
    const hasAlt = !!(altText && altText.trim().length);
    const hasCap = !!(caption && caption.trim().length);
    altEl.textContent = hasAlt ? altText : '';
    capEl.textContent = hasCap ? caption : '';
    meta.hidden = !(hasAlt || hasCap);
    lb.classList.add('open');
    lb.setAttribute('aria-hidden','false');
  }
  function close(){
    lb.classList.remove('open');
    lb.setAttribute('aria-hidden','true');
    img.removeAttribute('src');
    img.removeAttribute('alt');
    meta.hidden = true;
    altEl.textContent = '';
    capEl.textContent = '';
  }

  document.addEventListener('click', function(e){
    const a = e.target.closest('.gallery-item');
    if (a){
      e.preventDefault();
      open(
        a.getAttribute('data-full'),
        a.getAttribute('data-alt') || '',
        a.getAttribute('data-caption') || ''
      );
    }
  });

  lb.addEventListener('click', function(e){
    if (!e.target.closest('.lightbox-inner')) close();
  });
  closeBtn.addEventListener('click', close);
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') close();
  });
})();
</script>