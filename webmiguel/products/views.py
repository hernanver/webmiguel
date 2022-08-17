
from django.shortcuts import render, get_object_or_404
from .models import Product, Cart, Order
from django.shortcuts import HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import User
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

def cart(request):
    cart= get_object_or_404(Cart, user=request.user)
    return render(request, 'products/cart.html', context={"orders":cart.orders.all()})

def delete_cart(request):
   
    if cart := request.user.cart:
        cart.delete()

    return redirect('products')

def delete_producto(request):
   
    order = Order(request)
    product = Product.objects.filter()
    order.product.eliminar()
    

    return redirect('products')

# def eliminar_producto(request, producto_id):
#     carrito = Order(request)
#     producto = Product.objects.get(id=producto_id)
#     carrito.eliminar(producto)
#     return redirect("products")

    