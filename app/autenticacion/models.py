# autenticacion/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    RECEPCIONISTA = 'recepcionista'
    PACIENTE = 'paciente'
    ESPECIALISTA = 'especialista'
    ADMINISTRADOR = 'administrador'

    USER_TYPE_CHOICES = [
        (RECEPCIONISTA, 'Recepcionista'),
        (PACIENTE, 'Paciente'),
        (ESPECIALISTA, 'Especialista'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=ADMINISTRADOR,
    )

    # Hacer que el correo electrónico no sea obligatorio
    email = models.EmailField(unique=False, blank=True, null=True)

    def __str__(self):
        return self.username