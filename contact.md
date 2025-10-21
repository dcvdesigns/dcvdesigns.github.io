---
title: Contact
layout: page
---
Email me at <mailto:dcvdesigns@gmail.com> or use the form below.

<form action="https://formspree.io/f/xeorwvyp" method="POST" class="contact-form">
  <label>Your email
    <input type="email" name="email" required>
  </label>

  <label>Message
    <textarea name="message" required></textarea>
  </label>

  <input type="hidden" name="_subject" value="New contact from DCV Designs">

  <!-- Spam honeypot -->
  <label style="display:none">Leave this field empty
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off">
  </label>

  <!-- Redirect after success -->
  <input type="hidden" name="_next" value="/thanks/">

  <button type="submit" class="btn primary">Send</button>
</form>