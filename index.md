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
  {% assign featured = site.portfolio
      | where_exp: "i", "i.date <= site.time"
      | sort: "date" | reverse | slice: 0, 3 %}
  {% for item in featured %}
    <article class="card">
      {% if item.photos and item.photos[0] %}
        <img src="{{ item.photos[0] | relative_url }}" alt="{{ item.title }}">
      {% endif %}
      <div class="pad">
        <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        <p>{{ item.summary }}</p>
      </div>
    </article>
  {% endfor %}
</div>
<p style="margin-top:1rem;">
  <a class="btn" href="/portfolio/">See all</a>
</p>