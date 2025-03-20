from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    creado_por = serializers.ReadOnlyField(source='creado_por.username')

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'fecha_creacion', 'creado_por']
