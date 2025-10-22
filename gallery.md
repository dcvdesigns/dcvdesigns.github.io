---
title: Gallery
layout: page
permalink: /gallery/
---

{%- assign today = site.time | date: "%Y-%m-%d" -%}
{%- assign items = site.data.gallery | where_exp: "i", "i.publish_on == nil or i.publish_on <= today" -%}

<div class="card-grid gallery-grid">
  {%- comment -%}
  Show newest first by publish_on if present; otherwise keep order.
  {%- endcomment -%}
  {%- assign sorted = items | sort: "publish_on" | reverse -%}

  {%- for item in sorted -%}
    <a class="card gallery-item" href="{{ item.image | relative_url }}" data-full="{{ item.image | relative_url }}" aria-label="Open image">
      <div class="gallery-thumb">
        {% if item.category %}
          <span class="badge-cat">{{ item.category }}</span>
        {% endif %}
        <img src="{{ item.image | relative_url }}" alt="{{ item.alt | default: '' }}">
      </div>
    </a>
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