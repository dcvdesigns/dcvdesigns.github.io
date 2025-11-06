---
layout: page
class: home
---
<h1>DCV Designs - Modern 3D-printed decor and custom design</h1>
<br/>
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

<div class="carousel-wrap mock-glow">
<div class="scroll-strip" aria-label="Latest gallery images" tabindex="0">
  <div class="scroll-track">
  {%- assign added = 0 -%}
{%- assign limit = 24 -%}
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
</div>

<!-- found {{ entries | size }} manifest entries, showed {{ added }} -->

<div class="hero">
  <p>We design and print lightboxes, signage, coasters, and custom display pieces using clean multicolor workflows, polished finishes, and an eye for both aesthetic and function.</p>
  <p>Have an idea? We can bring it to life - click "Start a project" to reach out!</p>
  <div class="cta-row">
    <a class="btn primary" href="/contact/">Start a project</a>
    <a class="btn ghost" href="/portfolio/">See recent work</a>
  </div>
</div>
{% include announcement.html %}
## Featured Works ##
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
    const SPEED = window.matchMedia('(max-width: 640px)').matches ? 120 : 80; // faster on mobile
    // After duplication, half of track width corresponds to one full cycle
    const half = computeHalfWidth();
    const seconds = Math.max(6, Math.round(half / SPEED));
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