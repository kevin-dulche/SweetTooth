from django.db import models
from autenticacion.models import CustomUser

# Create your models here.

class NotaMedica(models.Model):
    paciente = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    texto = models.TextField(blank=True)

    def __str__(self):
        return f"Nota de {self.paciente.username}"
