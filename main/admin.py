from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Cars)
admin.site.register(Category)
