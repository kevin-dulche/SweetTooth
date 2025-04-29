import datetime
import uuid
from pagos.models.bridge.i_pago_con_tarjeta import IPagoConTarjeta
from pagos.models.bridge.i_pago_con_paypal import IPagoConPayPal
from pagos.models.bridge.i_pago_con_transferencia import IPagoConTransferencia
from pagos.models.bridge.a_pago_servicio import APago_Servicio
from pagos.models import Pago  # Asegúrate de importar el modelo Pago

class Slave_PagoCita:
    def realizar_pago(self, pago:Pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles):
        """
        Permite al usuario realizar el pago de una cita médica.
        """
        numero_transaccion = str(uuid.uuid4())  # Generar un número de transacción único
        fecha_pago = datetime.date.today().isoformat()


        # Simulación de la lógica de procesamiento de pagos
        if metodo_pago == "tarjeta":
            tarjeta_pago = IPagoConTarjeta()
            abstraccion_pago = APago_Servicio(tarjeta_pago)
            return abstraccion_pago.procesar_pago()
        elif metodo_pago == "Transferencia":
            transferencia_pago = IPagoConTransferencia()
            abstraccion_pago = APago_Servicio(transferencia_pago)
            return abstraccion_pago.procesar_pago()
        elif metodo_pago == "paypal":
            paypal_pago = IPagoConPayPal()
            abstraccion_pago = APago_Servicio(paypal_pago)
            return abstraccion_pago.procesar_pago()