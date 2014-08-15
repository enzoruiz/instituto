from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form

@dajaxice_register
def miajaxprueba(request):
    return simplejson.dumps({'message':'Hello from Python!'})

# @dajaxice_register
# def registrarCurso(request, form):
# 	dajax = Dajax()
# 	form = CursoForm(deserialize_form(form))

# 	if form.is_valid():
# 		form.save()

# 	else:
# 		form.
