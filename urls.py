from django.contrib import admin
from django.urls import path, re_path
from college import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about_us', views.about_view, name='about-us'),
    path('contact', views.contact_view, name='contact'),
    path('event', views.event_view, name='event'),
    path('news', views.news_view, name='news'),
    re_path(r'(?P<id>\d+)/$', views.standardnews_view, name='news1'),
    path('faculty', views.faculty_view, name='faculty'),


    ]
