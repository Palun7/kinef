from django.db import models
from django.contrib.auth.models import User


class Gastos(models.Model):

    class FijoVariable(models.TextChoices):
        FIJO = 'fijo', 'Fijo'
        VARIABLE = 'variable', 'Variable'

    class Mes(models.TextChoices):
        ENERO = 'Enero', 'Enero'
        FEBRERO = 'Febrero', 'Febrero'
        MARZO = 'Marzo', 'Marzo'
        ABRIL = 'Abril', 'Abril'
        MAYO = 'Mayo', 'Mayo'
        JUNIO = 'Junio', 'Junio'
        JULIO = 'Julio', 'Julio'
        AGOSTO = 'Agosto', 'Agosto'
        SEPTIEMBRE = 'Septiembre', 'Septiembre'
        OCTUBRE = 'Octubre', 'Octubre'
        NOVIEMBRE = 'Noviembre', 'Noviembre'
        DICIEMBRE = 'Diciembre', 'Diciembre'

    mes = models.CharField(max_length=10, choices=Mes.choices, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    concepto = models.CharField(max_length=200)
    monto = models.FloatField()
    fijo_variable = models.CharField(max_length=8, choices=FijoVariable.choices, verbose_name='Fijo o Variable')
    fecha_pago = models.DateField()

    def __str__(self):
        return f'{self.concepto}- ${self.monto}, {self.fijo_variable} - {self.fecha_pago}'
