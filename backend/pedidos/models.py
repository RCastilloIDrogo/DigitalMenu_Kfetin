from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Plato
from mesas.models import Mesa

User = get_user_model()

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('pendiente', 'Pendiente'),
        ('en_preparacion', 'En Preparación'),
        ('listo', 'Listo'),
    ]

    mesero = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos', limit_choices_to={'role': 'mesero'})
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='pedidos')  # Ahora hace referencia a Mesa
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.mesa} - {self.estado}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad}x {self.plato.nombre} (Pedido {self.pedido.id})"
