from django.urls import path
from .views import registrar_cuota, lista_cuotas

urlpatterns = [
    path("registrar/", registrar_cuota, name="registrar_cuota"),
    path("lista/", lista_cuotas, name="lista_cuotas"),
]

