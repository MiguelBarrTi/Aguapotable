from django.urls import path
from .views import registrar_periodo, lista_periodos

urlpatterns = [
    path("registrar/", registrar_periodo, name="registrar_periodo"),
    path("lista/", lista_periodos, name="lista_periodos"),
]
