from pagos.models.adapter.pagar import Pagar
from .gestor_pago_medicamento import Gestor_PagoMedicamento
from pagos.models import Pago

class Adaptador_PagarMedicamento(Pagar):
    def __init__(self, pago:Pago, gestor_pago_medicamento:Gestor_PagoMedicamento):
        self.pago_medicamento = pago
        self.gestor = gestor_pago_medicamento
        
    
    def pagar(self):
        return self.gestor.pagar(self.pago_medicamento)