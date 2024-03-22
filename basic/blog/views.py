from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import PostForm

def home(request):
    return render (request, 'blog/home.html')

def categories(request):
    categories = Category.objects.all
    data = {
        'categories': categories
        }
    return render (request, 'blog/categories.html', data)

def category(request, ctg_id):
    category = get_object_or_404(Category, pk=ctg_id)
    post = Post.objects.filter(categories=category)
    context = {
        'category': category,
        'post': post
        }
    return render (request, 'blog/category.html', context)

def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    info = {
        'post': post,
        }
    return render (request, 'blog/post.html', info)

def create_post(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверное заполнение формы'
    form = PostForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create_post.html', data)

