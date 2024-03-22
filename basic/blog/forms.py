from .models import Post, Category
from django import forms
from django.forms import TextInput


class PostForm(forms.ModelForm):
    #categories = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'categories']

