from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class UsuarioForm(forms.modelsForm):

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

    ## Número telefónico de contacto con el usuario
    telefono = forms.CharField(
        label=_("Teléfono:"),
        max_length=18,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '+58-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style': 'width:250px',
                'title': _("Indique el número telefónico de contacto"), 'data-mask': '+00-000-0000000'
            }
        ),
        help_text=_("(país)-área-número")
    )

    correo = forms.EmailField(
        label=_("Correo Electrónico:"),
        max_length=100,
        help_text=_("Cédula de Identidad del usuario"),
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'data-rule-required': 'true', 'style': 'width:250px',
                'title': _("Indique el correo electrónico de contacto con el usuario.")
            }
        )
    )

    password = forms.CharField(
        label=_("Contraseña:"),
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Contraseña de acceso"),
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique una contraseña de aceso al sistema")
            }
        )
    )

    ## Confirmación de contraseña de acceso
    verificar_contrasenha = forms.CharField(
        label=_("Verificar Contraseña:"),
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("Contraseña de acceso"),
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique nuevamente la contraseña de aceso al sistema")
            }
        )
    )
