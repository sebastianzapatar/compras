from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class Home(LoginRequiredMixin,generic.TemplateView):
    template_name="home/home.html"
    login_url="home:login"
class HomeSinprivilegio(generic.TemplateView):
    template_name="home/sinprivilegios.html"
class Sinprivilegios(PermissionRequiredMixin):
    raise_exception=False
    redirect_field_name="redirect_to"

    def handle_no_permission(self):
        self.login_url="home:sinprivilegios"
        return HttpResponseRedirect(reverse_lazy(self.login_url))
class RegistroUsuario(generic.CreateView):
    model=User
    template_name="home/registrar.html"
    form_class=UserCreationForm
    success_url=reverse_lazy("home:home")
    