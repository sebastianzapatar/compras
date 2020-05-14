from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from inv.models import Categoria, SubCategoria, Marca, UM, Producto
from inv.forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm
from django.urls import reverse_lazy
from home.views import Sinprivilegios
# Create your views here.
class ListarCategorias(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    model=Categoria
    permission_required="inv.view_categoria"
    template_name="inv/categoria_list.html"
    context_object_name="obj"
    login_url="home:login"
    
class InsertarCategoria(SuccessMessageMixin,PermissionRequiredMixin,LoginRequiredMixin, \
    generic.CreateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    permission_required="inv.view_categoria"
    context_object_name="obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:listarcategorias")
    login_url="home:login"
    success_message="Categoria creada melo"
    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class EditarCategoria(SuccessMessageMixin,LoginRequiredMixin, \
    generic.UpdateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    permission_required="inv.view_categoria"
    context_object_name="obj"
    
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:listarcategorias")
    login_url="home:login"
    success_message="Categoria editada melo"
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
class BorrarCategoria(LoginRequiredMixin, generic.DeleteView):
    model=Categoria
    template_name="inv/catalogos_delete.html"
    context_object_name="obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:listarcategorias")
    login_url="home:login"
class ListarSubCategorias(LoginRequiredMixin, Sinprivilegios ,generic.ListView):
    model=SubCategoria
    template_name="inv/Subcategoria_list.html"
    permission_required="inv.view_subcategoria"
    context_object_name="obj"
    login_url="home:login"
class InsertarSubCategoria(LoginRequiredMixin, generic.CreateView):
    model=SubCategoria
    template_name="inv/Subcategoria_form.html"
    context_object_name="obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:listarsubcategorias")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class EditarSubCategoria(LoginRequiredMixin, generic.UpdateView):
    model=SubCategoria
    template_name="inv/Subcategoria_form.html"
    context_object_name="obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:listarsubcategorias")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
class BorrarSubCategoria(LoginRequiredMixin, generic.DeleteView):
    model=SubCategoria
    template_name="inv/catalogos_delete.html"
    context_object_name="obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:listarsubcategorias")
    login_url="home:login"

class ListarMarcas(LoginRequiredMixin,Sinprivilegios,generic.ListView):
    model=Marca
    template_name="inv/marca_list.html"
    permission_required="inv.view_marca"
    context_object_name="obj"
    login_url="home:login"
class InsertarMarca(LoginRequiredMixin, generic.CreateView):
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name="obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inv:listarmarcas")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class EditarMarca(LoginRequiredMixin, generic.UpdateView):
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name="obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inv:listarmarcas")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
def marca_incativar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_delete.html"
    if not marca:
        return redirect("inv:listarmarcas")
    if request.method=='GET':
        contexto={'obj':marca}
    if request.method=='POST': #Para actualizar datos desde una vista
        marca.estado=False
        marca.save()
        return redirect("inv:listarmarcas")
    return render(request, template_name, contexto)
class ListarUM(LoginRequiredMixin,generic.ListView):
    model=UM
    template_name="inv/UM_list.html"
    context_object_name="obj"
    login_url="home:login"
class InsertarUM(LoginRequiredMixin, generic.CreateView):
    model=UM
    template_name="inv/UM_form.html"
    context_object_name="obj"
    form_class=UMForm
    success_url=reverse_lazy("inv:listarUM")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class EditarUM(LoginRequiredMixin, generic.UpdateView):
    model=UM
    template_name="inv/UM_form.html"
    context_object_name="obj"
    form_class=UMForm
    success_url=reverse_lazy("inv:listarUM")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
def UM_incativar(request, id):
    um = UM.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_delete.html"
    if not um:
        return redirect("inv:listarUM")
    if request.method=='GET':
        contexto={'obj':um}
    if request.method=='POST': #Para actualizar datos desde una vista
        um.estado=False
        um.save()
        return redirect("inv:listarUM")
    return render(request, template_name, contexto)
class ListarProductos(LoginRequiredMixin,generic.ListView):
    model=Producto
    template_name="inv/producto_list.html"
    context_object_name="obj"
    login_url="home:login"
    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
def Producto_incativar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_delete.html"
    if not Producto:
        return redirect("inv:listarproductos")
    if request.method=='GET':
        contexto={'obj':producto}
    if request.method=='POST': #Para actualizar datos desde una vista
        producto.estado=False
        producto.save()
        return redirect("inv:listarproductos")
    return render(request, template_name, contexto)
class InsertarProducto(LoginRequiredMixin, generic.CreateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name="obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:listarproductos")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class EditarProducto(LoginRequiredMixin, generic.UpdateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name="obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:listarproductos")
    login_url="home:login"
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)