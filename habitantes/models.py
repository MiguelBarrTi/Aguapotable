from django.db import models

# Create your models here.
class Habitante(models.Model):
    nombre = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
