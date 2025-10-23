---
title: Portfolio
layout: page
permalink: /portfolio/
---

{%- assign items = site.portfolio | default: site.collections['portfolio'].docs -%}
{%- assign items = items | sort: 'date' | reverse -%}

<ul>
  {%- for item in items -%}
    <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
  {%- endfor -%}
</ul>