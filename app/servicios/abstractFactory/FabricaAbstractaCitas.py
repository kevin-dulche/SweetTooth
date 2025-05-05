# Fábrica Abstracta
class FabricaAbstractaCitas:
    def crear_cita(self, paciente, fecha, hora, motivo, especialista):
        raise NotImplementedError("Este método debe ser implementado por las fábricas concretas.")