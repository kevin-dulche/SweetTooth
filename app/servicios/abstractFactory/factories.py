from ..abstractFactory.FabricaCitaValoracion import FabricaCitaValoracion
from ..abstractFactory.FabricaCitaUrgencia import FabricaCitaUrgencia
from ..abstractFactory.FabricaCitaTratamiento import FabricaCitaTratamiento
from ..abstractFactory.FabricaCitaSeguimiento import FabricaCitaSeguimiento

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
