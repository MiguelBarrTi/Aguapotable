from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "usuarios/login.html")

def panel_habitante(request):

    return render(
        request,
        "usuarios/panel_habitante.html"
    )