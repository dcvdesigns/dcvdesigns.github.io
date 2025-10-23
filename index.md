/* Existing variables and other CSS above remain unchanged */

.scroll-strip{
  display:block;
  overflow:hidden;            /* hide scrollbar entirely */
  padding:.25rem 0 .75rem;    /* subtle breathing room */
  -ms-overflow-style: none;   /* IE/Edge legacy */
  scrollbar-width: none;      /* Firefox */
}
.scroll-strip::-webkit-scrollbar{ display:none; }

/* The moving track */
.scroll-track{
  display:flex;
  align-items:center;
  gap: .9rem;
  will-change: transform;
  animation: ticker var(--ticker-duration, 40s) linear infinite;
}
/* Pause when the container has .paused (hover/focus handled in JS) */
.scroll-strip.paused .scroll-track{ animation-play-state: paused; }

/* Slightly tighten thumb styling so long rows feel continuous */
.scroll-thumb img{ border-radius: 14px; display:block; }

@keyframes ticker{
  from{ transform: translateX(0); }
  to{   transform: translateX(-50%); }
}

---
layout: page
class: home
---
<h1>DCV Designs - Modern 3D-printed decor and custom design</h1>
{%- comment -%} Latest 6 images from _data/gallery.yml (robust) {%- endcomment -%}
{%- assign today = site.time | date: "%Y-%m-%d" -%}
{%- assign raw = site.data.gallery -%}
{%- assign entries = nil -%}
{%- if raw.images -%}
  {%- assign entries = raw.images -%}
{%- elsif raw.items -%}
  {%- assign entries = raw.items -%}
{%- else -%}
  {%- assign entries = raw -%}
{%- endif -%}
{%- if entries == nil -%}
  {%- assign entries = "" | split: "" -%}
{%- endif -%}
{%- assign manifest = entries | sort: 'publish_on' | reverse -%}
<div class="scroll-strip" aria-label="Latest gallery images" tabindex="0">
  <div class="scroll-track">
  {%- assign added = 0 -%}
{%- assign limit = 12 -%}
  {%- for g in manifest -%}
    {%- if added < limit -%}
      {%- assign file = g.file | default: g.path | default: g.image -%}
      {%- if file -%}
        {%- assign ext = file | split: '.' | last | downcase -%}
        {%- if file contains '/assets/img/' and (ext == 'jpg' or ext == 'jpeg' or ext == 'png' or ext == 'webp' or ext == 'gif') -%}
          {%- assign start = g.start | default: g.publish_on | default: g.date -%}
          {%- assign end   = g.end -%}
          {%- assign start_ok = true -%}
          {%- assign end_ok = true -%}
          {%- if start and start != '' -%}
            {%- assign sdate = start | date: "%Y-%m-%d" -%}
            {%- if sdate > today -%}{%- assign start_ok = false -%}{%- endif -%}
          {%- endif -%}
          {%- if end and end != '' -%}
            {%- assign edate = end | date: "%Y-%m-%d" -%}
            {%- if edate < today -%}{%- assign end_ok = false -%}{%- endif -%}
          {%- endif -%}
          {%- if start_ok and end_ok -%}
            <a
              class="scroll-thumb gallery-item"
              href="{{ file | relative_url }}"
              data-full="{{ file | relative_url }}"
              data-alt="{{ g.alt | default: '' | escape }}"
              data-caption="{{ g.caption | default: '' | escape }}"
              aria-label="Open image"
            >
              <img src="{{ file | relative_url }}" alt="{{ g.alt | default: '' | escape }}" loading="lazy" decoding="async" width="132" height="132">
            </a>
            {%- assign added = added | plus: 1 -%}
          {%- endif -%}
        {%- endif -%}
      {%- endif -%}
    {%- endif -%}
  {%- endfor -%}
  </div>
</div>
<!-- found {{ entries | size }} manifest entries, showed {{ added }} -->

