from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect
from .models import *


# Create your views here.

main_menu = ['Main page', 'About', 'Contacts']

def index(request):
    return render(request, 'main/index.html', {'main_menu': main_menu, 'title': 'Main page'})


def main(request):
    posts = Cars.objects.all()
    return render(request, 'main/main.html', {'posts': posts, 'main_menu': main_menu, 'title': 'Main'})


def categories(request, year):
    if int(year) > datetime.now().year:
        return redirect('/archive/'+ datetime.now().year +'/', permanent=True)
    return HttpResponse(f"Выбран {year} год.")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!</h1>')
