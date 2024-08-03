from django.db import models
from usuarios.models import Usuarios

class Pagos(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    monto = models.FloatField()
    actividad = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.usuario}, {self.actividad}, {self.fecha}'

    class Meta:
        verbose_name = 'pago'
        verbose_name_plural = 'pagos'