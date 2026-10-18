from django.urls import path
from .views import registrar_pago, lista_pagos, comprobante_pago

urlpatterns = [
    path("registrar/", registrar_pago, name="registrar_pago"),
    path("lista/", lista_pagos, name="lista_pagos"),
    path("comprobante/<int:id>/", comprobante_pago, name="comprobante_pago"),

]
