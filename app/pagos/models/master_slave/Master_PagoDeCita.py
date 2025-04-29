from .Slave_PagoCita import Slave_PagoCita
from .Slave_Recibo import Slave_Recibo
from .Slave_Impresion import Slave_Impresion
from .Slave_AccionesPago import Slave_AccionesPago
from pagos.models import Pago 

class Master_PagoDeCita:
    def __init__(self):
        self.slave_pago = Slave_PagoCita()
        self.slave_recibo = Slave_Recibo()
        self.slave_impresion = Slave_Impresion()
        self.slave_acciones_pago = Slave_AccionesPago()

    def procesar_pago(self, pago:Pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles):
        
        resultado_pago = self.realizar_pago(pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles)
        return resultado_pago
        
        """if resultado_pago:
            print("Pago realizado exitosamente.")
            recibo = self.generar_recibo(resultado_pago['numero_transaccion'])
            if recibo:
                print(f"Recibo generado: {recibo}")
                self.imprimir_recibo(recibo)
                self.registrar_pago(resultado_pago)
            else:
                print("Error al generar el recibo.")
        else:
            print("Error al realizar el pago.")
        print("\n---")"""

    """def simular_consulta_por_fecha(self):
        historial = self.consultar_historial(fecha_inicio="2025-04-01", fecha_fin="2025-04-10")
        if historial:
            print("Historial de pagos por fecha:")
            for pago in historial:
                print(f"Número de Pago: {pago['numero_pago']}, Fecha: {pago['fecha_pago']}, Monto: {pago['monto']}")
        else:
            print("No se encontraron pagos en el rango de fechas especificado.")
        print("\n---")"""

    def simular_busqueda_pago(self):
        pago = self.buscar_pago("PAGO-001")
        if pago:
            print("Información detallada del pago:")
            print(f"Número de Pago: {pago['numero_pago']}")
            print(f"Paciente: {pago['paciente']}")
            print(f"Método de Pago: {pago['metodo_pago']}")
            print(f"Monto: {pago['monto']}")
        else:
            print("No se encontró ningún pago con el número especificado.")
            
    def realizar_pago(self, pago:Pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles):
        """
        Asigna la tarea de realizar el pago al Slave_PagoCita.
        """
        # Se delega la operación 
        resultado_pago = self.slave_pago.realizar_pago(pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles)
        return resultado_pago

    def generar_recibo(self, numero_transaccion, paciente, concepto, monto, metodo_pago):
        """
        Asigna la tarea de generar el recibo al Slave_Recibo.
        """
        ruta_recibo = self.slave_recibo.generar_recibo(numero_transaccion, paciente, concepto, monto, metodo_pago)
        return ruta_recibo

    def imprimir_recibo(self, ruta_archivo_pdf):
        """
        Asigna la tarea de imprimir el recibo al Slave_Impresion.
        """
        self.slave_impresion.imprimir_recibo(ruta_archivo_pdf)

    def registrar_pago(self, info_pago):
        """
        Asigna la tarea de registrar el pago al Slave_AccionesPago.
        """
        self.slave_acciones_pago.registrar_pago(info_pago)

    def consultar_historial(self, fecha_inicio=None, fecha_fin=None, numero_pago=None):
        """
        Asigna la tarea de consultar el historial de pagos al Slave_AccionesPago.
        """
        return self.slave_acciones_pago.consultar_historial(fecha_inicio, fecha_fin, numero_pago)

    def buscar_pago(self, numero_pago):
        """
        Asigna la tarea de buscar un pago específico al Slave_AccionesPago.
        """
        return self.slave_acciones_pago.buscar_pago(numero_pago)