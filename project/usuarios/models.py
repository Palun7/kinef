from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'