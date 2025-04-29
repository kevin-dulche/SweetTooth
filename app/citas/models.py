from django.db import models
from autenticacion.models import CustomUser

TIPO_CITA_CHOICES = [
    ('valoracion', 'Valoración'),
    ('urgencia', 'Urgencia'),
    ('tratamiento', 'Tratamiento'),
    ('seguimiento', 'Seguimiento'),
]

class Cita(models.Model):
    paciente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='citas_paciente')
    especialista = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='citas_especialista', null=True, blank=True)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_cita = models.CharField(max_length=50, choices=TIPO_CITA_CHOICES)
    motivo = models.TextField(blank=True, null=True)  # opcional: descripción del motivo de la cita

    def __str__(self):
        return f"{self.paciente.username} con {self.especialista.username} - {self.get_tipo_cita_display()} el {self.fecha} a las {self.hora}"

class HistorialClinico(models.Model):
    paciente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historial de {self.paciente.username} - {self.fecha_registro.strftime('%Y-%m-%d')}"
