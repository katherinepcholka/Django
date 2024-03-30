from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 

class Post(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=80)
    content = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return slugify(self.title)
    
    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts' 

