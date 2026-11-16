from django.urls import path
from .views import registrar_pago, lista_pagos, comprobante_pago,estado_de_cuenta, historial_pagos,reporte_pagos,corregir_pagos

urlpatterns = [
    path("registrar/", registrar_pago, name="registrar_pago"),
    path("lista/", lista_pagos, name="lista_pagos"),
    path("comprobante/<int:id>/", comprobante_pago, name="comprobante_pago"),
    path("estado-cuenta/<int:habitante_id>/", estado_de_cuenta, name="estado_cuenta"),
    path("historial/<int:habitante_id>/", historial_pagos, name="historial_pagos"),
    path("reporte/", reporte_pagos, name="reporte_pagos"),
    path("corregir/<int:id>/", corregir_pagos, name="corregir_pago"),

]
