---
layout: default
sharing: false
---

<div class="span9">
  
  <div class='hero-unit'>
    <h1>{{site.title}}</h1>
    <h2>{{site.subtitle}}</h2>
  </div>
  
  {% assign index = true %}
  {% for post in site.posts limit:1 %}
  {% assign content = post.content %}
    <article>
      {% include article.html %}
    </article>
  {% endfor %}
  <ul class="pager">
    {% if paginator.next_page %}
    <li class="previous"><a href="{{paginator.next_page}}">&larr; Older</a></li>
    {% endif %}
    <li><a href="/blog/archives">Blog Archives</a></li>
    {% if paginator.previous_page %}
    <li class="next"><a href="{{paginator.previous_page}}">Newer &rarr;</a></li>
    {% endif %}
  </ul>
</div>
<div class="sidebar-nav span3">
  {% if site.blog_index_asides.size %}
    {% include_array blog_index_asides %}
  {% else %}
    {% include_array default_asides %}
  {% endif %}
</div>