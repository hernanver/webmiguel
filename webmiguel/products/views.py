
from django.shortcuts import render, get_object_or_404
from .models import Product, Cart, Order
from django.shortcuts import HttpResponse, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})

def product_detail(request, slug):
    product= get_object_or_404(Product, slug=slug)
    return render(request, 'products/detail.html', context={"product": product})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,ordered=False, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))
    