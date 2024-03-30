from .models import Post, Category
from django import forms
from django.forms import TextInput, Textarea, SelectMultiple


class PostForm(forms.ModelForm):
    #categories = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'categories']
      
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            "subtitle": TextInput(attrs={'class': 'form-control', 'placeholder': 'Подзаголовок'}),
            "content": Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
            "categories": SelectMultiple(attrs={'class': 'form-control'})
        }   

