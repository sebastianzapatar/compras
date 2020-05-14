from django.shortcuts import render
from django.views import generic
from coms.models import ComprasEnc, ComprasDet
from inv.models import Producto
from home.views import Sinprivilegios
from coms.forms import ComprasEncForm
import datetime
from django.http import HttpResponse
# Create your views here.
class ComprasView( Sinprivilegios,generic.ListView):
    model=ComprasEnc
    template_name="coms/compras_list.html"
    permission_required="coms.view_comprasenc"
    context_object_name="obj"

def compras(request, compra_id=None):
    template_name="coms/compras.html"
    prod=Producto.objects.filter(estado=True)
    form_compras={}
    contexto={}

    if request.method=='GET':
        form_compras=ComprasEncForm()
        enc=ComprasEnc.objects.filter(pk=compra_id).first()
    
    if enc:
        det=ComprasEnc.object.filter(compras=enc)
        fecha_compra=datetime.date.isoformat(enc.fecha_compra)
        fecha_factura=datetime.date.isoformat(enc.fecha_factura)
        e:{
            'fecha_compra':fecha_compra,
            'fecha_factura':fecha_factura,
            'observacion':enc.observacion,
            'no_factura':enc.no_factura,
            'sub_total':enc.sub_total,
            'descuento':enc.descuento,
            'total':enc.total
        }
        form_compras=ComprasEncForm(e)
    else:
        det=None
    

    contexto={'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_compras}

    return render(request, template_name, contexto)
