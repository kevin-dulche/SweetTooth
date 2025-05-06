from abc import ABC, abstractmethod

# Interfaz común
class Pagar(ABC):
    @abstractmethod
    def pagar(self):
        pass