from django.shortcuts import render, redirect
from .models import Cuota
from .forms import CuotaForm
# Create your views here.
# HU-06: Registrar cuota
def registrar_cuota(request):
    if request.method == "POST":
        form = CuotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_cuotas")
    else:
        form = CuotaForm()
    return render(request, "cuotas/registrar.html", {"form": form})

# HU-06: Lista de cuotas
def lista_cuotas(request):
    cuotas = Cuota.objects.all()
    return render(request, "cuotas/lista.html", {"cuotas": cuotas})
