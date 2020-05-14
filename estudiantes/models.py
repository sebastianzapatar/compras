from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField(null=True,
    blank=True
    )
    direccion=models.CharField(max_length=50)
    def __str__(self):
        return '{} {}'.format(self.nombres,self.apellidos)
    class Meta:
        verbose_name_plural="Estudiantes"

class ClubDeportivo(models.Model):
    nombre=models.CharField(max_length=50)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
        verbose_name_plural="Clubes"