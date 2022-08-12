
from django.urls import path
from . import views
from products.views import product_detail, add_to_cart, cart

urlpatterns = [
    path('', views.products, name="products"),
    path('<str:slug>/', product_detail, name='product'),
    path('<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    

    # path('<slug:slug>/', views.product_detail, name="product"),
    # path('<str:slug>/', views.product_detail, name="product"),
]
