from django.urls import path


from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', CreatePage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', Post.as_view(), name='post'),
    path('category/<slug:cat_slug>/', Category.as_view(), name='category'),
    # path('cats/<int:catid>/', categories),
    # path('archive/<int:year>/', categories),
    # path('main/', main),
]
