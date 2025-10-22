---
title: About
layout: page
permalink: /about/
---

<script>
(function(){
  // Respect user motion preference
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;

  // Helper: add initial hidden state
  function prime(nodes){ nodes.forEach(el => el.classList.add('reveal-init')); }

  // Helper: add stagger delays to children in a container
  function addStagger(containerSelector, itemSelector){
    document.querySelectorAll(containerSelector).forEach(container => {
      const kids = container.querySelectorAll(itemSelector);
      kids.forEach((el, i) => el.style.setProperty('--delay', (i * 60) + 'ms'));
    });
  }

  // Prime typical elements (expanded for About page copy)
  prime(document.querySelectorAll('.hero > *'));
  prime(document.querySelectorAll('.page h1'));
  prime(document.querySelectorAll('.page h2'));
  prime(document.querySelectorAll('.page p'));
  prime(document.querySelectorAll('.page ul li'));
  // Prime all direct children inside the main content area on pages (About)
  prime(document.querySelectorAll('.page .content > *'));

  prime(document.querySelectorAll('.announce'));
  prime(document.querySelectorAll('.project-image'));
  prime(document.querySelectorAll('.card-grid .card'));
  // About page CTA row buttons
  prime(document.querySelectorAll('.cta-row a'));

  // Add stagger to grids, CTA row, and About content blocks
  addStagger('.card-grid', '.card');
  addStagger('.cta-row', 'a');
  // Stagger direct children of the page content area (About)
  document.querySelectorAll('.page .content').forEach(section => {
    const kids = Array.from(section.children);
    kids.forEach((el, i) => el.style.setProperty('--delay', (i * 60) + 'ms'));
  });

  // Observe and reveal once
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting){
        entry.target.classList.add('reveal-in');
        entry.target.classList.remove('reveal-init');
        obs.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });

  document.querySelectorAll('.reveal-init').forEach(el => io.observe(el));
})();
</script>