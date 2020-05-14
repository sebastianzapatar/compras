from django.db import models
from home.models import clasemodelo
# Create your models here.
class Categoria(clasemodelo):
    descripcion=models.CharField(
        max_length=100,
        help_text='Descripción del producto' #cuando creo el formulario en django hay un cambio
    )
    def __str__(self): #Para mostar cuando se llama y que aparezca la descripción no el valor hexadecimal
        return '{}'.format(self.descripcion)
    class Meta:
        verbose_name_plural="Categorias"
class SubCategoria(clasemodelo):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion=models.CharField(
        max_length=100,
        help_text='Descripción del producto' #cuando creo el formulario en django hay un cambio
    )
    def __str__(self): #Para mostar cuando se llama y que aparezca la descripción no el valor hexadecimal
        return '{}:{}'.format(self.descripcion,self.categoria.descripcion)
    class Meta:
        verbose_name_plural="SubCategorias"
        unique_together =('categoria', 'descripcion')
class Marca(clasemodelo):
    descripcion=models.CharField(
        max_length=100,
        help_text='Nombre de la Marca' #cuando creo el formulario en django hay un cambio
    )
    def __str__(self): #Para mostar cuando se llama y que aparezca la descripción no el valor hexadecimal
        return '{}'.format(self.descripcion)
    class Meta:
        verbose_name_plural="Marcas"
class UM(clasemodelo):
    descripcion=models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad de Medidad' #cuando creo el formulario en django hay un cambio
    )
    def __str__(self): #Para mostar cuando se llama y que aparezca la descripción no el valor hexadecimal
        return '{}'.format(self.descripcion)
    class Meta:
        verbose_name_plural="Unidades de Medida"
class Producto(clasemodelo):
    codigo=models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    existencia=models.IntegerField(default=0)
    ultima_compra=models.DateField(null=True, blank=True)
    precio=models.FloatField(default=0)

    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida=models.ForeignKey(UM, on_delete=models.CASCADE)
    subcategoria=models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    class Meta:
        verbose_name_plural="productos"
        unique_together =('codigo', 'codigo_barra')