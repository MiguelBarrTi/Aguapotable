from django.urls import path
from .views import registrar_habitante, modificar_habitante, lista_habitantes, detalle_habitante, baja_habitante

urlpatterns = [
    # HU-02
    path("registrar/", registrar_habitante, name="registrar_habitante"),

    # HU-03
    path("modificar/<int:id>/", modificar_habitante, name="modificar_habitante"),

    # HU-04
    path("lista/", lista_habitantes, name="lista_habitantes"),
    path("detalle/<int:id>/", detalle_habitante, name="detalle_habitante"),

    # HU-05
    path("baja/<int:id>/", baja_habitante, name="baja_habitante"),
]
