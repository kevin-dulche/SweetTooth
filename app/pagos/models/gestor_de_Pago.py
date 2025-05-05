from .adapter.pagar_cita import PagarCita
from .adapter.adaptador_pagar_medicamento import Adaptador_PagarMedicamento
from .adapter.gestor_pago_medicamento import Gestor_PagoMedicamento
from .master_slave.Master_PagoDeCita import Master_PagoDeCita
from pagos.models import Pago

class GestorPago():
    def __init__(self):
        self.master_pago = Master_PagoDeCita()
        
        

    def procesar_pago(self, pago:Pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles):
        if pago.tipo_tratamiento == "Medicamento":
            gestor_pago_medicamento = Gestor_PagoMedicamento()
            pagar_medicamento = Adaptador_PagarMedicamento(pago, gestor_pago_medicamento)
            pagar_medicamento.pagar()
        else:
            self.pagar_cita = PagarCita(pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles)
            # Se ejecuta el pago
            return self.pagar_cita.pagar()
    

    def mostrar_pagos(self):
        # Aquí puedes implementar la lógica para mostrar los pagos procesados
        pass

    def generar_recibo(self, numero_transaccion, paciente, concepto, monto, metodo_pago):
        # Aquí puedes implementar la lógica para generar un recibo
        master_pago = Master_PagoDeCita()
        direccion = master_pago.generar_recibo(numero_transaccion, paciente, concepto, monto, metodo_pago)
        return direccion        


    def imprimir_recibo(self, ruta):
        # Aquí puedes implementar la lógica para imprimir el recibo
        master_pago = Master_PagoDeCita()
        master_pago.imprimir_recibo(ruta)