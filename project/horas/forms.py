from django import forms
from .models import Horas, Dias

class HorasForm(forms.ModelForm):
    dia = forms.ModelMultipleChoiceField(queryset=Dias.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Horas
        fields = '__all__'