from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'id_pago', 'id_servicio', 'id_paciente', 'nombre_paciente',
            'tipo_tratamiento', 'descripcion_tratamiento', 
            'especialista_responsable', 'fecha_pago', 'monto_pago', 
            'metodo_pago'
        ]
        widgets = {
            'id_pago': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'id_servicio': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'id_paciente': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'nombre_paciente': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'tipo_tratamiento': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'descripcion_tratamiento': forms.Textarea(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'especialista_responsable': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'fecha_pago': forms.DateInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'monto_pago': forms.NumberInput(attrs={'readonly': 'readonly', 'class': 'readonly'}),
            'metodo_pago': forms.Select(attrs={'disabled': 'disabled', 'required': True}),
        }
