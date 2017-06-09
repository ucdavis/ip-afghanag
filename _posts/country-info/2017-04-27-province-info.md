---
layout: country-info
tags: country-info
permalink: /country-info/province-info
title:  "Province Information"
arabic: "معلومات ولایتی"
image: "/country-info/media/map.jpeg"
pictures: /country-info/media/maps.jpg"
problem-opportunities:
overview:
- "Afghanistan is divided into thirty-four provinces, each of which are further divided into districts.  Use the links below for more information about the provinces of Afghanistan."
- "Map of Afghan Administrative Divisions, Province and District Level PDF Map (2.47 MB) (MAIL and AIMS)"
- "Select a province from the list below for more information or use the Interactive Map"
intro:
content-table:
management:
disease:
market-information-link: ""
photo-gallery: ""
links: ""
---
<div class="hing-content">
  <h2>Provinces</h2>
  {% for post in site.tags.province %}
    <a href="{{post.permalink}}">
      <p>{{post.title}}</p>
    </a>
  {% endfor %}
</div>
<div class="hing-content">
  <h2>Socio-Economic and Demographic Profile Reports by Province</h2>
  <b>(2003-2005) (UNFPA)</b>
  {% for post in site.tags.province %}
    <a href="{{post.permalink}}">
      <p>{{post.title}}</p>
    </a>
  {% endfor %}
</div>
