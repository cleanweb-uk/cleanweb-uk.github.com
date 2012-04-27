---
layout: page
title: "Podcast"
comments: false
sharing: true
footer: true
---

The Cleanweb UK Podcast is a regular tour of current cleanweb affairs, presented by 
[@mrchrisadams](http://twitter.com/mrchrisadams) and [@floppy](http://twitter.com/floppy). 
With interviews, discussion, links, and more, we'll keep you up to date with what's going on. 

Click the episodes below to listen, leave feedback, or see links to everything we talked about.

<div id="blog-archives">
{% for post in site.categories.podcast reverse %}
{% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
{% unless year == this_year %}
  {% assign year = this_year %}
  <h2>{{ year }}</h2>
{% endunless %}
<article>
  {% capture category %}{{ post.categories | size }}{% endcapture %}
  <h1><a href="{{ root_url }}{{ post.url }}">{{post.title}}</a></h1>
  <time datetime="{{ post.date | datetime | date_to_xmlschema }}" pubdate>{{ post.date | date: "<span class='month'>%b</span> <span class='day'>%d</span> <span class='year'>%Y</span>"}}</time>
</article>
{% endfor %}
</div>