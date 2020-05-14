from django.db import models
from home.models import clasemodelo
from inv.models import Producto
# Create your models here.
class ComprasEnc(clasemodelo):
    fecha_compra=models.DateField(null=True, blank=True)
    observacion=models.TextField(blank=True,null=True)
    no_factura=models.CharField(max_length=100)
    fecha_factura=models.DateField()
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.observacion)
    def save(self):
        self.total=self.sub_total-self.descuento
        super(ComprasEnc,self).save()
    class Meta:
        verbose_name_plural="Encabezado compras"
        verbose_name="encabezado compra"
class ComprasDet(clasemodelo):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)
    def __str__(self):
        return '{}'.format(self.producto)
    def save(self):
        self.sub_total=float(self.cantidad*self.precio_prv)
        self.total=self.sub_total-float(self.descuento)
        super(ComprasDet,self).save()
    class Meta:
        verbose_name_plural="detalles compras"
        verbose_name="detalle compra"