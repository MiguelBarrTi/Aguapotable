from django.urls import path
from .views import generar_cobro, lista_cobros,consultar_adeudos,detalle_adeudo, reporte_adeudos

urlpatterns = [
    path("generar/", generar_cobro, name="generar_cobro"),
    path("lista/", lista_cobros, name="lista_cobros"),
    path("adeudos/", consultar_adeudos, name="consultar_adeudos"),
    path("adeudos/<int:id>", detalle_adeudo, name="detalle_adeudo"),
    path("reporte-adeudos/", reporte_adeudos, name="reporte_adeudos"),

]
