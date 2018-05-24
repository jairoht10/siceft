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