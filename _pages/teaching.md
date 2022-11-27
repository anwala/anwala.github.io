---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
current_semester: "Fall 2022"
---
{% include base_path %}

## {{ page.current_semester }}

{% for post in site.teaching %}
  {% if post.semester_code == page.current_semester_code %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Previous Semesters

## @ Old Dominion University

* CS 432/532 - Web Science ([Spring 2018](/teaching/2018-spring-cs-432-532)/[2019](/teaching/2019-spring-cs-432-532))
