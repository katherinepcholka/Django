from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Product, Catalog, Animal
from django import forms
from django.forms import TextInput, Textarea


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['catalog'].empty_label = "Catalog"
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'information', 'price', 'is_available', 'animal', 'catalog' ]


    