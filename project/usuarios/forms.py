from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuarios

class CustomUserCreationForm(UserCreationForm):
    dni = forms.CharField(max_length=8, required=True)
    fecha_nacimiento = forms.DateField(required=True)
    telefono = forms.CharField(max_length=15, required=True)
    domicilio = forms.CharField(max_length=150, required=True)
    instagram = forms.CharField(max_length=150, required=False)
    foto = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'dni', 'fecha_nacimiento', 'telefono', 'domicilio', 'instagram', 'foto', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Usuarios.objects.create(
                user=user,
                dni=self.cleaned_data['dni'],
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                telefono=self.cleaned_data['telefono'],
                domicilio=self.cleaned_data['domicilio'],
                instagram=self.cleaned_data['instagram'],
                foto=self.cleaned_data.get('foto'),
            )
        return user

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model= User
        fields = ['username', 'password']