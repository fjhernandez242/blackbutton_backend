from django import forms
from .models import catalogo_model

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = catalogo_model
        fields = ['guia', 'producto', 'precio', 'dimensiones', 'imagen']