<div class="hero">
  <p>I design and print lightboxes, signage, coasters, and custom display pieces using clean multicolor workflows, polished finishes, and an eye for both aesthetic and function. Have an idea? I can bring it to life - click "Start a project" to reach out!</p>
  <div class="cta-row">
    <a class="btn primary" href="/contact/">Start a project</a>
    <a class="btn ghost" href="/portfolio/">See recent work</a>
  </div>
</div>
{% include announcement.html %}
## Featured Works
<div class="card-grid">
  {%- assign today = site.time | date: "%Y-%m-%d" -%}
  {%- assign items = site.portfolio | sort: 'date' | reverse -%}
  {%- assign shown = 0 -%}
  {%- for item in items -%}
    {%- assign pub = item.publish_on | default: item.date | date: "%Y-%m-%d" -%}
    {%- if pub <= today and shown < 3 -%}
      <article class="card">
        {% if item.photos and item.photos[0] %}
          <a
            class="gallery-item"
            href="{{ item.photos[0] | relative_url }}"
            data-full="{{ item.photos[0] | relative_url }}"
            data-alt="{{ item.title | escape }}"
            data-caption="{{ item.summary | escape }}"
            aria-label="Open image"
          >
            <img src="{{ item.photos[0] | relative_url }}" alt="{{ item.title }}">
          </a>
        {% endif %}
        <div class="pad">
          <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
          <p>{{ item.summary }}</p>
        </div>
      </article>
      {% assign shown = shown | plus: 1 %}
    {% endif %}
  {% endfor %}
</div>

<p style="margin-top:1rem;">
  <a class="btn" href="{{ '/portfolio/' | relative_url }}">See all</a>
</p>

<!-- Lightbox modal (Home) -->
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

  function openLB(src, altText, caption){
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
  function closeLB(){
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
      openLB(
        a.getAttribute('data-full'),
        a.getAttribute('data-alt') || '',
        a.getAttribute('data-caption') || ''
      );
    }
  });

  lb.addEventListener('click', function(e){
    if (!e.target.closest('.lightbox-inner')) closeLB();
  });
  closeBtn.addEventListener('click', closeLB);
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') closeLB();
  });
})();
</script>
<script>
// Continuous ticker-style carousel using CSS animation
(function(){
  const strip = document.querySelector('.scroll-strip');
  if (!strip) return;
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return; // respect user preference

  const track = strip.querySelector('.scroll-track');
  if (!track) return;

  // Helper: compute half of the combined width after duplication
  function computeHalfWidth(){
    // total width after we duplicate will be 2x the original
    return track.scrollWidth / 2;
  }

  // Duplicate the children once so we have seamless loop
  const originalHTML = track.innerHTML;
  track.insertAdjacentHTML('beforeend', originalHTML);

  function setDuration(){
    // pixels per second — tune for feel
    const SPEED = 60; // slower = more calm, higher = faster
    // After duplication, half of track width corresponds to one full cycle
    const half = computeHalfWidth();
    const seconds = Math.max(10, Math.round(half / SPEED));
    track.style.setProperty('--ticker-duration', seconds + 's');
  }

  // Re-measure once first image loads (in case sizes were 0 at first paint)
  const firstImg = track.querySelector('img');
  if (firstImg && !firstImg.complete){
    firstImg.addEventListener('load', setDuration, { once: true });
  }
  // Also set after layout
  requestAnimationFrame(setDuration);
  window.addEventListener('resize', setDuration);

  // Pause on interaction, resume on leave/blur
  function pause(){ strip.classList.add('paused'); }
  function resume(){ strip.classList.remove('paused'); }
  ['mouseenter','focusin','pointerdown','touchstart'].forEach(evt => strip.addEventListener(evt, pause, { passive:true }));
  ['mouseleave','focusout','touchend','blur'].forEach(evt => strip.addEventListener(evt, resume, { passive:true }));
})();
</script>