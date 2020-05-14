from django import forms
from .models import ComprasEnc

class ComprasEncForm(forms.ModelForm):
    fecha_compra=forms.DateInput()
    fecha_factura=forms.DateInput()

    class Meta:
        model=ComprasEnc
        fields=['fecha_compra','observacion','no_factura','fecha_factura',
        'sub_total','descuento','total']
    def __init(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['fecha_compra'].widget.attrs['readonly']=True
        self.fields['fecha_factura'].widget.attrs['readonly']=True
        self.fields['sub_total'].widget.attrs['readonly']=True
        self.fields['total'].widget.attrs['readonly']=True
