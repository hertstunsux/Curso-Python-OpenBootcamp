from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del director")
    fecha = models.DateField(max_length=15, help_text="Fecha de nacimiento del director")
    genero = models.CharField(max_length=10, help_text="Pon el genero del director")
    lugar = models.CharField(max_length=50, help_text="Inserte el lugar de nacimiento del director")
    
    def __str__(self):
        return self.name
    
class Pelicula(models.Model):
    name = models.CharField(max_length=128, help_text="Pon el nombre de la película")
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=300, help_text="Ingrese aquí la descripción de la película")
    fecha = models.DateField(max_length=15, help_text="Fecha original de salida de la película")

    def __str__(self):
        return self.name