from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'myapp/index.html', context)

def show(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'myapp/show.html', context)

def home(request):
    products = Product.objects.all() 
    context = {'products': products}
    return render(request, 'myapp/home.html', context)

def show_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})