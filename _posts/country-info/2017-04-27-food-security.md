---
layout: country-info
tags: country-info
permalink: /country-info/food-security
title:  "Food Security"
arabic: "مصونیت غذایی"
image: "/country-info/media/culture.jpeg"
pictures: /country-info/media/about.jpeg"
problem-opportunities:
  - "Priorities include wheat and other staple crops and postharvest and home storage."
  - "To improve food security, initiatives must help farmers produce enough food and teach them how to safely store food and how to generate additional income from surplus food."
  - "e-Afghan Ag is dedicated to improving food security in Afghanistan by providing information about:"
  - "<ul>"
  - "How to produce greater quantities of staple Afghan crops, like wheat."
  - "How to preserve food using simple postharvest technologies."
  - "How to develop markets to buy and sell products."
  - "How to increase food security by growing food at home in a kitchen garden."
  - "How to respond to weather events and environmental pressures, like drought, which can negatively affect food security."
  - "</ul>"
overview:
  - "In Afghanistan, over 7 million people--about 30% of the population--are food insecure (consuming less than 2,100 kcal/day).Of these 7 million, it is estimated that 2.1 million are very severely food insecure (consuming less than 1,500 kcal/day).
Food insecure people do not have enough safe, nutritious food to lead healthy and active lives and they live with constant concern for their next meal.  They have little interest in investing in the future because their immediate needs remain unmet.  They lack the energy to perform physical tasks are more prone to illness, making them generally less productive than others."
  - "Food and Food Security <a href='/country-info/files/IS_Afghan_Food_Food_Security.pdf'>Info Sheet</a> (UC Davis)"
  - "Food Security and Nutrition Assessment <a href='/country-info/files/ppt_nutri_assessment_english_ramsing.pdf'> English</a> and <a href='/country-info/files/ppt_nutri_assessment_dari_ramsing.pdf'> دری </a>(U Maryland)"
  - "See Food Frequency Info Sheet <a href='/country-info/files/is_nutri_food_frequency_eng_Ramsing.pdf'> English</a> and <a href='/country-info/files/is_nutri_food_frequency_dari_Ramsing.pdf'> دری </a>(U Maryland)"
  - "See Regional Analysis of Wheat Markets and Food Security in Central Asia  <a href='/country-info/files/rep-wheat-markets-food-security-afgh-central-asia-fewsnet.pdf'>Report</a> (2011) (FEWSNET)"
intro:
content-table:
management:
disease:
market-information-link: ""
photo-gallery: ""
links: ""
---
<div class="hing-content">
  <h2>Choose a Topic</h2>
  <div id="main-boxes">
      {% for post in site.tags.food-security %}
      <div class="main-box">
        <a href="{{post.permalink}}">
          <h2>{{post.title}}</h2>
          <h2>{{post.arabic}}</h2></a>
          <img src="{{post.image}}">
        </a>
      </div>
      {% endfor %}
  </div>
</div>
<div class="hing-content">
<h2>For More Information</h2>
  <ul>
    <a href="http://www.fews.net/central-asia/afghanistan"><li>Famine Early Warning Systems Network</li></a>
    <a href="http://www1.wfp.org/countries/afghanistan"><li>World Food Program - Afghanistan</li></a>
    <a href="http://foodsecuritycluster.net/countries/afghanistan"><li>FAO Food Security Cluster - Afghanistan</li></a>
  </ul>
</div>
