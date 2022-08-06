from django.db import models
from django.urls import reverse

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
    

    # def get_absolute_url(self):
    #     return reverse("product", kwargs={"slug": self.slug})
    