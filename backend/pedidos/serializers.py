from rest_framework import serializers
from .models import Pedido, DetallePedido
from menu.models import Plato

class DetallePedidoSerializer(serializers.ModelSerializer):
    plato_nombre = serializers.ReadOnlyField(source='plato.nombre')  # Muestra el nombre del plato en lugar del ID

    class Meta:
        model = DetallePedido
        fields = ['id', 'pedido', 'plato', 'plato_nombre', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)
    mesero = serializers.ReadOnlyField(source='mesero.username')

    class Meta:
        model = Pedido
        fields = ['id', 'mesero', 'mesa', 'estado', 'fecha_creacion', 'detalles']

class PedidoCreateSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True)  # Ahora permitimos agregar detalles en la creación

    class Meta:
        model = Pedido
        fields = ['mesa', 'detalles']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        pedido = Pedido.objects.create(**validated_data, mesero=self.context['request'].user)
        for detalle_data in detalles_data:
            DetallePedido.objects.create(pedido=pedido, **detalle_data)
        return pedido

