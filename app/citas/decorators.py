# Decorator Base
class ICitaDecorator:
    def mostrar(self):
        raise NotImplementedError

    def get_cita(self):
        raise NotImplementedError

# Componente Concreto
class CitaBasica(ICitaDecorator):
    def __init__(self, cita):
        self._cita = cita

    def mostrar(self):
        return f"Cita para {self._cita.fecha} a las {self._cita.hora} - Tipo: {self._cita.tipo_cita}"

    def get_cita(self):
        return self._cita

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
