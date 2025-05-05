# Decorator Base
class ICitaDecorator:
    def mostrar(self):
        raise NotImplementedError

    def get_cita(self):
        raise NotImplementedError