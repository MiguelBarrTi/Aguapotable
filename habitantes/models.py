from django.db import models

class Habitante(models.Model):

    curp = models.CharField(
        max_length=18,
        unique=True
    )

    nombre = models.CharField(
        max_length=100
    )

    apellido_paterno = models.CharField(
        max_length=100
    )

    apellido_materno = models.CharField(
        max_length=100
    )

    telefono = models.CharField(
        max_length=15
    )

    domicilio = models.CharField(
        max_length=200
    )

    numero_exterior = models.CharField(
        max_length=20
    )

    numero_interior = models.CharField(
        max_length=20,
        blank=True
    )

    codigo_postal = models.CharField(
        max_length=5
    )

    lineas_domicilio = models.IntegerField(
        default=1
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"