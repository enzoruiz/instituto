from django.db import models
from apps.mantenimiento.models import Persona, Horario

# Create your models here.

class Matricula(models.Model):
	alumno = models.ForeignKey(Persona)
	horario = models.ForeignKey(Horario)
	fecha = models.DateField()
	tipo = models.CharField(max_length=1)
	descuento = models.FloatField()
	observacion = models.CharField(max_length=140)
	estado = models.CharField(max_length=1)

	def __str__(self):
		return self.alumno.user.first_name + ' ' + self.alumno.user.last_name + ' - ' + self.horario.curso.nombre

class Sesion(models.Model):
	horario = models.ForeignKey(Horario)
	fechaprogramada = models.DateField()
	titulo = models.CharField(max_length=140)
	descripcion = models.CharField(max_length=140)
	estado = models.CharField(max_length=1)

	def __str__(self):
		return self.horario.curso.nombre + ' - ' + self.titulo

class Pago(models.Model):
	matricula = models.ForeignKey(Matricula)
	monto = models.FloatField()
	numerovoucher = models.CharField(max_length=25)
	fecha = models.DateField()
	observacion = models.CharField(max_length=140)