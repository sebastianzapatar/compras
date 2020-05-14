"""compras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include(('home.urls','home'),namespace='home')),
    path('inv/',include(('inv.urls','inv'),namespace='inv')),
    path('admin/', admin.site.urls),
    path('coms/',include(('coms.urls','coms'),namespace='coms')),
    path('fac/',include(('fac.urls','coms'),namespace='fac')),
    path('estudiantes/',include(('estudiantes.urls','estudiantes'),namespace='estudiantes')),
]
