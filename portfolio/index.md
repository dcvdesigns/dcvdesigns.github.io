---
title: Portfolio
layout: page
permalink: /portfolio/
---

{%- assign today_epoch = site.time | date: '%s' | plus: 0 -%}
{%- assign items = site.portfolio | default: site.collections['portfolio'].docs -%}
{%- assign items = items | where_exp: 'i', "i.publish_on == nil or i.publish_on == '' or (i.publish_on | date: '%s' | plus: 0) <= today_epoch" -%}
{%- assign items = items | sort: 'date' | reverse -%}

<!-- Category filter -->
{%- assign cats = items | map: 'category' | compact | uniq | sort -%}
<div id="portfolio-filter" style="display:flex;align-items:center;gap:.5rem;margin:4px 0 12px;">
  <label for="catFilter" style="font:600 14px/1.2 system-ui, -apple-system, Segoe UI, Roboto, sans-serif;color:#0f172a;">Category:</label>
  <select id="catFilter" style="padding:.45rem .6rem;border:1px solid #e5e7eb;border-radius:10px;background:#fff;">
    <option value="all">All</option>
    {%- for c in cats -%}
      <option value="{{ c | downcase }}">{{ c }}</option>
    {%- endfor -%}
  </select>
</div>

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;padding:4px 0;" id="portfolio-grid-test">
  {%- for item in items -%}
    <article data-category="{{ item.category | default: 'Uncategorized' | downcase }}" style="border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 2px 8px rgba(0,0,0,.04)">
      {%- assign full = item.photos | first -%}
      {%- if full -%}
        <a href="{{ item.url | relative_url }}" style="display:block;">
          <img
            src="{{ full | relative_url }}"
            alt="{{ item.title | escape }}"
            loading="lazy"
            decoding="async"
            width="800"
            height="800"
            style="display:block;width:100%;height:auto;aspect-ratio:1/1;object-fit:cover"
          >
        </a>
      {%- else -%}
        <a href="{{ item.url | relative_url }}" style="display:block;text-decoration:none;color:inherit;">
          <div style="aspect-ratio:1/1;display:grid;place-items:center;border-top:1px solid #e5e7eb;background:#f8fafc;color:#64748b;">No image</div>
        </a>
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
<script>
(function(){
  var select = document.getElementById('catFilter');
  var grid = document.getElementById('portfolio-grid-test');
  if(!select || !grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('article'));

  function applyFilter(val){
    var v = (val||'all').toLowerCase();
    cards.forEach(function(card){
      var c = (card.getAttribute('data-category')||'uncategorized').toLowerCase();
      var show = (v === 'all') || (c === v);
      card.style.display = show ? '' : 'none';
    });
  }

  // Read from query (?category=Holiday)
  try {
    var p = new URLSearchParams(window.location.search);
    var q = p.get('category');
    if(q){
      var opt = Array.prototype.find.call(select.options, function(o){ return o.value === q.toLowerCase(); });
      if(opt) select.value = q.toLowerCase();
    }
  } catch(e){}

  applyFilter(select.value);
  select.addEventListener('change', function(){ applyFilter(this.value); });
})();
</script>