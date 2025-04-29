from django.db import models
import datetime

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_servicio = models.IntegerField(default=0)
    id_paciente = models.IntegerField(default=0)
    nombre_paciente = models.CharField(max_length=200, default='')
    tipo_tratamiento = models.CharField(max_length=100, default='')
    descripcion_tratamiento = models.TextField(default='')
    especialista_responsable = models.CharField(max_length=100, default='')
    fecha_pago = models.DateField(default=datetime.date.today)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metodo_pago = models.CharField(max_length=50, default='')
    estado_pago = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"Pago ID {self.id_pago} - {self.nombre_paciente} - ${self.monto_pago}"

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
