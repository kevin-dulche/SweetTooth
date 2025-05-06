from autenticacion.models import CustomUser

class CustomUserBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._user = CustomUser()

    def set_username(self, username):
        self._user.username = username

    def set_password(self, password):
        self._user.set_password(password)  # Encriptar password

    def set_user_type(self, user_type):
        self._user.user_type = user_type

    def set_email(self, email):
        self._user.email = email

    def get_result(self):
        return self._user
