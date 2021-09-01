from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.shortcuts import redirect
from .models import *


# Create your views here.

main_menu = [{'title': 'About', 'url_name': 'about'},
            {'title': 'Add article', 'url_name': 'add_page'},
            {'title': 'Contacts', 'url_name': 'contact'},
            {'title': 'Login', 'url_name': 'login'}
]


def index(request):
    posts = Car.objects.all()
    context = {'posts': posts,
               'main_menu': main_menu,
               'title': 'Main',
               'cat_selected': 0
   }

    return render(request, 'main/main.html', context=context)


def show_category(request, cat_id):
    posts = Car.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if cat_id > len(cats) or cat_id == 0:
        raise Http404()

    context = {'posts': posts,
               'cats': cats,
               'main_menu': main_menu,
               'title': cats[cat_id-1],
               'cat_selected': cat_id,
               }

    return render(request, 'main/main.html', context=context)


def show_post(request, post_id):
    post = get_object_or_404(Car, pk=post_id)

    context = {
        'post': post,
        'main_menu': main_menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'main/post.html', context=context)


def about(request):
    return render(request, 'main/about.html', {'main_menu': main_menu, 'title': 'About'})


def addpage(request):
    return HttpResponse('Add article')


def contact(request):
    return HttpResponse('Contacts')


def login(request):
    return HttpResponse('Login')


# def categories(request, year):
#     if int(year) > datetime.now().year:
#         return redirect('/archive/'+ datetime.now().year +'/', permanent=True)
#     return HttpResponse(f"Выбран {year} год.")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!</h1>')
