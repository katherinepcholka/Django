from django.shortcuts import render

def main(request):
    return render (request, 'shop/main.html')

def catalog(request):
    return render (request, 'shop/catalog.html')
