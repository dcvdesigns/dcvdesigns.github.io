---
title: Contact
layout: page
permalink: /contact/
---

<p>Tell me a bit about what you need. I’ll get back to you shortly.</p>

<form action="https://formspree.io/f/xeorwvyp" method="POST" class="contact-form" novalidate>
  <!-- Name -->
  <label for="name">Name *</label>
  <input id="name" name="name" type="text" required autocomplete="name" placeholder="Your name">

  <!-- Email -->
  <label for="email">Email *</label>
  <input id="email" name="email" type="email" required autocomplete="email" placeholder="you@example.com">

  <!-- Request type -->
  <label for="request_type">Request type *</label>
  <select id="request_type" name="request_type" required>
    <option value="" selected disabled>Select one</option>
    <option>Custom Design Request</option>
    <option>Order Items</option>
    <option>General Question</option>
    <option>Wholesale / Bulk Order</option>
    <option>Collaboration / Partnership</option>
  </select>

  <!-- Message -->
  <label for="message">Message *</label>
  <textarea id="message" name="message" required placeholder="Describe what you’re looking for — style, purpose, timeline, etc."></textarea>

  <!-- Hidden fields -->
  <input type="hidden" name="_subject" value="New inquiry from dcvdesigns.com">
  <input type="hidden" name="_next" value="/thanks/">

  <!-- Spam honeypot -->
  <label style="display:none">Leave this field empty
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off">
  </label>

  <button type="submit" class="btn primary">Send</button>
</form>
<script>
(function () {
  const params = new URLSearchParams(window.location.search);

  // Prefill Request Type (matches by value or visible text)
  const typeParam = params.get('request_type');
  const selectEl = document.getElementById('request_type');
  if (typeParam && selectEl) {
    const typeLower = typeParam.toLowerCase();
    const match = Array.from(selectEl.options).find(opt =>
      (opt.value && opt.value.toLowerCase() === typeLower) ||
      (opt.text && opt.text.toLowerCase() === typeLower)
    );
    if (match) {
      selectEl.value = match.value || match.text;
    }
  }

  // Prefill Message
  const msgParam = params.get('message');
  const msgEl = document.getElementById('message');
  if (msgParam && msgEl) {
    msgEl.value = msgParam;
  }

  // Optional: Prefill Name and Email if provided
  const nameParam = params.get('name');
  const nameEl = document.getElementById('name');
  if (nameParam && nameEl) {
    nameEl.value = nameParam;
  }

  const emailParam = params.get('email');
  const emailEl = document.getElementById('email');
  if (emailParam && emailEl) {
    emailEl.value = emailParam;
  }
})();
</script>