---
title: Portfolio
layout: page
permalink: /portfolio/
---

<!-- Filter -->
<div class="portfolio-filter">
  <label for="cat-filter" class="sr-only">Filter by category</label>

  {%- comment -%}
  Collect visible items (not future-dated) and derive categories.
  We always render the select; if no categories exist yet, you’ll still see "All categories".
  {%- endcomment -%}
  {%- assign visible = site.portfolio | where_exp: "i", "i.date <= site.time" -%}
  {%- assign cats = visible | map: "category" | uniq | sort -%}

  <select id="cat-filter">
    <option value="all">All categories</option>
    {%- for c in cats -%}
      {%- if c and c != "" -%}
        <option value="{{ c | downcase }}">{{ c }}</option>
      {%- endif -%}
    {%- endfor -%}
    {%- assign has_uncat = false -%}
    {%- for i in visible -%}
      {%- if i.category == nil or i.category == "" -%}
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
  {%- assign items = visible | sort: 'date' | reverse -%}
  {%- for item in items -%}
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

  // Restore selection from ?cat= query if present
  const params = new URLSearchParams(location.search);
  const qcat = (params.get('cat') || '').toLowerCase();
  if (qcat) {
    const opt = Array.from(sel.options).find(o => o.value.toLowerCase() === qcat);
    if (opt) sel.value = opt.value;
  }

  sel.addEventListener('change', () => {
    apply(sel.value);
    // Update URL (no reload)
    const p = new URLSearchParams(location.search);
    if (sel.value === 'all') { p.delete('cat'); }
    else { p.set('cat', sel.value); }
    const url = location.pathname + (p.toString() ? '?' + p.toString() : '');
    history.replaceState(null, '', url);
  });

  apply(sel.value);
})();
</script>