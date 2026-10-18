from django.shortcuts import render,redirect
from .models import Periodo
from .forms import PeriodoForm

# Create your views here.
#HU-07 Registrar periodo
def registrar_periodo(request):
    if request.method == "POST":
        form = PeriodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_periodos")
    else:
        form = PeriodoForm()
    return render(request, "periodos/registrar.html", {"form": form})

#HU-07 Lista de periodos
def lista_periodos(request):
    periodos = Periodo.objects.all()
    return render(request, "periodos/lista.html", {"periodos": periodos})