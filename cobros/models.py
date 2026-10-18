from django.db import models
from habitantes.models import Habitante
from periodos.models import Periodo

# Create your models here.
class Cobro(models.Model):
    habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"Cobro {self.habitante.nombre} - {self.periodo.nombre}"