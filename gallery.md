---
title: Gallery
layout: page
permalink: /gallery/
---

<div class="card-grid gallery-grid">
  {%- comment -%}
  Gather all static files under /assets/img/ and filter to common image extensions.
  {%- endcomment -%}
  {%- assign all_imgs = site.static_files | where_exp: "f", "f.path contains '/assets/img/'" -%}
  {%- assign jpgs  = all_imgs | where: "extname", ".jpg"  | concat: (all_imgs | where: "extname", ".jpeg") -%}
  {%- assign pngs  = all_imgs | where: "extname", ".png"  -%}
  {%- assign gifs  = all_imgs | where: "extname", ".gif"  -%}
  {%- assign webps = all_imgs | where: "extname", ".webp" -%}
  {%- assign avifs = all_imgs | where: "extname", ".avif" -%}
  {%- assign imgs  = jpgs | concat: pngs | concat: gifs | concat: webps | concat: avifs -%}

  {%- for file in imgs -%}
    <a class="card gallery-item" href="{{ file.path | relative_url }}" data-full="{{ file.path | relative_url }}" aria-label="Open image">
      <img src="{{ file.path | relative_url }}" alt="">
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