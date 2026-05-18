from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view

def landing_view(request):
    return render(request,'landing.html',) 

def signup_view(request):
    if request.method =="POST":
        form=SignupForm(request.POST)