from .models import *
from django.db.models import *


main_menu = [{'title': 'About', 'url_name': 'about'},
            {'title': 'Add article', 'url_name': 'add_page'},
            {'title': 'Contacts', 'url_name': 'contact'},
            {'title': 'Login', 'url_name': 'login'}
]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('car'))
        user_menu = main_menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['main_menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context