from rest_framework import serializers
from .models import Estudiante
class EsutianteSerializado(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        #fields('nombres','apellidos','fecha_nacimiento')
        fields='__all__'