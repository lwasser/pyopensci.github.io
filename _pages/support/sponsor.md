---
layout: splash
classes: flowing
title: "Support pyOpenSci's Mission"
author_profile: false
published: true
site-map: true
permalink: /support/sponsor.html
header:
  overlay_image: images/headers/pyopensci-learn-header.png
  overlay_filter: 0.3
---

<div class="pyos-section" markdown="1">
<div class="content padding" markdown="1">

## Support Us

Support pyOpenSci's mission to break down social and technical barriers to open science and broaden participation in scientific open source through corporate sponsorship.

</div>
</div>

<div class="pyos-section purple" markdown="1">
<div class="content padding" markdown="1">

## Why Sponsor pyOpenSci

Your corporate sponsorship directly supports our mission to make scientific open source more accessible and inclusive. When you sponsor pyOpenSci, you help us:

* **Expand our peer review program** to support more scientific Python packages, ensuring higher quality software for the research community
* **Develop accessible training resources** and educational content that lower barriers to entry for scientists learning Python packaging
* **Support scholarships** for our training events, making professional development opportunities available to underrepresented groups
* **Maintain and grow our community infrastructure** that connects thousands of scientists, developers, and researchers worldwide

By sponsoring pyOpenSci, you're investing in the future of open science and helping build a more diverse, inclusive scientific software ecosystem.

</div>
</div>

{% include div_purple_bottom.html  %}

<div class="pyos-section" markdown="1">
<div class="content padding" markdown="1">

## Interested in Sponsoring?

We're actively seeking corporate sponsors who share our commitment to open science and scientific software quality. Sponsorship opportunities are available at various levels to fit your organization's goals and budget.

If you're interested in learning more about sponsorship opportunities, benefits, and how your organization can support pyOpenSci, please reach out to us at [admin@pyopensci.org](mailto:admin@pyopensci.org).

</div>
</div>

{% if site.data.sponsors.size > 0 %}
{% include div_purple_top.html  %}

<div class="pyos-section purple" markdown="1">
<div class="content padding" markdown="1">

## Current Sponsors

We're grateful to our sponsors who help make pyOpenSci's work possible:

<div class="sponsors-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2em; margin-top: 2em;">
{% for sponsor in site.data.sponsors %}
  <div class="sponsor-item" style="text-align: center;">
    {% if sponsor.logo %}
      {% if sponsor.url %}
        <a href="{{ sponsor.url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ sponsor.logo }}" alt="{{ sponsor.name }}" style="max-width: 200px; max-height: 100px; object-fit: contain;">
        </a>
      {% else %}
        <img src="{{ sponsor.logo }}" alt="{{ sponsor.name }}" style="max-width: 200px; max-height: 100px; object-fit: contain;">
      {% endif %}
    {% endif %}
    {% if sponsor.url %}
      <h3 style="margin-top: 1em;"><a href="{{ sponsor.url }}" target="_blank" rel="noopener noreferrer">{{ sponsor.name }}</a></h3>
    {% else %}
      <h3 style="margin-top: 1em;">{{ sponsor.name }}</h3>
    {% endif %}
    {% if sponsor.date_joined %}
      <p style="font-size: 0.9em; color: #666;">Sponsor since {{ sponsor.date_joined }}</p>
    {% endif %}
  </div>
{% endfor %}
</div>

</div>
</div>

{% include div_purple_bottom.html  %}
{% endif %}

<div class="pyos-section purple" markdown="1">
<div class="content padding" markdown="1">

## Other Ways to Support pyOpenSci

* [Volunteer with us](/volunteer.html) - Contribute your time and expertise
* [Become a member](/support/membership.html) - Join our membership program
* [Donate](https://fnd.us/pyopensci_2024) - Make a one-time or recurring donation

</div>
</div>
