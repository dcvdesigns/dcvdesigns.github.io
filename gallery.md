---
title: Gallery
layout: page
permalink: /gallery/
---

{%- assign today = site.time | date: "%Y-%m-%d" -%}

<div class="card-grid gallery-grid">
  {%- comment -%}
  Loop through images defined in _data/gallery.yml
  and only show ones where:
  - publish_on is not set, OR
  - publish_on <= today
  {%- endcomment -%}
  {%- assign items = site.data.gallery | sort: "publish_on" | reverse -%}
  {%- for item in items -%}
    {%- if item.publish_on == nil or item.publish_on <= today -%}
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

  // Click any thumbnail to open
  document.addEventListener('click', function(e){
    const a = e.target.closest('.gallery-item');
    if (a){
      e.preventDefault();
      open(a.getAttribute('data-full'));
    }
  });

  // Close on backdrop click
  lb.addEventListener('click', function(e){
    if (e.target === lb) close();
  });

  closeBtn.addEventListener('click', close);

  // Escape key closes
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') close();
  });
})();
</script>