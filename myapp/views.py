from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
  products = Product.objects.all()
  return render(request, 'myapp/index.html', {'products': products})

def product_detail(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  return render(request, 'myapp/show.html', {'product': product})

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def show(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'show.html', {'product': product})