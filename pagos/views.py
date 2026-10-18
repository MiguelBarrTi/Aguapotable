from django.shortcuts import render, redirect, get_object_or_404
from .models import Pago
from .forms import PagoForm

# Create your views here.
# HU-09: Registrar pago
def registrar_pago(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save()
            # actualizar estado del cobro
            pago.cobro.estado = "pagado"
            pago.cobro.save()
            return redirect("lista_pagos")
    else:
        form = PagoForm()
    return render(request, "pagos/registrar.html", {"form": form})

# HU-09: Lista de pagos
def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, "pagos/lista.html", {"pagos": pagos})

# HU-10 Generar Comprobante
def comprobante_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    return render(request, "pagos/comprobante.html", {"pago": pago})
