---
layout: home
title: Home
---

# Advanced Python Programming

Welcome to this advanced programming course focusing on Python, development tools, and modern software practices.
[Access the git repository](https://github.com/KnuxV/advanced_programming_python)

## Course Overview

This course explores essential programming tools and concepts that will enhance your development workflow and prepare you for professional software development.

### Quick Polls
Help shape the course by participating in these anonymous polls:
{% for poll in site.data.navigation.course.polls %}
- {{ poll.icon }} [{{ poll.title }}]({{ poll.url }})
{% endfor %}

---

{% for class in site.data.navigation.classes %}
## Class {{ class.number }}: {{ class.title }} {#{{ class.id }}}

{% if class.lessons %}
### Lessons
{% for lesson in class.lessons %}
{{ forloop.index }}. [{{ lesson.title }}]({{ lesson.path | relative_url }}){% if lesson.description %} - {{ lesson.description }}{% endif %}
{% endfor %}
{% endif %}

{% if class.code_examples %}
### Code Examples
{% for example in class.code_examples %}
- [{{ example.title }}]({{ example.path | relative_url }}){% if example.description %} - {{ example.description }}{% endif %}
{% endfor %}
{% endif %}

{% if class.exercises %}
### Exercises
{% for exercise in class.exercises %}
- [{{ exercise.title }}]({{ exercise.path | relative_url }}){% if exercise.description %} - {{ exercise.description }}{% endif %}
{% endfor %}
{% endif %}

---

{% endfor %}

## Contributing to the Course {#contributing}

### Earn Bonus Points! 🌟
Contribute to our course materials and earn 0.5-1 bonus points on your final grade.

**Ways to Contribute:**
- Submit exercise solutions
- Add helpful resources or tutorials
- Fix bugs or typos
- Improve documentation
- Translate content

**How to Submit:**
1. Fork the [course repository](https://github.com/KnuxV/advanced_programming_python)
2. Make your improvements
3. Submit a pull request
4. See the [Pull Requests exercise]({{ '/exercices/05-pull_requests' | relative_url }}) for detailed instructions

---

## External Resources

{% for resource in site.data.navigation.course.resources %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}
