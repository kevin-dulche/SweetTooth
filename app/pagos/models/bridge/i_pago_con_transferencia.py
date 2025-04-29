from .implementador_pago import *
from pagos.models import Pago  # Asegúrate de importar el modelo Pago

class IPagoConTransferencia(ImplementadorPago):
    

    
    def realizar_pago(self):
        print("Realizando pago con transferencia...")
        
        print("Pago realizado con transferencia.")
        
        return True
