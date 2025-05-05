from .ICitaDecorator import ICitaDecorator

# Componente Concreto
class CitaBasica(ICitaDecorator):
    def __init__(self, cita):
        self._cita = cita

    def mostrar(self):
        return f"Cita para {self._cita.fecha} a las {self._cita.hora} - Tipo: {self._cita.tipo_cita}"

    def get_cita(self):
        return self._cita