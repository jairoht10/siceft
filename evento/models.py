from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    ##Clase que contiene los datos de evento
    ##Nombre del evento
    nombre = models.CharField(max_length=150)

    ## Breve descripción del evento
    resumen = models.CharField(max_length=150)

    ##Permitir que los usuarios se suscriban al evento
    suscripcion = models.BooleanField()

    ##Permitir que el evento sea visible a los usuarios
    publicacion = models.BooleanField()

    ##Fecha del evento
    fecha = models.DateField()

    ##Fecha de inicio del evento
    fecha_inicial = models.DateField()

    ##Fecha Final del evento
    fecha_final = models.DateField()

    ##Establece relacion entre usuario del sistema y evento
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Certificado(models.Model):
    ##Clase que contiene los datos de un certificado que se genera para algún usuario cuando es otorgado

    ##Imagen delantera del Certificado
    imagen_delantera = models.ImageField(upload_to='certificado/')

    ## Coordenada en el eje Y del nombre del suscriptor
    coordenada_y_nombre = models.IntegerField()

    ## Establece la relación del certificado con el evento
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' | ' + str(self.evento)
