from django.urls import path
from .views import generar_cobro, lista_cobros

urlpatterns = [
    path("generar/", generar_cobro, name="generar_cobro"),
    path("lista/", lista_cobros, name="lista_cobros"),
]
