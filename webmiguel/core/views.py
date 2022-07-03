from turtle import home
from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")
def contact(request):
    return render(request, "core/contact.html")