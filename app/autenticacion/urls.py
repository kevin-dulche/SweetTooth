# autenticacion/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.custom_login, name='login'),
    path('recepcionista_dashboard/', views.recepcionista_dashboard, name='recepcionista_dashboard'),
    path('paciente_dashboard/', views.paciente_dashboard, name='paciente_dashboard'),
    path('especialista_dashboard/', views.especialista_dashboard, name='especialista_dashboard'),
    path('logout/', LogoutView.as_view(next_page=''), name='logout')
]
