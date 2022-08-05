
from django.urls import path
from . import views
# from products.views import product_detail

urlpatterns = [
    path('', views.products, name="products"),
    # path('<slug:slug>/', views.product_detail, name="product"),
    # path('<str:slug>/', views.product_detail, name="product"),
]
