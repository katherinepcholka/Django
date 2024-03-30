from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name= 'home'),
    path('categories', views.categories, name= 'categories'),
    path('category/<int:ctg_id>', views.category, name='category'),
    path('post/<int:post_id>', views.show_post, name='post'),
    path('create_post', views.create_post, name='create_post'),
    path('post/<int:post_id>/update_post', views.update_post, name='update_post'),
    path('post/<int:post_id>/delete_post', views.delete_post, name='delete_post')
]