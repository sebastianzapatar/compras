from django.contrib import admin
from django.urls import include, path
from coms.views import ComprasView
from coms.report import reporte
urlpatterns=[
    path('coms/',ComprasView.as_view(),name='listarcompras'),
    path('coms/imprimir',reporte,name='imprimirproductos'),
]