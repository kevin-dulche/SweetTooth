from abc import ABC, abstractmethod

class ImplementadorPago(ABC):
    @abstractmethod
    def realizar_pago(self):
        pass
