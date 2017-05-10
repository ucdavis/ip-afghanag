---
layout: pest
tags: pest
permalink: /pest-management/pomegranate
intro:
  - "Pest Management Manual (UCCE)"
  - "See Pest Identification Cards and general Pest Management Page"
---
<div id="main-boxes">
    {% for post in site.tags.pest-pomegranate %}
      <div class="main-box">
      <h2>{{post.title}}</h2>
        <a href="./files/{{ post.file-names }}.pdf">Fact Sheet</a>
          <img src="./media/{{post.file-names}}.jpeg">
        </a>
      </div>
    {% endfor %}
</div>


red mites missing
