from django.db import models
from apps.negocio.models import Sesion
from apps.mantenimiento.models import Persona

# Create your models here.

class Material(models.Model):
	sesion = models.ForeignKey(Sesion)
	tipo = models.CharField(max_length=15)
	ubicacion = models.CharField(max_length=25)

class Nota(models.Model):
	alumno = models.OneToOneField(Persona)
	sesion = models.OneToOneField(Sesion)
	valor = models.FloatField()
	fecha = models.DateField()

class Asistencia(models.Model):
	alumno = models.OneToOneField(Persona)
	sesion = models.OneToOneField(Sesion)
	valor = models.CharField(max_length=15)
	fecha = models.DateField()

class Asistenciadocente(models.Model):
	docente = models.OneToOneField(Persona)
	sesion = models.OneToOneField(Sesion)
	valor = models.CharField(max_length=15)
	fecha = models.DateField()