from .models import Cita

# Fábrica Abstracta
class FabricaAbstractaCitas:
    def crear_cita(self, paciente, fecha, hora, motivo, especialista):
        raise NotImplementedError("Este método debe ser implementado por las fábricas concretas.")

# Fábricas concretas
class FabricaCitaValoracion(FabricaAbstractaCitas):
    def crear_cita(self, paciente, especialista, fecha, hora, motivo):
        return Cita.objects.create(
            paciente=paciente,
            especialista=especialista,
            fecha=fecha,
            hora=hora,
            tipo_cita='valoracion',
            motivo=motivo
        )

class FabricaCitaUrgencia(FabricaAbstractaCitas):
    def crear_cita(self, paciente, especialista, fecha, hora, motivo):
        return Cita.objects.create(
            paciente=paciente,
            especialista=especialista,
            fecha=fecha,
            hora=hora,
            tipo_cita='urgencia',
            motivo=motivo
        )

class FabricaCitaTratamiento(FabricaAbstractaCitas):
    def crear_cita(self, paciente, especialista, fecha, hora, motivo):
        return Cita.objects.create(
            paciente=paciente,
            especialista=especialista,
            fecha=fecha,
            hora=hora,
            tipo_cita='tratamiento',
            motivo=motivo
        )

class FabricaCitaSeguimiento(FabricaAbstractaCitas):
    def crear_cita(self, paciente, especialista, fecha, hora, motivo):
        return Cita.objects.create(
            paciente=paciente,
            especialista=especialista,
            fecha=fecha,
            hora=hora,
            tipo_cita='seguimiento',
            motivo=motivo
        )

# Función de ayuda para escoger la fábrica adecuada
def obtener_fabrica(tipo_cita):
    if tipo_cita == 'valoracion':
        return FabricaCitaValoracion()
    elif tipo_cita == 'urgencia':
        return FabricaCitaUrgencia()
    elif tipo_cita == 'tratamiento':
        return FabricaCitaTratamiento()
    elif tipo_cita == 'seguimiento':
        return FabricaCitaSeguimiento()
    else:
        raise ValueError("Tipo de cita no válido")
