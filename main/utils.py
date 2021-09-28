from .models import *
from django.db.models import *
from django.core.cache import cache


main_menu = [{'title': 'About', 'url_name': 'about'},
            {'title': 'Add article', 'url_name': 'add_page'},
            {'title': 'Contact', 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('car'))
            cache.set('cats', cats, 60*15)

        user_menu = main_menu.copy()
        if not self.request.user.is_staff:
            user_menu.pop(1)

        context['main_menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context