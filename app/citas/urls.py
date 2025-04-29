from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar_cita, name='agendar_cita'),
    path('modificar/', views.modificar_cita, name='modificar_cita'),
    path('eliminar/', views.eliminar_cita, name='eliminar_cita'),
    path('mis_citas/', views.mis_citas, name='mis_citas'),
    path('citas/agendar-propia/', views.agendar_propia_cita, name='agendar_propia_cita'),
    path('citas/', views.gestor_citas, name='gestor_citas'),
]
