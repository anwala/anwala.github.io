---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
current_semester: "Fall 2024"
next_semester: "Spring 2025"
---
{% include base_path %}

<!--
## Next Semester ({{ page.next_semester }})

{% for post in site.teaching %}
  {% if post.semester == page.next_semester %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
-->

## Current Semester ({{ page.current_semester }})

{% for post in site.teaching %}
  {% if post.semester == page.current_semester %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Previous Semesters

* DATA [445-01](/teaching/2024-spring-data-445-01)/[641-01](/teaching/2024-spring-data-641-01) - Network Analysis (Spring 2024)
* DATA 440-02 - Web Science ([Fall 2023](/teaching/2023-fall-data-440-02))
* DATA 340-02 - Network Science ([Spring 2023](/teaching/2023-spring-data-340-02))
* DATA 440-03 - Web Science ([Fall 2022](/teaching/2022-fall-data-440-03))

### @ Old Dominion University

* CS 432/532 - Web Science ([Spring 2018](/teaching/2018-spring-cs-432-532)/[2019](/teaching/2019-spring-cs-432-532))
