from rest_framework import serializers
from .models import Pedido, DetallePedido
from menu.models import Plato
from mesas.models import Mesa  # Importamos Mesa


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['plato', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)
    mesero = serializers.ReadOnlyField(source='mesero.username')

    class Meta:
        model = Pedido
        fields = ['id', 'mesero', 'mesa', 'estado', 'fecha_creacion', 'detalles']

class PedidoCreateSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['mesa', 'detalles']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')  # Extraer los detalles del pedido
        pedido = Pedido.objects.create(**validated_data)  # Crear el pedido primero
        for detalle_data in detalles_data:
            DetallePedido.objects.create(pedido=pedido, **detalle_data)  # Asociar los platos al pedido
        return pedido

