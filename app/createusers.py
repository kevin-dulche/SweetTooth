import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sweettooth.settings')  # <--- cámbialo
django.setup()

User = get_user_model()

username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin')

if not User.objects.filter(username=username).exists():
    print(f"⚡ Creando superusuario: {username}")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"✅ Superusuario {username} ya existe.")


from autenticacion.models import CustomUser

user = CustomUser.objects.create_user(
    username='Paciente1',               # Nombre de usuario
    password='Paciente1',    # Contraseña
    user_type=CustomUser.PACIENTE      # Tipo de usuario
)
user.save()
print(f"⚡ Creando usuario: {user.username}")


user = CustomUser.objects.create_user(
    username='Recepcionista1',               # Nombre de usuario
    password='Recepcionista1',    # Contraseña
    user_type=CustomUser.RECEPCIONISTA      # Tipo de usuario
)
user.save()
print(f"⚡ Creando usuario: {user.username}")

user = CustomUser.objects.create_user(
    username='Especialista1',               # Nombre de usuario
    password='Especialista1',    # Contraseña
    user_type=CustomUser.ESPECIALISTA      # Tipo de usuario
)
user.save()
print(f"⚡ Creando usuario: {user.username}")