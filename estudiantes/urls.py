from django.contrib import admin
from django.urls import include, path
from .views import ListarEstudiantes,NuevoEstudiante, ListarClubes, NuevoClub, consulta, EstudiantesList, EstudiantesList2

urlpatterns=[
    path('estudiantes/',ListarEstudiantes.as_view(),name='listarestudiantes'),
    path('estudiantes/prueba',consulta,name='consultajoin'),
    path('estudiantes/new',NuevoEstudiante.as_view(),name='insertarEstudiante'),
    path('clubes/',ListarClubes.as_view(),name='listarclubes'),
    path('clubes/new',NuevoClub.as_view(),name='insertarClub'),
    path('estudiantesjson/', EstudiantesList,name='listarestudiantes2'),
    path('estudiantesjson1/', EstudiantesList2.as_view(),name='listarestudiantes3'),
]