from django.urls import path
from . import views

urlpatterns = [
    path('modificar_usuario/', views.modificar_usuario, name='modificar_usuario'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),
    path('notas_pacientes/', views.notas_pacientes, name='notas_pacientes'),
    path('mis_notas/', views.mis_notas, name='mis_notas'),
    path('gestion_usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
]
