from .CustomUserBuilder import CustomUserBuilder
from autenticacion.models import CustomUser

class AdministradorBuilder(CustomUserBuilder):
    def set_user_type(self):
        return CustomUser.ADMINISTRADOR