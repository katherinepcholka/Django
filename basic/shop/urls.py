from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name= 'main'),
    path('catalog', views.catalog, name= 'catalog'),
    path('catalog/<int:anml_id>/<int:ctl_id>', views.element, name='element'),
    path('product/<int:prdt_id>', views.product, name='product')
]