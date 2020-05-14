from django import forms
from estudiantes.models import Estudiante, ClubDeportivo
class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=['nombres', 'apellidos','fecha_nacimiento',
            'direccion'
        ]
        widget={'nombres':forms.TextInput(),'apellidos':forms.TextInput(),
        'fecha_nacimiento':forms.DateField(),'direccion':forms.TextInput()
        }
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
class ClubForm(forms.ModelForm):
    estudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.order_by('apellidos')
    )
    class Meta:
        model=ClubDeportivo
        fields=['nombre', 'estudiante'
        ]
        widget={'nombres':forms.TextInput()
        }
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })