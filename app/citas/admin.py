from django.contrib import admin

# Register your models here.

from .models import Cita, HistorialClinico

admin.site.register(Cita)
admin.site.register(HistorialClinico)