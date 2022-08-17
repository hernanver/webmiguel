from audioop import add
from functools import total_ordering
from django.db import models
from django.urls import reverse
from django.utils import timezone
from webmiguel.settings import AUTH_USER_MODEL
from operator import __add__
from itertools import accumulate
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, 
        verbose_name="Título")
    slug = models.SlugField(max_length=128)
    subtitle = models.CharField(max_length=200, 
        verbose_name="Subtítulo")
    # slug= models.SlugField(max_length=128)
    # stock= models.IntegerField(default=0)
    content = models.TextField(
        verbose_name="Contenido")
    price = models.FloatField(max_length=10, verbose_name="Precio", default='0.0')
    stock = models.IntegerField(default=0)
    image = models.ImageField(verbose_name="Imagen", 
        upload_to="products")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, 
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def __str__(self):
          return f"{self.title} ({self.stock})"

    def get_absolute_url(self):
        return reverse("product", kwargs= {"slug": self.slug})
    



class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    ordered= models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    total=0
    suma_final= 0
    
    def __str__(self):
        return f"{self.product} ({self.quantity})"

    
    def calculo_total(self):
        total = 0
        subtotal = self.quantity * self.product.price
        Order.total = Order.total + subtotal
        return (subtotal)

    def total_carrito(self):
        Order.suma_final = Order.total
        Order.total = 0
        
        return (Order.suma_final)

    def delete_product(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        del self.product
        super().delete(*args, **kwargs)

    def eliminar(self,product):
        id = str(product)
        if product in self.order:
            del self.product
            self.order.save()

    


    

        
    


    # def total_carrito(self):
    #     suma= 0
    #     total = 0
    #     for order in Order:
    #         total = (self.quantity * self.product.price)
    #         suma = suma + total
    #     return (suma)
        
    






class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    total = 0
    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)

    # def eliminar(self, producto):
    #     id = str(producto.id)
    #     if id in self.orders.all():
    #         del self.order.product[id]
    #         self.order.save()