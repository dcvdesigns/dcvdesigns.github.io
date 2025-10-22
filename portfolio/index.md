---
title: Portfolio
layout: page
permalink: /portfolio/
---

<label for="cat-filter" class="sr-only">Filter by category</label>
<div class="portfolio-filter">
  {% assign visible = site.portfolio
      | where_exp: "i", "i.date <= site.time" %}
  {% assign cats = visible | map: "category" | uniq | sort %}
  <select id="cat-filter">
    <option value="all">All categories</option>
    {% for c in cats %}
      {% if c %}
        <option value="{{ c | downcase }}">{{ c }}</option>
      {% endif %}
    {% endfor %}
    {% if cats contains nil %}
      <option value="uncategorized">Uncategorized</option>
    {% endif %}
  </select>
</div>

<div class="card-grid" id="portfolio-grid">
  {% assign items = visible | sort: 'date' | reverse %}
  {% for item in items %}
    {% assign catval = item.category | default: 'Uncategorized' %}
    <article class="card" data-category="{{ catval | downcase }}">
      {% if item.photos and item.photos[0] %}
        <img src="{{ item.photos[0] | relative_url }}" alt="{{ item.title }}">
      {% endif %}
      <div class="pad">
        <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        <p>{{ item.summary }}</p>
        {% if item.category %}
          <p class="mini-cat"><span class="tag">{{ item.category }}</span></p>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>

<script>
(function(){
  const sel = document.getElementById('cat-filter');
  const cards = Array.from(document.querySelectorAll('#portfolio-grid .card'));
  if (!sel || !cards.length) return;

  function apply(){
    const val = sel.value;
    cards.forEach(card => {
      const cat = (card.getAttribute('data-category') || '').toLowerCase();
      const show = (val === 'all') || (cat === val);
      card.style.display = show ? '' : 'none';
    });
  }
  sel.addEventListener('change', apply);
  apply(); // initial
})();
</script>