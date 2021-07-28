from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    return HttpResponse(f"Главная страница")

def categories(request, catid):

    return HttpResponse(f"Главная страница. <br> <p> {catid} </p>")
