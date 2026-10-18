from django.db import models

# Create your models here.
class Cuota(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    periodo = models.CharField(max_length=100)
    fecha_limite = models.DateField()

    def __str__(self):
        return f"Cuota {self.periodo} - ${self.monto}"