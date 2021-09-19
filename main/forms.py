from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

from django.core.exceptions import ValidationError




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

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length over 200 symbols')

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login:', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password:', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Confirm password:', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
