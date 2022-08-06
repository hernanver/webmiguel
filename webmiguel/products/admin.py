from django.contrib import admin
from .models import Product, Order, Cart


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Cart)

