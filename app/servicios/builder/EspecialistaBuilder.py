from .CustomUserBuilder import CustomUserBuilder
from autenticacion.models import CustomUser

class EspecialistaBuilder(CustomUserBuilder):
    def set_user_type(self):
        return CustomUser.ESPECIALISTA