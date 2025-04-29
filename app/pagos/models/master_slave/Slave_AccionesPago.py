# Slave_AccionesPago.py
import datetime

class Slave_AccionesPago:
    historial_pagos = []
    contador_pagos = 0

    def registrar_pago(self, info_pago):
        """
        Permite registrar el pago realizado de una cita médica.
        """
        Slave_AccionesPago.contador_pagos += 1
        info_pago['numero_pago'] = f"PAGO-{Slave_AccionesPago.contador_pagos:03d}"
        Slave_AccionesPago.historial_pagos.append(info_pago)
        print(f"Pago registrado con número: {info_pago['numero_pago']}")

    def consultar_historial(self, fecha_inicio=None, fecha_fin=None, numero_pago=None):
        """
        Permite al usuario visualizar los pagos realizados por fecha o número de pago.
        """
        resultados = []
        if numero_pago:
            for pago in Slave_AccionesPago.historial_pagos:
                if pago.get('numero_pago') == numero_pago:
                    resultados.append(pago)
            return resultados
        elif fecha_inicio and fecha_fin:
            try:
                inicio = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                fin = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d").date()
                for pago in Slave_AccionesPago.historial_pagos:
                    fecha_pago_obj = datetime.datetime.strptime(pago.get('fecha_pago'), "%Y-%m-%d").date()
                    if inicio <= fecha_pago_obj <= fin:
                        resultados.append(pago)
                return resultados
            except ValueError:
                print("Error: Formato de fecha incorrecto (YYYY-MM-DD).")
                return []
        else:
            return Slave_AccionesPago.historial_pagos

    def buscar_pago(self, numero_pago):
        """
        Permite al usuario visualizar la información detallada de un pago registrado.
        """
        for pago in Slave_AccionesPago.historial_pagos:
            if pago.get('numero_pago') == numero_pago:
                return pago
        return None