from django import forms
from .models import *


# class AddPostForm(forms.ModelForm):
#     title = forms.CharField(max_length=255, label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255, label="URL")
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Content')
#     is_published = forms.BooleanField(required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category", empty_label='Category not choosed'

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category not selected'
        self.fields['cat'].label = 'Category'

    class Meta:
        model = Car
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
