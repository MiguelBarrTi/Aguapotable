from django.shortcuts import render,redirect
from .models import Cobro
from .forms import CobroForm

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