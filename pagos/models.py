import uuid
from django.db import models
from cobros.models import Cobro

# Create your models here.
class Pago(models.Model):
    cobro = models.ForeignKey(Cobro, on_delete=models.CASCADE)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(auto_now_add=True)
    folio = models.CharField(max_length=100, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Pago {self.cobro.habitante.nombre} - {self.cobro.periodo.nombre} - {self.folio}"