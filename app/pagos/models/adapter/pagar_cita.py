from pagos.models.master_slave.Master_PagoDeCita import Master_PagoDeCita
from pagos.models.adapter.pagar import Pagar
from pagos.models import Pago

class PagarCita(Pagar):
    def __init__(self, pago:Pago, nombre_paciente, id_pago, metodo_pago, monto_pago, tipo_tarjeta, numero_tarjeta, fecha_expiracion, cvv, correo_paypal, detalles):
        self.pago = pago
        self.nombre_paciente = nombre_paciente
        self.id_pago = id_pago
        self.metodo_pago = metodo_pago
        self.monto_pago = monto_pago
        self.tipo_tarjeta = tipo_tarjeta
        self.numero_tarjeta = numero_tarjeta
        self.fecha_expiracion = fecha_expiracion
        self.cvv = cvv
        self.correo_paypal = correo_paypal
        self.detalles = detalles
        self.master_pago = Master_PagoDeCita()

    
    def pagar(self):
        return self.master_pago.procesar_pago(self.pago, self.nombre_paciente, self.id_pago, self.metodo_pago, self.monto_pago, self.tipo_tarjeta, self.numero_tarjeta, self.fecha_expiracion, self.cvv, self.correo_paypal, self.detalles)
