---
title: Gallery
layout: page
permalink: /gallery/
---

{%- assign today = site.time | date: "%Y-%m-%d" -%}

{%- comment -%}
Make a safe items array even if _data/gallery.yml is missing.
{%- endcomment -%}
{%- assign items = site.data.gallery -%}
{%- if items == nil -%}
  {%- assign items = "" | split: "|" -%}
{%- endif -%}

{%- comment -%}
Sort newest first by publish_on (string or date); reverse for descending.
{%- endcomment -%}
{%- assign items = items | sort: "publish_on" | reverse -%}

<div class="card-grid gallery-grid">
  {%- for item in items -%}
    {%- comment -%}
    Normalize publish_on to a string date for safe comparison.
    If publish_on is blank/nil, show immediately.
    {%- endcomment -%}
    {%- assign pub = item.publish_on | date: "%Y-%m-%d" -%}
    {%- if item.publish_on == nil or item.publish_on == "" or pub <= today -%}
      <a class="card gallery-item" href="{{ item.image | relative_url }}" data-full="{{ item.image | relative_url }}" aria-label="Open image">
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

<!-- Lightbox modal -->
<div class="lightbox" id="lightbox" aria-hidden="true">
  <button class="lightbox-close" aria-label="Close">×</button>
  <img id="lightbox-img" alt="">
</div>

<script>
(function(){
  const lb = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  const closeBtn = lb.querySelector('.lightbox-close');

  function open(src){
    img.src = src;
    lb.classList.add('open');
    lb.setAttribute('aria-hidden','false');
  }
  function close(){
    lb.classList.remove('open');
    lb.setAttribute('aria-hidden','true');
    img.removeAttribute('src');
  }

  document.addEventListener('click', function(e){
    const a = e.target.closest('.gallery-item');
    if (a){
      e.preventDefault();
      open(a.getAttribute('data-full'));
    }
  });
  lb.addEventListener('click', function(e){
    if (e.target === lb) close();
  });
  closeBtn.addEventListener('click', close);
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') close();
  });
})();
</script>