from turtle import home
from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/index.html")
def services(request):
    return render(request, "core/services.html")

def products(request):
    return render(request, "core/products.html")
def about(request):
    return render(request, "core/about.html")
def contact(request):
    return render(request, "core/contact.html")