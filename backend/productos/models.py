from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos', limit_choices_to={'role': 'Varona'})

    def __str__(self):
        return f"{self.nombre} - S/. {self.precio}"
