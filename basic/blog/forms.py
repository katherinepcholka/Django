from .models import Post, Category
from django import forms
from django.forms import TextInput, Textarea, SelectMultiple


class PostForm(forms.ModelForm):
    #categories = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'categories']
      
        widgets = {
            "title": TextInput(attrs={'placeholder': 'Название'}),
            "subtitle": TextInput(attrs={ 'placeholder': 'Подзаголовок'}),
            "content": Textarea(attrs={'placeholder': 'Текст'})
        }   

