from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class clasemodelo(models.Model):
    estado=models.BooleanField(default=True)
    fc=models.DateTimeField(auto_now_add=True)#Se crea la fecha y no se actualiza, solo cuando el registro se crea
    fm=models.DateTimeField(auto_now=True)#Se crea la fecha y se actualiza siempre que hay cambio
    uc=models.ForeignKey(User, on_delete=models.CASCADE) #Se importa el usuario que crea del usuario que este logueado
    um=models.IntegerField(blank=True, null=True) #Dejar campo vacio y permitir nulos
    class Meta:
        abstract=True


