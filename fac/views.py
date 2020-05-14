from django.shortcuts import render
from django.views import generic
from .models import Cliente


# Create your views here.
class ListarClientes(generic.ListView):
    model=Cliente
    template_name="fac/clientes_list.html"
    context_object_name="obj"
    login_url="home:login"