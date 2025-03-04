from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='platos')
    precio_personal = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    precio_mediana = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    precio_grande = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='platos/', null=True, blank=True)  # Agregamos la imagen

    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"
