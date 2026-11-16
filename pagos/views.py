from django.shortcuts import render, redirect, get_object_or_404
from .models import Pago
from .forms import PagoForm
from django.db.models import Sum
from  .forms import CorregirPagoForm

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

# HU-12 Estado de cuenta
def estado_de_cuenta(request, habitante_id):
    pagos = Pago.objects.filter(
        cobro_habiante_id= habitante_id
    )

    pendientes = Cobro.object.filter(
        habitante_id = habitante_id,
        estado = 'Pendiente'
    )

    total_pendiente = pendientes.aggregate(
        Sum('Monto')
    )

    return render(
        request,
        'pagos/estado_cuenta.html',
        {
            'pagos' : pagos,
            'pendientes' : pendientes,
            'total pendiente' : total_pendiente
        }
    )

# HU-13 Historial Pagos
def historial_pagos(request, habitante_id):
    historial = Pago.objects.filter(
        cobro_habitante_id = habitante_id
    )

    return render(
        request,
        'pagos/historial_pagos.html',
        {'historial' : historial}
    )

# HU-14 Reporte Pagos
def reporte_pagos(request):

    pagos =Pago.objects.all()
    total = pagos.aaggregate(
        Sum('monto_pago')
    )

    return render(
        request,
        'pagos/reporte_pagos.html',
        {
            'pagos' : pagos,
            'total' :total
        }
    )

# HU-17 Corregir Pagos 
def corregir_pagos(request, id):

    pago = get_object_or_404(
        Pago,
        id=id
    )

    if request.method == "POST":

        form = CorregirPagoForm(
            request.POST,
            instance=pago
        )

        if form.is_valid():

            form.save()

            return redirect(
                "lista_pagos"
            )
        
    else:

        form = CorregirPagoForm(
            instance=pago
        )

    return render(
        'pagos/corregir_pago.html',
        {
            'form' : form
        }
    )