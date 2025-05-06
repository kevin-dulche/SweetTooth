from .CustomUserBuilder import CustomUserBuilder
from autenticacion.models import CustomUser

class PacienteBuilder(CustomUserBuilder):
    def set_user_type(self):
        return CustomUser.PACIENTE