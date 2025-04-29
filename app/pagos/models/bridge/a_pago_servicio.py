from .abstraccion_pago import Abstraccion_Pago
from .implementador_pago import *


class APago_Servicio(Abstraccion_Pago):
    
    __implementador_pago:ImplementadorPago
    
    
    def __init__(self, implementador_pago:ImplementadorPago):
        self.__implementador_pago = implementador_pago
        
    def procesar_pago(self):
        return self.__implementador_pago.realizar_pago()
        
        

    
