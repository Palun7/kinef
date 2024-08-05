from django.db import models
from usuarios.models import Usuarios

class Dias(models.Model):
    dia = models.CharField(max_length=2)

    def __str__(self):
        return self.dia

    class Meta:
        verbose_name = 'Dia'
        verbose_name_plural = 'Dias'

class Horas(models.Model):
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

    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    mes = models.CharField(max_length=10, choices=Mes.choices)
    horas = models.IntegerField()
    dia = models.ManyToManyField(Dias)

    def __str__(self):
        return f'{self.usuario} - {self.horas}'

    def get_dia_str(self):
        return ' / '.join([dia.dia for dia in self.dia.all()])

    class Meta:
        verbose_name = 'Horas'
        verbose_name_plural = 'Horas'