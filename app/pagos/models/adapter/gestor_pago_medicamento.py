from pagos.models import Pago

#Clase auxiliar para verificar disponibilidad de medicamentos
class Gestor_PagoMedicamento:
    def __init__(self):
        pass
        
    
    def pagar(self, pago:Pago):
        pago.estado_pago = "Pagado"
        return pago.save()