from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name= 'home'),
    path('categories', views.categories, name= 'categories'),
    path('category/<int:ctg_id>', views.category, name='category'),
    path('post/<int:post_id>', views.show_post, name='post')
]