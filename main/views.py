from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


# Create your views here.

main_menu = [{'title': 'About', 'url_name': 'about'},
            {'title': 'Add article', 'url_name': 'add_page'},
            {'title': 'Contacts', 'url_name': 'contact'},
            {'title': 'Login', 'url_name': 'login'}
]

class Home(ListView):
    model = Car
    template_name = 'main/main.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Home page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = 'Home page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Car.objects.filter(is_published=True)


# def index(request):
#     posts = Car.objects.all()
#     context = {'posts': posts,
#                'main_menu': main_menu,
#                'title': 'Main',
#                'cat_selected': 0
#                }
#
#     return render(request, 'main/main.html', context=context)

class Category(ListView):
    model = Car
    template_name = 'main/main.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(request, cat_slug):
#
#     if cat_slug not in Category.objects.all().values_list('slug', flat=True):
#         raise Http404()
#
#     cat_selected = Category.objects.filter(slug=cat_slug).values_list('pk', flat=True)[0]
#     cat_name = Category.objects.filter(slug=cat_slug).values_list('name', flat=True)[0]
#     cats = Category.objects.all()
#     posts = Car.objects.filter(cat_id=cat_selected)
#
#     context = {'posts': posts,
#                'cats': cats,
#                'main_menu': main_menu,
#                'title': cat_name,
#                'cat_selected': cat_selected,
#                }
#
#     return render(request, 'main/main.html', context=context)


class Post(DetailView):
    model = Car
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = context['post']
        return context

# def show_post(request, post_slug):
#     post = get_object_or_404(Car, slug=post_slug)
#
#     context = {
#         'post': post,
#         'main_menu': main_menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'main/post.html', context=context)


def about(request):
    return render(request, 'main/about.html', {'main_menu': main_menu, 'title': 'About'})


class CreatePage(CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = 'Add new article'
        return context

# def addpage(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     return render(request, 'main/addpage.html', {'form': form, 'main_menu': main_menu, 'title': 'Add article'})


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
