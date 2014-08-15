from django.conf.urls import patterns, include, url
from .views import CursoView, HorarioView

urlpatterns = patterns('',

    url(r'^curso/$', CursoView.as_view(), name='nuevocurso'),
    url(r'^curso/(?P<id>[0-9]+)$', 'apps.mantenimiento.views.updatedeleteCurso', name='updatedeletecurso'),
    url(r'^horario/$', HorarioView.as_view(), name='nuevohorario'),

)
