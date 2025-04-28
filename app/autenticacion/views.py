from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.contrib.auth import logout
# Create your views here.

# autenticacion/views.py
def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirigir según el tipo de usuario
            if user.user_type == 'recepcionista':
                return redirect('recepcionista_dashboard')  # Vista para recepcionista
            elif user.user_type == 'paciente':
                return redirect('paciente_dashboard')  # Vista para paciente
            elif user.user_type == 'especialista':
                return redirect('especialista_dashboard')  # Vista para especialista
        else:
            # Si el formulario no es válido, muestra un mensaje de error
            return render(request, 'autenticacion/login.html', {'form': form, 'error_message': 'Usuario o contraseña incorrectos'})

    else:
        form = AuthenticationForm()
    
    return render(request, 'autenticacion/login.html', {'form': form})


# autenticacion/views.py
from django.shortcuts import render

def is_recepcionista(user):
    return user.user_type == 'recepcionista'

def is_paciente(user):
    return user.user_type == 'paciente'

def is_especialista(user):
    return user.user_type == 'especialista'

def recepcionista_dashboard(request):
    if not is_recepcionista(request.user):
        form = AuthenticationForm()
        return render(request, 'autenticacion/login.html', {'form': form, 'error_message': 'No tienes permiso para acceder a esta página. Solo los recepcionistas pueden verlo.'})
    current_time = timezone.now().strftime("%d/%m/%Y - %I:%M %p")  # Formato: 25/04/2025 - 11:15 p.m.
    return render(request, 'autenticacion/recepcionista_dashboard.html', {'current_time': current_time})

def paciente_dashboard(request):
    if not is_paciente(request.user):
        form = AuthenticationForm()
        return render(request, 'autenticacion/login.html', {'form': form, 'error_message': 'No tienes permiso para acceder a esta página. Solo los pacientes pueden verlo.'})
    
    current_time = timezone.now().strftime("%d/%m/%Y - %I:%M %p")  # Formato: 25/04/2025 - 11:15 p.m.
    return render(request, 'autenticacion/paciente_dashboard.html', {'current_time': current_time})

def especialista_dashboard(request):
    if not is_especialista(request.user):
        form = AuthenticationForm()
        return render(request, 'autenticacion/login.html', {'form': form, 'error_message': 'No tienes permiso para acceder a esta página. Solo los especialistas pueden verlo.'})
    current_time = timezone.now().strftime("%d/%m/%Y - %I:%M %p")  # Formato: 25/04/2025 - 11:15 p.m.
    return render(request, 'autenticacion/especialista_dashboard.html', {'current_time': current_time})

def logout_view(request):
    logout(request)
    return redirect('login')