from django.shortcuts import render, get_object_or_404
from college.models import *

# Create your views here.

def home_view(request):
    event_list = Events_model.objects.order_by('-date')[:3]
    news_list = News_model.objects.order_by('-date')[1:4]
    news1_list = News_model.objects.order_by('-date')[0]
    context = {'event_list':event_list,'news_list':news_list,'news1_list':news1_list}
    return render(request, 'index.html',context)


def about_view(request):
    return render(request, 'about-us.html')


def contact_view(request):
    return render(request, 'contact.html')


def event_view(request):
    event_list = Events_model.objects.order_by('-date')
    context = {'event_list':event_list}
    return render(request, 'event-calendar.html',context)


def news_view(request):
    news_list = News_model.objects.order_by('-date')
    context = {'news_list':news_list}
    return render(request, 'news.html',context)


def standardnews_view(request, id=None):
    instance = get_object_or_404(News_model,id=id)
    context = {'instance':instance}
    return render(request, 'standard-news.html' ,context)


def faculty_view(request):
    faculty_list = faculty_model.objects.all()
    context = {'faculty_list':faculty_list}
    return render(request, 'faculty.html',context)
