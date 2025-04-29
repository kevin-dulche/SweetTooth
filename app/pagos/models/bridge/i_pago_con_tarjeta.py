from .implementador_pago import *
import uuid
from pagos.models import Pago  # Asegúrate de importar el modelo Pago

class IPagoConTarjeta(ImplementadorPago):
    
    
    def realizar_pago(self):
        print("Realizando pago con tarjeta...")

        print("Pago realizado con tarjeta.")
        return True

        
