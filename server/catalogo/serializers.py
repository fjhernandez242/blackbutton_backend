from rest_framework import serializers
from .models import catalogo_model

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo_model
        fields = ['id', 'producto', 'precio', 'dimensiones', 'imagen']