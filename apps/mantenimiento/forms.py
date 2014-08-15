from django.forms import ModelForm
from .models import Curso, Horario

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion')
    
class HorarioForm(ModelForm):
	class Meta:
		model = Horario
		fields = ('docente', 'curso', 'ambiente', 'costo', 'cuposminimo', 'cuposmaximo')
		labels = {
			'cuposminimo' : 'Cupos Minimo',
			'cuposmaximo' : 'Cupos Maximo',
		}