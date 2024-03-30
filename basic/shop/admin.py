from django.contrib import admin
from .models import Product, Catalog, Animal, Basket


admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(Animal)
admin.site.register(Basket)