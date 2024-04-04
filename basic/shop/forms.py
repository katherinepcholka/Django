from .models import Product, Catalog, Animal
from django import forms
from django.forms import TextInput, Textarea, IntegerField


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['catalog'].empty_label = "Catalog"
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'information', 'price', 'is_available', 'animal', 'catalog' ]

        widgets = {
            "title": TextInput(attrs={'placeholder': 'Название'}),
            "description": TextInput(attrs={'placeholder': 'Описание'}),
            "information": Textarea(attrs={'placeholder': 'Информация'})
        }