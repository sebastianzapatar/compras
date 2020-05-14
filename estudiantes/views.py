from django.shortcuts import render
from django.views import generic
from .models import Estudiante, ClubDeportivo
from django.urls import reverse_lazy
from estudiantes.forms import EstudianteForm, ClubForm
# Create your views here.
class ListarEstudiantes(generic.ListView):
    model=Estudiante
    template_name="estudiantes/estudiantes_list.html"
    context_object_name="obj"
class NuevoEstudiante(generic.CreateView):
    model=Estudiante
    template_name="estudiantes/estudiante_form.html"
    context_object_name="obj"
    form_class=EstudianteForm
    success_url=reverse_lazy("estudiantes:listarestudiantes")
class ListarClubes(generic.ListView):
    model=ClubDeportivo
    template_name="estudiantes/clubes_list.html"
    context_object_name="obj"
class NuevoClub(generic.CreateView):
    model=ClubDeportivo
    template_name="estudiantes/club_form.html"
    context_object_name="obj"
    form_class=ClubForm
    success_url=reverse_lazy("estudiantes:listarclubes")