# Clase que necesita ser adaptada: Pago de Medicamento
class PagoMedicamento:
    def __init__(self, medicamento, tratamiento):
        self.medicamento = medicamento
        self.tratamiento = tratamiento
    
    def procesar_pago(self):
        return f"Pago procesado para medicamento: {self.medicamento}, tratamiento: {self.tratamiento}."