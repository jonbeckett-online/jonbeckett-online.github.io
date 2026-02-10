---
title: "Category Archives"
layout: single
permalink: /categories/
---

{% assign categories = site.categories | sort %}

<h1>All Categories</h1>

{% if categories.size > 0 %}
{% for category in categories %}
  {% assign category_name = category[0] %}
  {% assign posts = category[1] %}
  
<h2 id="{{ category_name | slugify }}"><a href="#{{ category_name | slugify }}">{{ category_name }}</a> ({{ posts.size }} posts)</h2>
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

<p>No categories found. Categories will appear here as you add them to your posts.</p>

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