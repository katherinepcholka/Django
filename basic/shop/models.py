from django.db import models
from django.utils.text import slugify

class Animal(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'

class Catalog(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalog'

class Available_Products(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_available=1)


class Product(models.Model):
    class Available(models.IntegerChoices):
        OUT = 0, 'Out stock'
        ON = 1, 'On stock'

    title = models.CharField(max_length=60)
    description = models.CharField(max_length=80)
    information = models.TextField(null=True)
    price = models.FloatField()
    is_available = models.BooleanField(choices=Available.choices, default=Available.ON)
    animal = models.ManyToManyField(Animal)
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT)

    objects = models.Manager()
    available = Available_Products()

    def __str__(self):
        return slugify(self.title)
    
    class Meta():
        verbose_name = 'Product'
        verbose_name_plural = 'Products' 