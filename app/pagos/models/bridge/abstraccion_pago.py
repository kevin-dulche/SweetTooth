from abc import ABC, abstractmethod

class Abstraccion_Pago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass
