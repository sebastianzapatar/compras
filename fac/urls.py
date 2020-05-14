from django.contrib import admin
from django.urls import include, path
from .views import ListarClientes
urlpatterns=[
    path('clientes/',ListarClientes.as_view(),name='listarclientes'),
]