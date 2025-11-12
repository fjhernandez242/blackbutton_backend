from django.db import models

# Create your models here.
class catalogo_model(models.Model):

    guia = models.CharField(max_length=255, verbose_name='Guia', null=True, blank=True)
    producto = models.CharField(max_length=255, verbose_name='Producto', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', null=True, blank=True)
    dimensiones = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Dimensiones', null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)
    fecha_registro = models.DateTimeField(verbose_name='Fecha de regsitro', null=True, blank=True)

    class Meta:
        verbose_name="Catalogo"
        verbose_name_plural="Catalogos"

    def __str__(self):
        return self.guia