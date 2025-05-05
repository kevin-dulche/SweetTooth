from .ICitaDecorator import ICitaDecorator

# Decorador para agregar información del paciente
class InfoPacienteDecorator(ICitaDecorator):
    def __init__(self, cita_decorator):
        self._cita_decorator = cita_decorator

    def mostrar(self):
        info_base = self._cita_decorator.mostrar()
        paciente_info = f" - Paciente: {self._cita_decorator.get_cita().paciente.username}"
        return info_base + paciente_info

    def get_cita(self):
        return self._cita_decorator.get_cita()