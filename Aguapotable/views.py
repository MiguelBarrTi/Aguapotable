from django.shortcuts import render
from habitantes.models import Habitante
from cobros.models import Cobro
from pagos.models import Pago
from django.db.models import Sum
def dashboard_admin(request):
    return render(request, "panel.html")

# HU-16 Resumen Administrativo
def resumen_administrativo(request):

    habitantes = Habitante.objects.count()

    cuotas = Cobro.objects.count()

    pagos = Pago.objects.count()

    adeudo = Cobro.objects.filter(
        estado = "pendiente"
    ).count()

    recaudado = Pago.objects.aggregate(
        Sum("monto_pagado")
    )

    return render(
        request,
        {
            "habitantes" : habitantes,
            "cuotas" : cuotas,
            "pagos" : pagos,
            "adeudos" : adeudo,
            "recacudando" : recaudado
        }
    )
