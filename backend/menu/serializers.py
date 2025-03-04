from rest_framework import serializers
from .models import Categoria, Plato

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PlatoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    imagen = serializers.ImageField(required=False)

    class Meta:
        model = Plato
        fields = '__all__'
