from rest_framework import serializers
from .models import Pedido, DetallePedido
from menu.models import Plato
from mesas.models import Mesa
from django.contrib.auth import get_user_model

User = get_user_model()  # Obtener el modelo de usuario

# Serializador para los detalles del pedido (platos y cantidades)
class DetallePedidoSerializer(serializers.ModelSerializer):
    plato_nombre = serializers.ReadOnlyField(source='plato.nombre')

    class Meta:
        model = DetallePedido
        fields = ['plato', 'plato_nombre', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)
    mesero = serializers.SerializerMethodField()
    estado = serializers.CharField()
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'mesero', 'estado', 'fecha_creacion', 'detalles']

    def get_mesero(self, obj):
        return obj.mesero.username if obj.mesero else "Sin asignar"

# Serializador para la creación de pedidos
class PedidoCreateSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['mesa', 'detalles']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')  
        pedido = Pedido.objects.create(**validated_data)  

        # Crear los detalles del pedido
        for detalle_data in detalles_data:
            DetallePedido.objects.create(pedido=pedido, **detalle_data)  

        return pedido
