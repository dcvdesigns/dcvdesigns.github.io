

---
layout: default
title: Custom Orders
permalink: /custom-orders/
description: "How to request custom 3D‑printed designs from DCV Designs — from idea to finished product."
---

# Custom Orders

Some of our favorite projects begin with an idea from you. Whether it’s a personalized gift, a custom lightbox, a themed coaster set, or something entirely new, we’ll collaborate to bring it to life with clean design and high‑quality 3D printing.

## How It Works

1. **Inquire** – Tell us what you have in mind using the form below.
2. **Design & Quote** – We confirm feasibility, materials, colors, and timeline. You’ll receive a clear quote and a mockup or proof for approval.
3. **Approve & Produce** – Once approved, we 3D print your design and assemble as necessary.
4. **Delivery or Ship** – Local delivery in the St. Charles County, MO or shipping within the U.S.

> Typical turnaround is **1–2 weeks after design approval** for most items, often sooner — we’ll align on timing up front.

## Example Custom Projects

- Personalized lightboxes (logos, signage, etc.)
- Branded items for your small business
- Recognition plaques and nameplates
- Themed coaster sets and ornaments
- Neckerchief slides and small keepsakes

Looking for something else? Just ask — if it can be cleanly designed and printed in PLA, we’ll explore it with you.

---

## Start a Custom Design Request

Please share a few details so we can respond with an informed estimate. Fields marked with * are required. You should receive a response within 1-2 days.

<!-- Embedded Formspree form: tailored for custom orders -->
<form action="https://formspree.io/f/xeovjpwz" method="POST" class="custom-order-form" accept-charset="UTF-8">
  <!-- Identify the request path/type -->
  <input type="hidden" name="request_type" value="Custom Design Request">
  <input type="hidden" name="page" value="{{ page.url }}">

  <fieldset>
    <legend>Your Info</legend>
    <label for="name">Name *</label>
    <input id="name" name="name" type="text" required>

    <label for="email">Email *</label>
    <input id="email" name="email" type="email" required>

    <label for="phone">Phone (optional)</label>
    <input id="phone" name="phone" type="tel" inputmode="tel" placeholder="(###) ###‑####">
  </fieldset>

  <fieldset>
    <legend>Project Details</legend>

    <label for="project_title">Project Title (short) *</label>
    <input id="project_title" name="project_title" type="text" placeholder="e.g., Mizzou Columns Lightbox" required>

    <label for="project_type">Project Type *</label>
    <select id="project_type" name="project_type" required>
      <option value="">Select one…</option>
      <option>Lightbox</option>
      <option>Coasters</option>
      <option>Sliding Tile Puzzle</option>
      <option>Sign / Wall Art</option>
      <option>Key Hanger</option>
      <option>Other</option>
    </select>

    <label for="message">What are you envisioning? *</label>
    <textarea id="message" name="message" rows="6" placeholder="Tell us about the idea, intended use, audience, placement, etc." required></textarea>

    <label for="colors">Colors / Materials</label>
    <input id="colors" name="colors" type="text" placeholder="e.g., black + gold, white base, translucent front">

    <label for="dimensions">Approximate Size</label>
    <input id="dimensions" name="dimensions" type="text" placeholder="e.g., 7 in wide x 5 in tall x 1.5 in deep">

    <div class="inline-fields">
      <div>
        <label for="quantity">Quantity *</label>
        <input id="quantity" name="quantity" type="number" min="1" step="1" value="1" required>
      </div>
      <div>
        <label for="deadline">Target Date</label>
        <input id="deadline" name="deadline" type="date">
      </div>
    </div>

    <label for="budget">Budget Range (helps us propose options)</label>
    <select id="budget" name="budget">
      <option value="">Select a range…</option>
      <option>$25–$50</option>
      <option>$50–$100</option>
      <option>$100–$200</option>
      <option>$200+</option>
    </select>

    <label for="reference_url">Reference Link (optional)</label>
    <input id="reference_url" name="reference_url" type="url" placeholder="https://…">

    <!-- If you enable attachments on Formspree, you can uncomment the file field below
    <label for="reference_file">Attach a reference (JPG, PNG, PDF, SVG)</label>
    <input id="reference_file" name="attachment" type="file" accept=".jpg,.jpeg,.png,.pdf,.svg">
    -->
  </fieldset>

  <fieldset>
    <legend>Other Details</legend>
    <label for="how_hear">How did you hear about us?</label>
    <select id="how_hear" name="how_hear">
      <option value="">Select one…</option>
      <option>Friend / Family</option>
      <option>Social Media</option>
      <option>Craft Fair / Event</option>
      <option>Search / Web</option>
      <option>Other</option>
    </select>

    <!-- Simple antispam honeypot -->
    <label class="visually-hidden" for="company">Company (leave blank)</label>
    <input id="company" name="company" type="text" tabindex="-1" autocomplete="off">

    <label for="consent" class="checkbox">
      <input id="consent" name="consent" type="checkbox" required>
      I agree to be contacted about this request.
    </label>
  </fieldset>

  <button type="submit" class="btn primary">Submit Custom Request</button>
</form>

<style>
.custom-order-form { max-width: 720px; margin: 1rem auto 2rem; }
.custom-order-form fieldset { border: 1px solid #eee; padding: 1rem 1rem 1.25rem; margin: 0 0 1rem; border-radius: 8px; }
.custom-order-form legend { font-weight: 700; margin-bottom: .25rem; }
.custom-order-form label { display: block; font-weight: 600; margin-top: .75rem; }
.custom-order-form input[type="text"],
.custom-order-form input[type="email"],
.custom-order-form input[type="tel"],
.custom-order-form input[type="url"],
.custom-order-form input[type="date"],
.custom-order-form input[type="number"],
.custom-order-form select,
.custom-order-form textarea {
  width: 100%; padding: .6rem .7rem; border: 1px solid #d9d9d9; border-radius: 6px; font: inherit;
}
.custom-order-form .inline-fields { display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; }
.custom-order-form .checkbox { display: flex; align-items: center; gap: .5rem; margin-top: .75rem; font-weight: 500; }
.custom-order-form .visually-hidden { position: absolute; left: -9999px; }
.custom-order-form button.btn { margin-top: 1rem; }
@media (max-width: 640px){ .custom-order-form .inline-fields{ grid-template-columns: 1fr; } }
</style>

---

### FAQ

**What materials do you use?**  
We print models in high‑quality PLA in a wide range of colors. We can discuss specialty filaments (e.g., translucent, marble PLA) as appropriate. LED strips and other associated materials have been tested for reliability.

**Do you ship?**  
Yes — U.S. shipping available. Free local pickup or delivery in St. Charles County, MO.

**How do payments work?**  
For custom work, we typically take a **50% deposit at approval**, with the balance due prior to delivery/shipping.