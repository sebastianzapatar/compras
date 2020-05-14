from django.contrib import admin
from django.urls import include, path
from home.views import Home, HomeSinprivilegio, RegistroUsuario
from django.contrib.auth import views as authviews
urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('login/',
    authviews.LoginView.as_view(template_name="home/login.html"),name="login"),
    path('logout/',authviews.LogoutView.as_view(template_name='home/login.html'),name='logout'),
    path('sinprivilegios',HomeSinprivilegio.as_view(), name="sinprivilegios"),
    path('registrar',RegistroUsuario.as_view(),name="registrar"),
]
