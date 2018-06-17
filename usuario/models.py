from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core import validators

# Create your models here.

class Perfil(models.Model):
    telefono = models.CharField(
        max_length=16, help_text=_("Número telefónico de contacto con el usuario"),
        validators=[
            validators.RegexValidator(
                r'^\+\d{3}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: + -")
            ),
        ]
    )
    telefono_casa = models.CharField(
    max_length=16, help_text=_("Número telefónico de contacto con el usuario"),
    validators=[
        validators.RegexValidator(
            r'^\+\d{3}-\d{3}-\d{7}$',
            _("Número telefónico inválido. Solo se permiten números y los símbolos: + -")
         ),
      ]
    )
    ## Establece el correo de la persona
    correo = models.CharField(
        max_length=100, help_text=("correo@correo.com")
    )
    ## Nombre de la Persona
    nombre = models.CharField(max_length=100)

    ## Apellido de la Persona
    apellido = models.CharField(max_length=100)

    ## Cédula de la Persona
    cedula = models.CharField(
        max_length=9,
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ],unique=True
    )
    
    user = models.ManyToManyField(User,on_delete=models.CASCADE)

class Meta:

        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfiles")
        def __str__(self):

            return "%s, %s" % (self.user.first_name, self.user.last_name)
