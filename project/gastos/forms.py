from django import forms
from .models import Gastos

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = ['mes', 'concepto', 'monto', 'monto', 'fijo_variable', 'fecha_pago']
