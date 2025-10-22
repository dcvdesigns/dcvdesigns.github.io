---
layout: page
class: home
---
<h1>DCV Designs - Modern 3D-printed decor and custom design</h1>
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

{%- comment -%} Latest 6 gallery images — horizontal strip {%- endcomment -%}
<div class="scroll-strip" aria-label="Latest gallery images">
  {% assign added = 0 %}
  {% assign limit = 6 %}
  {% assign gal = site.gallery | sort: 'date' | reverse %}
  {% for g in gal %}
    {% if g.photos and g.photos.size > 0 %}
      {% for p in g.photos %}
        {% if added < limit %}
          <a
            class="scroll-thumb gallery-item"
            href="{{ p | relative_url }}"
            data-full="{{ p | relative_url }}"
            data-alt="{{ g.title | escape }}"
            data-caption="{{ g.summary | escape }}"
            aria-label="Open image"
          >
            <img src="{{ p | relative_url }}" alt="{{ g.title | escape }}">
          </a>
          {% assign added = added | plus: 1 %}
        {% endif %}
      {% endfor %}
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