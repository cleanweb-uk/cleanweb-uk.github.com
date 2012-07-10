---
layout: page
sharing: false
---

<div class="span9">
  {% assign index = true %}
  {% for post in site.posts %}
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