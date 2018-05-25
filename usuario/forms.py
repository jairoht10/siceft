from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class UsuarioForm(forms.modelsForm):
    # Se usa la cedula como username
    cedula=forms.CharField(
    label=_("Cédula"),
    max_length=9,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Cédula de la Persona"),
            }
        )
    )

    # Nombre del suscriptor
    nombre=forms.CharField(
    label=_("Nombres"),
    max_length=100,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style': 'width:250px;',
                'title':_("Indique Los Nombres de la Persona"),
            }
         )
    )

    # Apellido del suscriptor
    apellido=forms.CharField(
    label=_("Apellidos"),
    max_length=100,
    widget=forms.TextInput(
            attrs={
                'class':'form-control input-sm', 'data-toggle': 'tooltip', 'style': 'width:250px;',
                'title':_("Indique Los Apellidos de la Persona"),
            }
        )
    )
