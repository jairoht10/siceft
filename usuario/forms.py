from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from usuario.models import Suscriptor

class UsuarioForm(forms.ModelForm):

    ## Cedula (login) del suscriptor
    username = forms.CharField(
        label=_("Cédula (username):"),
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agregan ceros (0) si la longitud es de 7 o menos caracteres.")
            ),
        ], help_text=_("V00000000 ó E00000000")
    )

    ## Nombre del suscriptor
    nombre=forms.CharField(
        label=_("Nombres"),
        max_length=100,
        widget=forms.TextInput(
                attrs={
                'class':'form-control input-sm', 'data-toggle': 'tooltip', 'style': 'width:250px;',
                'title':_("Indique Los Nombres de la Persona"),
                       }
                )
    )

    ## Apellido del suscriptor
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

    correo = forms.EmailField(
        label=_("Correo Electrónico:"), max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'data-toggle': 'tooltip',
                'title': _("Indique el correo electrónico de contacto")
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
    ## Número telefónico de la casa de contacto con el usuario
    telefono_casa = forms.CharField(
        label=_("Teléfono local:"),
        max_length=16,
        widget=forms.TextInput(
            attrs={
                'clas   s': 'form-control input-sm', 'placeholder': '+058-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'size': '15',
                'title': _("Indique el número telefónico de contacto"), 'data-mask': '+000-000-0000000'
            }
        ),
        help_text=_("(país)-área-número")
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

    def clean_verificar_contrasenha(self):
        verificar_contrasenha = self.cleaned_data['verificar_contrasenha']
        contrasenha = self.data['password']
        if contrasenha != verificar_contrasenha:
            raise forms.ValidationError(_("La contraseña no es la misma"))
        return verificar_contrasenha

    class Meta:
        model = User
        exclude = [
            'perfil','date_joined',
        ]



class UsuarioUpdateForm(UsuarioForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['verificar_contrasenha'].required = False
        self.fields['password'].widget.attrs['disabled'] = True
        self.fields['verificar_contrasenha'].widget.attrs['disabled'] = True

    def clean_verificar_contrasenha(self):
        pass

    class Meta:
        model = User
        exclude = [
            'password','verificar_contrasenha','username','date_joined','last_login','is_active',
            'is_superuser','is_staff'
        ]

class SuscriptorForm(forms.ModelForm):
    #Clase que contiene los datos de las suscipciones de los usuarios a los eventos

    ## Muestra el evento al que el usuario está suscrito
    evento = forms.CharField(
        label=_("Evento:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'readonly':'true',
                'title': _("Muestra el evento"),
            }
        )
    )

    ## Muestra al suscriptor
    perfil = forms.CharField(
        label=_("Perfil:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'readonly':'true',
                'title': _("Muestra el perfil"),
            }
        )
    )

    ## Variable que indica si el usuario puede descargar el certificado
    otorgar = forms.BooleanField(
        label= _("Otorgar:"),
        required = False,
    )

    class Meta:
        model = Suscriptor
        exclude = [
            'evento','perfil',
        ]
