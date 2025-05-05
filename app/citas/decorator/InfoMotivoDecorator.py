from .ICitaDecorator import ICitaDecorator

# Decorador para agregar información del motivo de la cita
class InfoMotivoDecorator(ICitaDecorator):
    def __init__(self, cita_decorator):
        self._cita_decorator = cita_decorator

    def mostrar(self):
        info_base = self._cita_decorator.mostrar()
        motivo_info = f" - Motivo: {self._cita_decorator.get_cita().motivo}"
        return info_base + motivo_info

    def get_cita(self):
        return self._cita_decorator.get_cita()