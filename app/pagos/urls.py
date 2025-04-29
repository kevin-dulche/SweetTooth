from django.urls import path
from .views import view_menu_pagos, view_realizar_pago, view_consultar_historial_pagos, view_imprimir_recibo, buscar_pago

urlpatterns = [
    path("", view_menu_pagos, name="menu_pagos"),   
    path("realizar_pago/", view_realizar_pago, name="realizar_pago"),   
    path("consulta/", view_consultar_historial_pagos, name="consulta_pagos"),
    path('imprimir_recibo/', view_imprimir_recibo, name='imprimir_recibo'),
    path('buscar_pago/', buscar_pago, name='buscar_pago'),
]
