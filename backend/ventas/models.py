from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Plato

User = get_user_model()

class Venta(models.Model):
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('saldo', 'Saldo Prepago'),
    ]

    cajero = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas', limit_choices_to={'role': 'mesero'})
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metodo_pago = models.CharField(max_length=10, choices=METODOS_PAGO, default='efectivo')

    def __str__(self):
        return f"Venta {self.id} - Total: S/. {self.total} - {self.metodo_pago}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad}x {self.plato.nombre} - Venta {self.venta.id}"
