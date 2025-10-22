---
title: Gallery
layout: page
permalink: /gallery/
---

{%- assign today = site.time | date: "%Y-%m-%d" -%}

{%- comment -%} Safe items array even if _data/gallery.yml missing {%- endcomment -%}
{%- assign items = site.data.gallery -%}
{%- if items == nil -%}{%- assign items = "" | split: "|" -%}{%- endif -%}

{%- assign items = items | sort: "publish_on" | reverse -%}

<div class="card-grid gallery-grid">
  {%- for item in items -%}
    {%- assign pub = item.publish_on | date: "%Y-%m-%d" -%}
    {%- if item.publish_on == nil or item.publish_on == "" or pub <= today -%}
      <a
        class="card gallery-item"
        href="{{ item.image | relative_url }}"
        data-full="{{ item.image | relative_url }}"
        data-alt="{{ item.alt | escape }}"
        data-caption="{{ item.caption | escape }}"
        aria-label="Open image"
      >
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

  <!-- Keep meta constrained to image width by wrapping both inside .lightbox-inner -->
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
  const inner = lb.querySelector('.lightbox-inner');
  const img = document.getElementById('lightbox-img');
  const meta = document.getElementById('lightbox-meta');
  const altEl = document.getElementById('lightbox-alt');
  const capEl = document.getElementById('lightbox-caption');
  const closeBtn = lb.querySelector('.lightbox-close');

  function open(src, altText, caption){
    img.src = src;
    img.alt = altText || '';
    // populate meta
    const hasAlt = !!(altText && altText.trim().length);
    const hasCap = !!(caption && caption.trim().length);
    if (hasAlt){ altEl.textContent = altText; } else { altEl.textContent = ''; }
    if (hasCap){ capEl.textContent = caption; } else { capEl.textContent = ''; }
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

  // Open on thumbnail click
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

  // Close on backdrop click
  lb.addEventListener('click', function(e){
    if (e.target === lb) close();
  });
  closeBtn.addEventListener('click', close);
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') close();
  });
})();
</script>