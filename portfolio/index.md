---
title: Portfolio
layout: page
permalink: /portfolio/
---

<!-- Filter -->
<div class="portfolio-filter">
  <label for="cat-filter" class="sr-only">Filter by category</label>

  {%- comment -%} Build a unique category list from visible (non-future) items {%- endcomment -%}
  {%- assign cat_string = "|" -%}
  {%- assign items_all = site.portfolio | sort: 'date' | reverse -%}
  <select id="cat-filter">
    <option value="all">All categories</option>
    {%- for i in items_all -%}
      {%- if i.date <= site.time and i.category and i.category != "" -%}
        {%- assign needle = "|" | append: i.category | append: "|" -%}
        {%- unless cat_string contains needle -%}
          {%- assign cat_string = cat_string | append: i.category | append: "|" -%}
          <option value="{{ i.category | downcase }}">{{ i.category }}</option>
        {%- endunless -%}
      {%- endif -%}
    {%- endfor -%}
    {%- assign has_uncat = false -%}
    {%- for i in items_all -%}
      {%- if i.date <= site.time and (i.category == nil or i.category == "") -%}
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
  {%- for item in items_all -%}
    {%- if item.date <= site.time -%}
      {%- assign catval = item.category | default: 'Uncategorized' -%}
      <article class="card" data-category="{{ catval | downcase }}">
        {%- if item.photos and item.photos[0] -%}
          <img src="{{ item.photos[0] | relative_url }}" alt="{{ item.title }}">
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

<script>
(function(){
  const sel = document.getElementById('cat-filter');
  const grid = document.getElementById('portfolio-grid');
  if (!sel || !grid) return;

  const cards = Array.from(grid.querySelectorAll('.card'));

  function apply(val){
    cards.forEach(card => {
      const cat = (card.getAttribute('data-category') || '').toLowerCase();
      const show = (val === 'all') || (cat === val);
      card.style.display = show ? '' : 'none';
    });
  }

  // Restore selection from ?cat=
  const params = new URLSearchParams(location.search);
  const qcat = (params.get('cat') || '').toLowerCase();
  if (qcat) {
    const opt = Array.from(sel.options).find(o => o.value.toLowerCase() === qcat);
    if (opt) sel.value = opt.value;
  }

  sel.addEventListener('change', () => {
    apply(sel.value);
    const p = new URLSearchParams(location.search);
    if (sel.value === 'all') { p.delete('cat'); }
    else { p.set('cat', sel.value); }
    history.replaceState(null, '', location.pathname + (p.toString() ? '?' + p.toString() : ''));
  });

  apply(sel.value);
})();
</script>