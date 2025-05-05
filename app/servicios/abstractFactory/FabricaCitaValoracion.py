from .FabricaAbstractaCitas import FabricaAbstractaCitas
from citas.models import Cita

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