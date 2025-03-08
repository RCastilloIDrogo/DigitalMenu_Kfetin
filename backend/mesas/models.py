from django.db import models

class Mesa(models.Model):
    ESTADO_MESA = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
    ]

    numero = models.PositiveIntegerField(unique=True)
    estado = models.CharField(max_length=20, choices=ESTADO_MESA, default='disponible')

    def __str__(self):
        return f"Mesa {self.numero} - {self.estado}"
