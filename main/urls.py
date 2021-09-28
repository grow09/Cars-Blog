from django.urls import path
from django.views.decorators.cache import cache_page


from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', CreatePage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', Post.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarCategory.as_view(), name='category'),
    path('logout/', logout_user, name='logout'),
    # path('cats/<int:catid>/', categories),
    # path('archive/<int:year>/', categories),
    # path('main/', main),
]
