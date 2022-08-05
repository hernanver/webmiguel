from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})

# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'products/detail.html', context={'product': product})