from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Estudiante, ClubDeportivo
from django.urls import reverse_lazy
from estudiantes.forms import EstudianteForm, ClubForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EsutianteSerializado
# Create your views here.
class ListarEstudiantes(LoginRequiredMixin,generic.ListView):
    model=Estudiante
    template_name="estudiantes/estudiantes_list.html"
    context_object_name="obj"
    login_url="home:login"
class NuevoEstudiante(LoginRequiredMixin,generic.CreateView):
    model=Estudiante
    template_name="estudiantes/estudiante_form.html"
    context_object_name="obj"
    form_class=EstudianteForm
    success_url=reverse_lazy("estudiantes:listarestudiantes")
    login_url="home:login"
class ListarClubes(LoginRequiredMixin,generic.ListView):
    model=ClubDeportivo
    template_name="estudiantes/clubes_list.html"
    context_object_name="obj"
    login_url="home:login"
class NuevoClub(LoginRequiredMixin,generic.CreateView):
    model=ClubDeportivo
    template_name="estudiantes/club_form.html"
    context_object_name="obj"
    form_class=ClubForm
    success_url=reverse_lazy("estudiantes:listarclubes")
    login_url="home:login"
def consulta(request):
    from django.db import connection
    with connection.cursor as cursor:
        cursor.execute("select * from estudiantes_estudiante as e join estudiantes_clubdeportivo as c on e.id=c.estudiante_id")
        rawData=cursor.fetchall()
        result=[]
        for r in rawData:
            result.append(list(r))
        contexto={"obj",result}
    return render(request,'estudiantes/consulta.html',contexto)
def EstudiantesList(request):
    MAX_OBJECTS = 200
    est = Estudiante.objects.all()[:MAX_OBJECTS]
    data = {"results": list(est.values("nombres","apellidos"))}
    return JsonResponse(data)
def Estudiante_detalle(request,pk):
    est = get_object_or_404(Estudiante, pk=pk)
    data = {"results": {
        "nombres": est.nombres,
        "apellidos": est.apellidos
        }}
    return JsonResponse(data)
class EstudiantesList2(APIView):
    def get(self,request):
        estuidantes= Estudiante.objects.all()
        data=EsutianteSerializado(estuidantes, many=True).data
        return Response(data)