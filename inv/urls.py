from django.contrib import admin
from django.urls import include, path
from inv.views import ListarCategorias, InsertarCategoria,EditarCategoria, BorrarCategoria, ListarSubCategorias, \
    InsertarSubCategoria, EditarSubCategoria, BorrarSubCategoria, ListarMarcas, InsertarMarca, EditarMarca, marca_incativar, \
        ListarUM, InsertarUM, EditarUM, UM_incativar, ListarProductos, Producto_incativar, InsertarProducto, EditarProducto

urlpatterns=[
    path('categorias/',ListarCategorias.as_view(),name='listarcategorias'),
    path('categorias/new',InsertarCategoria.as_view(),name='nuevacategoria'),
    path('categorias/edit/<int:pk>',EditarCategoria.as_view(),name='editarcategoria'),
    path('categorias/delete/<int:pk>',BorrarCategoria.as_view(),name='BorrarCategoria'),


    path('subcategorias/',ListarSubCategorias.as_view(),name='listarsubcategorias'),
    path('subcategorias/new',InsertarSubCategoria.as_view(),name='nuevasubcategoria'),
    path('subcategorias/edit/<int:pk>',EditarSubCategoria.as_view(),name='editarsubcategoria'),
    path('subcategorias/delete/<int:pk>',BorrarSubCategoria.as_view(),name='BorrarSubCategoria'),

    path('marcas/',ListarMarcas.as_view(),name='listarmarcas'),
    path('marcas/new',InsertarMarca.as_view(),name='nuevamarca'),
    path('marcas/edit/<int:pk>',EditarMarca.as_view(),name='editarmarca'),
    path('marca/inactivar/<int:id>',marca_incativar,name='marcainactivar'),

    path('UM/',ListarUM.as_view(),name='listarUM'),
    path('UM/new',InsertarUM.as_view(),name='NuevoUM'),
    path('UM/edit/<int:pk>',EditarUM.as_view(),name='EditarUM'),
    path('UM/inactivar/<int:id>', UM_incativar,name="UMinactivar"),


    path('productos/',ListarProductos.as_view(),name='listarproductos'),
    path('productos/inactivar/<int:id>', Producto_incativar,name="Productoinactivar"),
    path('producto/new',InsertarProducto.as_view(),name='NuevoProducto'),
    path('producto/edit/<int:pk>',EditarProducto.as_view(),name='EditarProducto'),
]