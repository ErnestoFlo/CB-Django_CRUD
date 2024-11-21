from django.db import models
from .choices import *
from django import forms
from datetime import datetime


class foranea (models.Model):
    nombreForaneo= models.CharField(max_length=20, verbose_name='Nombre Foraneo')
    nombreForaneoB= models.CharField(max_length=20, verbose_name='Nombre ForaneoB')
    eleccion= models.CharField(max_length=20, choices=opciones, default='A')

    def rtNombreForaneo(self):
        return "{} {}, {}".find(self.nombreForaneo, self.nombreForaneoB, self.eleccion)

    class Meta:
        verbose_name = "Foranea"
        verbose_name_plural = "Foraneas"
        db_table = "foranea"
        ordering =["nombreForaneo", "-nombreForaneoB"]

# Create your models here.
class crud (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True, verbose_name='Imagen')
    descripcion = models.TextField(null=True, verbose_name='Descripción')
    ##OJO ESTO ES EXTRA 
    numero = models.IntegerField(null=True, verbose_name='Número')
    ## decimal = models.DecimalField(null=True, verbose_name='Decimal', max_digits=2, decimal_places=2)
    ## booleano = models.BooleanField(verbose_name='Boleano', default=0)
    fecha = models.DateField(null=True, blank=True)
    correo = models.EmailField(verbose_name='Correo Electrónico', null=True)
    campoForaneo = models.ForeignKey(foranea, null=True, blank=True, on_delete=models.CASCADE)

    # Esta es la descripción de los datos del admin
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion 
        return fila
    
    # Esto es para eliminar imagenes del servidor de alojamiento
    def delete(self, using= None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()