from .implementador_pago import *
import uuid
from pagos.models import Pago  # Asegúrate de importar el modelo Pago

class IPagoConPayPal(ImplementadorPago):
    
    
    def realizar_pago(self):
        print("Realizando pago con PayPal...")
        
        print("Pago realizado con PayPal.")
        
        return True
