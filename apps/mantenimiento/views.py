from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CursoForm, HorarioForm
from .models import Curso, Horario, Persona
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
import datetime

# Create your views here.

class CursoView(TemplateView):
	
	def get(self, request, *args, **kwargs):
		form = CursoForm()
		cursos = Curso.objects.all()
		return render(request, 'mantenimiento/curso.html', { 'form' : form, 'cursos' : cursos})

	def post(self, request, *args, **kwargs):
		valores = {}
		form = CursoForm(request.POST)
		# to_json = {}
		idCurso = request.POST['idCurso']
		if idCurso != '':
			if form.is_valid():
				curso = Curso.objects.get(id=idCurso)
				curso.nombre = request.POST['nombre']
				curso.descripcion = request.POST['descripcion']
				curso.save()
				cursos = Curso.objects.all()
				nuevoForm = CursoForm()
				valores['form'] = nuevoForm
				valores['cursos'] = cursos
			else:
				cursos = Curso.objects.all()
				valores['form'] = form
				valores['cursos'] = cursos
		else:
			if form.is_valid():
				form.save()
				# to_json['mensaje'] = 'Pepe el pollo'
				cursos = Curso.objects.all()
				# data = serializers.serialize('json', cursos, fields=('nombre',))

				# return HttpResponse(data, mimetype='application/json')
				nuevoForm = CursoForm()
				valores['form'] = nuevoForm
				valores['cursos'] = cursos
			else:
				cursos = Curso.objects.all()
				valores['cursos'] = cursos
				valores['form'] = form

		return render(request, 'mantenimiento/curso.html', valores)

def updatedeleteCurso(request, id):
	if request.POST:
		tipo = request.POST['tipo']
		if tipo == 'Editar':
			curso = Curso.objects.filter(id=id)
			data = serializers.serialize('json', curso, fields=('nombre', 'descripcion'))
		if tipo == 'Eliminar':
			Curso.objects.get(id=id).delete()
			cursos = Curso.objects.all()
			data = serializers.serialize('json', cursos, fields=('nombre', 'descripcion'))
		
		return HttpResponse(data, content_type='application/json')
	else:
		return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
		
class HorarioView(TemplateView):

	def obtenerCamposExtras(self, fechas):
		camposextra = {}
		diasClase = ""
		dias = {1 : 'Lunes', 2 : 'Martes', 3 : 'Miercoles', 4 : 'Jueves', 5 : 'Viernes', 6 : 'Sabado', 7 : 'Domingo'}
		cantidad = len(fechas.split(','))
		listaFechas = fechas.split(',')

		for idx, val in enumerate(listaFechas):
			valor = datetime.datetime.strptime(str(val), '%d/%m/%Y').date()
			numero = valor.isoweekday()
			dia = dias[numero]
			if dia in diasClase:
				pass
			else:
				diasClase += dia + '-'

		diasClase = diasClase.rstrip('-')
		camposextra['fechainicio'] = datetime.datetime.strptime(listaFechas[0], '%d/%m/%Y').date()
		camposextra['fechafin'] = datetime.datetime.strptime(listaFechas[cantidad - 1], '%d/%m/%Y').date()
		camposextra['dias'] = diasClase
		camposextra['duracion'] = cantidad
		return camposextra
	
	def get(self, request, *args, **kwargs):
		form = HorarioForm()
		horarios = Horario.objects.all()
		return render(request, 'mantenimiento/horario.html', { 'form' : form, 'horarios' : horarios })

	def post(self, request, *args, **kwargs):
		valores = {}
		fechas = request.POST['fechas']
		form = HorarioForm(request.POST)
		
		camposextra = self.obtenerCamposExtras(fechas)

		if form.is_valid():
			horario = Horario()
			horario.docente = Persona.objects.get(id=request.POST['docente'])
			horario.curso = Curso.objects.get(id=request.POST['curso'])
			horario.fechainicio = camposextra['fechainicio']
			horario.fechafin = camposextra['fechafin']
			horario.dias = camposextra['dias']
			horario.ambiente = request.POST['ambiente']
			horario.horainicio = request.POST['horaInicio']
			horario.horafin = request.POST['horaFin']
			horario.duracion = camposextra['duracion']
			horario.costo = request.POST['costo']
			horario.fechas = request.POST['fechas']
			horario.cuposminimo = request.POST['cuposmaximo']
			horario.cuposmaximo = request.POST['cuposminimo']
			horario.save()
			horarios = Horario.objects.all()
			nuevoForm = HorarioForm()
			valores['form'] = nuevoForm
			valores['horarios'] = horarios
		else:
			horarios = Horario.objects.all()
			valores['form'] = form
			valores['horarios'] = horarios
		
		return render(request, 'mantenimiento/curso.html', valores)