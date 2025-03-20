from rest_framework import serializers
from .models import Venta, DetalleVenta

class DetalleVentaSerializer(serializers.ModelSerializer):
    plato_nombre = serializers.ReadOnlyField(source='plato.nombre')

    class Meta:
        model = DetalleVenta
        fields = ['plato', 'plato_nombre', 'cantidad', 'precio_unitario']

class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True, read_only=True)
    cajero = serializers.SerializerMethodField()
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    
    class Meta:
        model = Venta
        fields = ['id', 'cajero', 'fecha_creacion', 'total', 'metodo_pago', 'detalles']

    def get_cajero(self, obj):
        return obj.cajero.username if obj.cajero else "Desconocido"

class VentaCreateSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)

    class Meta:
        model = Venta
        fields = ['detalles', 'metodo_pago']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        venta = Venta.objects.create(**validated_data)

        total = 0
        for detalle_data in detalles_data:
            plato = detalle_data['plato']
            cantidad = detalle_data['cantidad']
            precio_unitario = plato.precio  

            total += cantidad * precio_unitario  

            DetalleVenta.objects.create(
                venta=venta,
                plato=plato,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )

        venta.total = total
        venta.save()
        return venta
