from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, 
        verbose_name="Título")
    subtitle = models.CharField(max_length=200, 
        verbose_name="Subtítulo")
    content = models.TextField(
        verbose_name="Contenido")
    price = models.CharField(max_length=10, verbose_name="Precio", default='DEFAULT VALUE')
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
          return self.title