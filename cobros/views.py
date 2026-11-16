from django.shortcuts import render,redirect, get_object_or_404
from .models import Cobro
from .forms import CobroForm
from django.db.models import Sum

# Create your views here.
# HU-08: Generar cobro
def generar_cobro(request):
    if request.method == "POST":
        form = CobroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_cobros")
    else:
        form = CobroForm()
    return render(request, "cobros/generar.html", {"form": form})

# HU-08: Lista de cobros
def lista_cobros(request):
    cobros = Cobro.objects.all()
    return render(request, "cobros/lista.html", {"cobros": cobros})

# HU-11: consultar adeudos
def consultar_adeudos(request):

    adeudos = Cobro.objects.filter(
        estado = 'pendiente'
    )

    return render(
        request, 
        'Cobros/adeudos.html',
        {'adeudos': adeudos}
    )

def detalle_adeudo(request, id):

    adeudo = get_object_or_404(
        cobro,
        id=id
    )

    return render(
        request,
        'Cobros/detalle_adeudo.html',
        {'adeudo': adeudo}
    )

# HU-15 Reporte de Adeudos 
def reporte_adeudos(request):

    adeudos = Cobro.objects.filter(
        estado = 'pendiente'
    )

    total = adeudos.aggregate(
        Sum('monto')
    )

    return render(
        request,
        'cobros/reporte_adeudos.html',
        {
            'adeudos' : adeudos,
            'total' : total
        }
    )