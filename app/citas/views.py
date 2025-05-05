from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from citas.decorator.CitaBasica import CitaBasica
from citas.decorator.InfoPacienteDecorator import InfoPacienteDecorator
from citas.decorator.InfoMotivoDecorator import InfoMotivoDecorator
from .models import Cita

@login_required
def mis_citas(request):
    citas = Cita.objects.filter(paciente=request.user)

    citas_decoradas = []
    for cita in citas:
        cita_base = CitaBasica(cita)    
        cita_con_paciente = InfoPacienteDecorator(cita_base)
        cita_con_motivo = InfoMotivoDecorator(cita_con_paciente)

        citas_decoradas.append(cita_con_motivo.mostrar())

    return render(request, 'citas/mis_citas.html', {'citas': citas_decoradas})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Cita
from django.contrib.auth.decorators import login_required


@login_required
def modificar_cita(request):
    citas = Cita.objects.all()
    especialistas = CustomUser.objects.filter(user_type=CustomUser.ESPECIALISTA)

    if request.method == 'POST':
        cita_id = request.POST.get('cita_seleccionada')
        nueva_fecha = request.POST.get('nueva_fecha')
        nueva_hora = request.POST.get('nueva_hora')
        nuevo_tipo = request.POST.get('nuevo_tipo')
        nuevo_motivo = request.POST.get('nuevo_motivo')
        nuevo_especialista = request.POST.get('nuevo_especialista')

        cita = get_object_or_404(Cita, id=cita_id, paciente=request.user)

        if nueva_fecha:
            cita.fecha = nueva_fecha
        if nueva_hora:
            cita.hora = nueva_hora
        if nuevo_tipo:
            cita.tipo_cita = nuevo_tipo
        if nuevo_motivo:
            cita.motivo = nuevo_motivo
        if nuevo_especialista:
            cita.especialista = get_object_or_404(CustomUser, id=nuevo_especialista)

        cita.save()
        return redirect('gestor_citas')

    return render(request, 'citas/modificar_cita.html', {
        'citas': citas,
        'especialistas': especialistas,
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from servicios.abstractFactory.factories import obtener_fabrica # <-- Tu función para obtener la fábrica
from django.contrib.auth.decorators import login_required
from autenticacion.models import CustomUser

@login_required
def agendar_cita(request):
    pacientes = CustomUser.objects.filter(user_type=CustomUser.PACIENTE)
    especialistas = CustomUser.objects.filter(user_type=CustomUser.ESPECIALISTA)

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        especialista_id = request.POST.get('especialista')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        tipo_cita = request.POST.get('tipo_cita').lower()  # <- Minúscula para coincidir
        motivo = request.POST.get('motivo')

        paciente = get_object_or_404(CustomUser, id=paciente_id)
        especialista = get_object_or_404(CustomUser, id=especialista_id)

        # Obtener la fábrica correcta según el tipo de cita
        fabrica = obtener_fabrica(tipo_cita)

        # Crear la cita usando la fábrica
        cita = fabrica.crear_cita(paciente=paciente, fecha=fecha, hora=hora, motivo=motivo, especialista=especialista)

        cita.save()

        return redirect('gestor_citas')  # Redireccionas después de agendar

    return render(request, 'citas/agendar_cita.html', {
        'pacientes': pacientes,
        'especialistas': especialistas,
    })


@login_required
def eliminar_cita(request):
    citas = Cita.objects.all()

    if request.method == 'POST':
        cita_id = request.POST.get('cita_id')
        cita = get_object_or_404(Cita, id=cita_id)
        cita.delete()
        return redirect('eliminar_cita')  # Redireccionamos después de eliminar 

    return render(request, 'citas/eliminar_cita.html', {
        'citas': citas,
    })


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from servicios.abstractFactory.factories import obtener_fabrica
from autenticacion.models import CustomUser
from django.contrib import messages

@login_required
def agendar_propia_cita(request):
    especialistas = CustomUser.objects.filter(user_type=CustomUser.ESPECIALISTA)

    if request.method == 'POST':
        paciente = request.user  # Paciente autenticado
        especialista_id = request.POST.get('especialista')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        tipo_cita = request.POST.get('tipo_cita').lower()
        motivo = request.POST.get('motivo')

        especialista = get_object_or_404(CustomUser, id=especialista_id)

        try:
            fabrica = obtener_fabrica(tipo_cita)
            fabrica.crear_cita(
                paciente=paciente,
                especialista=especialista,
                fecha=fecha,
                hora=hora,
                motivo=motivo
            )
            messages.success(request, "Cita agendada exitosamente.")
            return redirect('mis_citas')  # Redirige a la vista de citas del paciente
        except ValueError as e:
            messages.error(request, f"Error: {str(e)}")

    return render(request, 'citas/agendar_propia_cita.html', {
        'especialistas': especialistas
    })


@login_required
def gestor_citas(request):
    return render(request, 'citas/gestor_citas.html')