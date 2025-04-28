from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .controlador_usuarios import ControladorUsuarios
from autenticacion.models import CustomUser

# Create your views here.

controlador = ControladorUsuarios()

@login_required
def gestion_usuarios(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'usuario/gestion_usuarios.html', {'usuarios': usuarios})

@login_required
def agregar_usuario(request):
    if request.method == 'POST':
        print("Ingreso a agregar usuario")
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        tipo_usuario = request.POST.get('tipo_usuario')

        print("Tipo de usuario:", tipo_usuario)

        if tipo_usuario == 'Paciente':
            controlador.crear_paciente(nombre, contrasena, correo)
        elif tipo_usuario == 'Especialista':
            controlador.crear_especialista(nombre, contrasena, correo)
        elif tipo_usuario == 'Recepcionista':
            controlador.crear_recepcionista(nombre, contrasena, correo)
        elif tipo_usuario == 'Administrador':
            print("Ingreso a crear administrador")
            controlador.crear_administrador(nombre, contrasena, correo)

        return redirect('gestion_usuarios')
    else:
        return render(request, 'usuario/agregar_usuario.html')



@login_required
def modificar_usuario(request):
    if request.method == 'POST':
        user_id = request.POST.get('usuario_seleccionado')
        nuevo_tipo = request.POST.get('nuevo_tipo')
        nuevo_correo = request.POST.get('nuevo_correo')
        nueva_contrasena = request.POST.get('nueva_contrasena')

        usuario = get_object_or_404(CustomUser, id=user_id)

        if nuevo_tipo:
            usuario.user_type = nuevo_tipo
        if nuevo_correo:
            usuario.email = nuevo_correo
        if nueva_contrasena:
            usuario.set_password(nueva_contrasena)

        usuario.save()

        return redirect('gestion_usuarios')
    
    usuarios = CustomUser.objects.all()
    return render(request, 'usuario/modificar_usuario.html', {'usuarios': usuarios})

@login_required
def eliminar_usuario(request):
    if request.method == 'POST':
        user_id = request.POST.get('usuario_eliminar')
        usuario = get_object_or_404(CustomUser, id=user_id)
        usuario.delete()
        return redirect('gestion_usuarios')
    
    usuarios = CustomUser.objects.all()
    return render(request, 'usuario/eliminar_usuario.html', {'usuarios': usuarios})

@login_required
def mostrar_informacion_usuario(request):
    if request.user.user_type == CustomUser.PACIENTE:
        return render(request, 'mis_notas.html')
    else:
        return render(request, 'usuario/notas_pacientes.html')


from django.shortcuts import render, redirect, get_object_or_404
from autenticacion.models import CustomUser
from .models import NotaMedica  # O donde guardes las notas

@login_required
def notas_pacientes(request):
    pacientes = CustomUser.objects.filter(user_type=CustomUser.PACIENTE)
    nota_actual = ""
    paciente_seleccionado_id = None

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente_seleccionado')
        nota_texto = request.POST.get('nota_paciente')
        
        paciente = get_object_or_404(CustomUser, id=paciente_id)

        # Guarda o actualiza la nota
        nota, created = NotaMedica.objects.get_or_create(paciente=paciente)
        nota.texto = nota_texto
        nota.save()

        paciente_seleccionado_id = paciente.id
        nota_actual = nota.texto

    else:  # <-- Cuando sea GET
        if pacientes.exists():
            primer_paciente = pacientes.first()
            paciente_seleccionado_id = primer_paciente.id
            try:
                nota = NotaMedica.objects.get(paciente=primer_paciente)
                nota_actual = nota.texto
            except NotaMedica.DoesNotExist:
                nota_actual = ""

    return render(request, 'usuario/notas_pacientes.html', {
        'pacientes': pacientes,
        'nota_actual': nota_actual,
        'paciente_seleccionado_id': paciente_seleccionado_id,
    })


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import NotaMedica

@login_required
def mis_notas(request):
    paciente = request.user

    try:
        nota = NotaMedica.objects.get(paciente=paciente)
        nota_actual = nota.texto
    except NotaMedica.DoesNotExist:
        nota_actual = "No tienes notas médicas registradas."

    return render(request, 'usuario/mis_notas.html', {
        'nota_actual': nota_actual,
    })
