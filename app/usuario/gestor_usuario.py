from autenticacion.models import CustomUser

class GestorUsuario:
    def __init__(self, builder):
        self._builder = builder

    def construir_usuario(self, username, password, email=None):

        # Aquí puedes agregar la lógica para construir el usuario utilizando el builder
        # Por ejemplo:
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email,
            user_type=self._builder.set_user_type()
        )

        user.save()


        # self._builder.set_username(username)
        # self._builder.set_password(password)
        # if email:
        #     self._builder.set_email(email)
        # self._builder.set_user_type()
        # user = self._builder.get_result()
        # user.save()
        # return user