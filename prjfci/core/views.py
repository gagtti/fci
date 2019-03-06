from django.shortcuts import render, HttpRequest

# Create your views here.

def home(request):
    return(HttpRequest("Home"))