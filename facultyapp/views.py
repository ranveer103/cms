from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('hello')

def about_view(request):
    return HttpResponse('hello2')