from django.contrib import admin
from .models import Material, Nota, Asistencia, Asistenciadocente

# Register your models here.

admin.site.register(Material)
admin.site.register(Nota)
admin.site.register(Asistencia)
admin.site.register(Asistenciadocente)