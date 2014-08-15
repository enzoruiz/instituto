from django.contrib import admin
from .models import Matricula, Sesion, Pago

# Register your models here.

admin.site.register(Matricula)
admin.site.register(Sesion)
admin.site.register(Pago)