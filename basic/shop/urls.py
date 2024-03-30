from django.urls import path, include
from . import views

urlpatterns = [
    path('main', views.main, name= 'main'),
    path('catalog', views.catalog, name= 'catalog'),
    path('catalog/<int:anml_id>/<int:ctl_id>', views.element, name='element'),
    path('product/<int:prdt_id>', views.product, name='product'),
    path('create_product', views.create_product, name='create_product'),
    path('order/<int:prdt_id>', views.order, name='order'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),
    path('basket', views.basket, name= 'basket'),
    path('', include('django.contrib.auth.urls')) 
]