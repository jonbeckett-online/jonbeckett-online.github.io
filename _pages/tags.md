---
title: "Tag Archives"
layout: single
permalink: /tags/
---

{% assign tags = site.tags | sort %}

<h1>All Tags</h1>

{% if tags.size > 0 %}
{% for tag in tags %}
  {% assign tag_name = tag[0] %}
  {% assign posts = tag[1] %}
  
<h2 id="{{ tag_name | slugify }}"><a href="#{{ tag_name | slugify }}">{{ tag_name }}</a> ({{ posts.size }} posts)</h2>
<ul>
{% for post in posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="post-meta"> - {{ post.date | date: "%B %d, %Y" }}</span>
  </li>
{% endfor %}
</ul>

{% endfor %}

{% else %}

<p>No tags found. Tags will appear here as you add them to your posts.</p>

{% endif %}

<style>
.post-meta {
  color: #666;
  font-size: 0.9em;
}

h2 {
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: #2c3e50;
}

h2 a {
  text-decoration: none;
  color: #2c3e50;
}

h2 a:hover {
  text-decoration: underline;
}

ul {
  margin-bottom: 2rem;
}

li {
  margin-bottom: 0.5rem;
}
</style>

<style>
.post-meta {
  color: #666;
  font-size: 0.9em;
}

h2 {
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: #2c3e50;
}

ul {
  margin-bottom: 2rem;
}

li {
  margin-bottom: 0.5rem;
}
</style>