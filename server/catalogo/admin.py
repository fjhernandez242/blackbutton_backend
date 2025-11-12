from django.contrib import admin
from .models import catalogo_model

# Register your models here.
class CatalogoModelAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista del panel
    list_display = ('guia', 'producto', 'precio')
    # Añade un campo de búsqueda
    search_fields = ['guia', 'producto']
    # Añade filtros en la barra lateral
    list_filter = ('guia', 'producto')

# Ahora registra tu modelo con la clase personalizada
admin.site.register(catalogo_model, CatalogoModelAdmin)
