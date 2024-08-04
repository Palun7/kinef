from django import forms
from .models import Pagos

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = ['usuario', 'monto', 'modo_pago', 'actividad', 'pase']