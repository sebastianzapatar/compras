from django.db import models
from home.models import clasemodelo
# Create your models here.
class Cliente(clasemodelo):
    nombre=models.CharField(max_length=150)
    apellidos=models.CharField(max_length=100)
    celular=models.CharField(max_length=20,
    null=True,
    blank=True
    )
    NAT='Natural'
    JUR='Juridica'
    TIPO_CLIENTE=[
        (NAT,'Natural'),
        (JUR,'Juridica')]
    tipo=models.CharField(
        max_length=20,
        choices=TIPO_CLIENTE,
        default=NAT
    )
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)
    class Meta:
        verbose_name_plural="Clientes"
        