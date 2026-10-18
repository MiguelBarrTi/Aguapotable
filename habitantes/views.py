from django.shortcuts import render, redirect, get_object_or_404
from .models import Habitante
from .forms import HabitanteForm

#HU-02 Registrar H
def registrar_habitante(request):
    if request.method == "POST":
        form = HabitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_habitantes")  # redirige al listado
    else:
        form = HabitanteForm()
    return render(request, "habitantes/registrar.html", {"form": form})

#HU-03 Modificar H
def modificar_habitante(request, id):
    habitante = get_object_or_404(Habitante, id=id)
    if request.method == "POST":
        form = HabitanteForm(request.POST, instance=habitante)
        if form.is_valid():
            form.save()
            return redirect("lista_habitantes")
    else:
        form = HabitanteForm(instance=habitante)
    return render(request, "habitantes/modificar.html", {"form": form})

#HU-04 Lista H
def lista_habitantes(request):
    query = request.GET.get("q")
    if query:
        habitantes = Habitante.objects.filter(nombre__icontains=query)
    else:
        habitantes = Habitante.objects.all()
    return render(request, "habitantes/lista.html", {"habitantes": habitantes})

#HU-04 Detalle H
def detalle_habitante(request, id):
    habitante = get_object_or_404(Habitante, id=id)
    return render(request, "habitantes/detalle.html", {"habitante": habitante})

#HU-05 Baja H
def baja_habitante(request, id):
    habitante = get_object_or_404(Habitante, id=id)
    if request.method == "POST":
        habitante.activo = False
        habitante.save()
        return redirect("lista_habitantes")
    return render(request, "habitantes/baja.html", {"habitante": habitante})