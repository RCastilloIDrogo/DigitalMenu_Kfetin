from django.db import models

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)  # Número único de la mesa
    capacidad = models.PositiveIntegerField(default=4)  # Capacidad de la mesa

    def __str__(self):
        return f"Mesa {self.numero} (Capacidad: {self.capacidad})"
