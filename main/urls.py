from django.urls import path


from .views import *

urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', categories),
    path('archive/<int:year>/', categories),
    path('main/', main),
]