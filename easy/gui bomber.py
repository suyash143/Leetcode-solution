import time

import pyautogui
s='''{% extends 'index_main.html' %}
{% load static %}
{% block content %}
  <main id="main">

    <!-- ======= Breadcrumbs ======= -->
    <section id="breadcrumbs" class="breadcrumbs">
      <div class="container">

        <div class="d-flex justify-content-between align-items-center">
          <h2>{{ event.title }}</h2>
          <ol>
            <li><a href="{% url 'index' %}">Home</a></li>
            <li>Event Details</li>
          </ol>
        </div>

      </div>
    </section>
    <!-- End Breadcrumbs -->

    <!-- ======= Portfolio Details Section ======= -->
    <section id="portfolio-details" class="portfolio-details">
      <div class="container">

        <div class="row gy-4">

          <div class="col-lg-8">
            <div class="portfolio-details-slider swiper">
              <div class="swiper-wrapper align-items-center">

                <div class="swiper-slide">
                  <img src="{% static event.imageURL %}" alt="{{ event.title }}" >

                </div>
                  {% if event.cover_image_2 %}
              <div class="swiper-slide">


                  <img src="{% static event.imageURL_2 %}" alt="{{ event.title }}" >

                </div>
 {% endif %}

              </div>
              <div class="swiper-pagination"></div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="portfolio-info">
              <h3>Event Information</h3>
              <ul>
                  {% if event.vertical %}
                <li><strong>Event Vertical</strong>: {{ event.vertical }}</li>
                  {% endif %}
                <li><strong>Event Date</strong>:{% if event.date %} {{ event.date }}{% else %} Coming Soon{% endif %}</li>
                <li><strong>Registration link</strong>:{% if event.registration_link %} <a href="{{ event.registration_link }}">{{ event.registration_link|truncatechars:25 }}</a>{% else %} Coming Soon{% endif %}</li>
                {% if event.last_date %}
                  <li><strong>Last Date</strong>: {{ event.last_date }}</li>
              {% endif %}
              </ul>
            </div>
            <div class="portfolio-description">
              <h2>Description</h2>
              <p>
                {{ event.description }}
              </p>
            </div>
          </div>

        </div>

      </div>
    </section><!-- End Portfolio Details Section -->


  </main><!-- End #main -->

{% endblock content %}'''

t=s.split()
print(len(t))
for i in t:
    pyautogui.write(f"{i}")
    pyautogui.press('enter')