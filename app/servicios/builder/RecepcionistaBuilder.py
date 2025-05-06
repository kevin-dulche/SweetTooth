from .CustomUserBuilder import CustomUserBuilder
from autenticacion.models import CustomUser

class RecepcionistaBuilder(CustomUserBuilder):
    def set_user_type(self):
        return CustomUser.RECEPCIONISTA