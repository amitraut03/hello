from __future__ import unicode_literals
#from django.http import HttpResponse
import csv,io
from django.shortcuts import render,redirect,HttpResponse
from vms.models import *
from .import forms
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages

def signup_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            messages.success(request,"Account is created")
            form.save()
            return redirect('login')
    else:
        form= UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('reception_portal')
    elif request.user.is_authenticated:
        return render (request,'accounts/reception_portal.html')
    else:
        form= AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return render (request,'accounts/logout.html')
@login_required(login_url="login")
def new_visitors_view(request):
    if request.method=="POST":
        form=forms.new_visitor_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render (request,'accounts/thanks.html')
    else:
        form=forms.new_visitor_form()
    return render(request,'accounts/new_visitors.html',{'form':form})

@login_required(login_url="login")
def visitors_info(request):
    visitor_list=New_visitor.objects.order_by('-date')
    query= request.GET.get('q')
    if query:
        visitor_list=visitor_list.filter(
        Q(phone_no__icontains=query) | Q(vname__icontains=query) | Q(ename__icontains=query) |
         Q(purpose_of_visit__icontains=query) | Q(date__icontains=query))
    return render (request,'accounts/visitors_info.html',{'visitor_list':visitor_list})

@login_required(login_url="login")
def reception_portal_view(request):
    return render (request,'accounts/reception_portal.html')
