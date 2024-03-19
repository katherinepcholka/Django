from django.shortcuts import render

def home(request):
    return render (request, 'blog/home.html')

def categories(request):
    return render (request, 'blog/categories.html')