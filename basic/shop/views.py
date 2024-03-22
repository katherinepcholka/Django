from django.shortcuts import render, get_object_or_404
from .models import Product, Catalog, Animal
from .forms import ProductForm

def main(request):
    return render (request, 'shop/main.html')

def catalog(request):
    catalog = Catalog.objects.all
    data = {
        'catalog': catalog,
        }
    return render (request, 'shop/catalog.html', data)

def element(request, anml_id, ctl_id):
    animal = get_object_or_404(Animal, pk=anml_id)
    element = get_object_or_404(Catalog, pk=ctl_id)
    product = Product.objects.filter(catalog=element, animal=animal, is_available=1)
    context = {
        'element': element,
        'product': product
        }
    return render (request, 'shop/element.html', context)

def product(request, prdt_id):
    product = get_object_or_404(Product, pk=prdt_id)
    info = {
        'product': product,
        }
    return render (request, 'shop/product.html', info)

def create_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверное заполнение'
    form = ProductForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'shop/create_product.html', data)
