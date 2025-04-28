from .builders import PacienteBuilder, EspecialistaBuilder, RecepcionistaBuilder, AdministradorBuilder
from .gestor_usuario import GestorUsuario
from autenticacion.models import CustomUser

class ControladorUsuarios:

    def crear_paciente(self, username, password, email=None):
        builder = PacienteBuilder()
        gestor = GestorUsuario(builder)
        return gestor.construir_usuario(username, password, email)

    def crear_especialista(self, username, password, email=None):
        builder = EspecialistaBuilder()
        gestor = GestorUsuario(builder)
        return gestor.construir_usuario(username, password, email)

    def crear_recepcionista(self, username, password, email=None):
        builder = RecepcionistaBuilder()
        gestor = GestorUsuario(builder)
        return gestor.construir_usuario(username, password, email)

    def crear_administrador(self, username, password, email=None):
        builder = AdministradorBuilder()
        print(builder.set_user_type())
        gestor = GestorUsuario(builder)
        return gestor.construir_usuario(username, password, email)

    # NUEVOS MÉTODOS:

    def listar_usuarios(self):
        return CustomUser.objects.all()

    def obtener_usuario_por_id(self, user_id):
        return CustomUser.objects.get(id=user_id)

    def modificar_usuario(self, user_id, nuevo_tipo=None, nuevo_correo=None, nueva_contrasena=None):
        usuario = CustomUser.objects.get(id=user_id)

        if nuevo_tipo:
            usuario.user_type = nuevo_tipo
        if nuevo_correo:
            usuario.email = nuevo_correo
        if nueva_contrasena:
            usuario.set_password(nueva_contrasena)

        usuario.save()
        return usuario

    def eliminar_usuario(self, user_id):
        usuario = CustomUser.objects.get(id=user_id)
        usuario.delete()
        return True
