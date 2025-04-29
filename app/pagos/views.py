import random
from django.shortcuts import render
from pagos.models import Pago  # Asegúrate de importar el modelo Pago
from .forms import PagoForm  # Asegúrate de importar el formulario de Pago (si lo tienes)
from .models.gestor_de_Pago import GestorPago  # Asegúrate de importar el GestorPago

# Vista para realizar un pago
def view_realizar_pago(request):
    mensaje = ""
    if request.method == 'POST':
        # Recoger los datos del formulario de pago
        id_pago = request.POST.get('id_pago')
        id_servicio = request.POST.get('id_servicio')
        id_paciente = request.POST.get('id_paciente')
        nombre_paciente = request.POST.get('nombre_paciente')
        tipo_tratamiento = request.POST.get('tipo_tratamiento')
        descripcion_tratamiento = request.POST.get('descripcion_tratamiento')
        especialista_responsable = request.POST.get('especialista_responsable')
        fecha_pago = request.POST.get('fecha_pago')
        monto_pago = request.POST.get('monto_pago')
        
        # Información del método de pago
        metodo_pago = request.POST.get('metodo_pago')
        tipo_tarjeta = request.POST.get('tipo_tarjeta')
        numero_tarjeta = request.POST.get('numero_tarjeta')
        fecha_expiracion = request.POST.get('fecha_expiracion')
        cvv = request.POST.get('cvv')
        correo_paypal = request.POST.get('correo_paypal')

        # Buscar el pago en la base de datos
        try:
            pago = Pago.objects.get(id_pago=id_pago)
        except Pago.DoesNotExist:
            mensaje = "El pago seleccionado no existe."
            return render(request, 'pagos/realizar_pago.html', {
                'form': PagoForm(),
                'pagos_pendientes': Pago.objects.filter(estado_pago='pendiente'),
                'mensaje': mensaje,
            })

        # (Opcional) Detalles del método de pago
        detalles = ""
        if metodo_pago == 'tarjeta':
            detalles = f"{tipo_tarjeta} terminada en {numero_tarjeta[-4:]}"
        elif metodo_pago == 'paypal':
            detalles = f"Cuenta PayPal: {correo_paypal}"

        # Procesar el pago usando la clase GestorPago
        gestor = GestorPago()
        if gestor.procesar_pago(pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles):
            # Actualizar el estado del pago a "completado"
            pago.estado_pago = "completado"
            pago.save()
            mensaje = "Pago procesado con éxito."
        else:
            mensaje = "Error al procesar el pago."

    # En GET y en POST, se renderiza la misma plantilla
    return render(request, 'pagos/realizar_pago.html', {
        'form': PagoForm(),
        'pagos_pendientes': Pago.objects.filter(estado_pago='pendiente'),
        'mensaje': mensaje,
    })

# Vista para el menú de pagos
def view_menu_pagos(request):
    return render(request, "pagos/menu_pagos.html")

# Vista para imprimir el recibo
def view_imprimir_recibo(request):
    if request.method == 'POST':
        # Generar un número de transacción aleatorio de 10 dígitos
        numero_transaccion = str(random.randint(1000000000, 9999999999))
        
        # Recuperar los datos enviados en el formulario
        paciente = request.POST.get('paciente')
        concepto = request.POST.get('concepto')
        monto = request.POST.get('monto')
        metodo_pago = request.POST.get('metodo_pago')

        # Crear el gestor y generar el recibo
        gestor = GestorPago()
        ruta = gestor.generar_recibo(numero_transaccion, paciente, concepto, monto, metodo_pago)
        gestor.imprimir_recibo(ruta)

        return render(request, "pagos/imprimir_recibo.html", {"ruta_recibo": ruta})
    return render(request, "pagos/imprimir_recibo.html")

# Vista para consultar el historial de pagos
def view_consultar_historial_pagos(request):
    pagos = Pago.objects.all()  # Puedes filtrar según necesites
    return render(request, "pagos/consultar_historial_pagos.html", {"pagos": pagos})

def buscar_pago(request):
    buscar_id = request.GET.get("buscar_id")  # Captura lo que el usuario escribió
    pagos = []

    if buscar_id:
        pagos = Pago.objects.filter(id_pago=buscar_id)  # Busca el pago por ID exacto

    return render(request, "pagos/consultar_historial_pagos.html", {"pagos": pagos})