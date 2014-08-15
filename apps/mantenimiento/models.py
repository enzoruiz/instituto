from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
	nombre = models.CharField(max_length=45)
	descripcion = models.CharField(max_length=140, blank=True)
	estado = models.CharField(max_length=1, default=1)

	def __str__(self):
		return self.nombre

class Persona(models.Model):
	user = models.OneToOneField(User)
	dni = models.CharField(max_length=8)
	telefono = models.CharField(max_length=15, blank=True)
	celular = models.CharField(max_length=15, blank=True)
	direccion = models.CharField(max_length=140, blank=True)
	tipo = models.CharField(max_length=15)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.dni

class Horario(models.Model):
	docente = models.ForeignKey(Persona)
	curso = models.ForeignKey(Curso)
	fechainicio = models.DateField()
	fechafin = models.DateField()
	dias = models.CharField(max_length=140)
	ambiente = models.CharField(max_length=140)
	horainicio = models.CharField(max_length=5)
	horafin = models.CharField(max_length=5)
	duracion = models.IntegerField()
	costo = models.FloatField()
	fechas = models.CharField(max_length=500)
	cuposminimo = models.IntegerField()
	cuposmaximo = models.IntegerField()
	estado = models.CharField(max_length=1, default=1)

	def __str__(self):
		return self.docente.user.first_name + ' ' + self.docente.user.last_name + ' - ' + self.curso.nombre