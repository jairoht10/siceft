from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import Evento, Certificado
from base.constant import SINO

class EventoForm(forms.ModelForm):
    """ Clase que contiene los formularios del evento """
    ##Nombre del evento
    nombre = models.CharField(
        label =_("Nombre:"), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique el nombre del evento"),
            }
        )
    )

    ##Resumen del evento
    resumen = forms.CharField(
        label=_("Resumen:"), max_length=100,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'cols': '40', 'rows': '10',
                'title': _("Indique el resumen del evento"),
            }
        )
    )

    ## Permitir que los usuarios se suscriban a los eventos
    suscripcion = forms.ChoiceField(
        label= _("¿Permitir Suscripciones?"),
        choices= SINO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _("Seleccione la opción correcta"),
            }
        ),
    )

    ## Fecha del evento
    fecha = forms.CharField(
        label=_("Fecha:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm datepicker','readonly':'true',
                'title': _("Seleccione la fecha que se realiza el evento"),
            }
        )
    )

    ## Fecha de inicio del evento
    fecha_inicial = forms.CharField(
        label=_("Fecha Inicial:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm datepicker','readonly':'true',
                'title': _("Seleccione la fecha inicial del evento"),
            }
        )
    )

    ## Fecha de inicio del evento
    fecha_final = forms.CharField(
        label=_("Fecha Final:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm datepicker','readonly':'true',
                'title': _("Seleccione la fecha final del evento"),
            }
        )
    )

    class Meta:
        model = Evento
        exclude = ['user']

class CertificadoForm(forms.ModelForm):
    """Clase que contiene los campos del formulario evento """

    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user')
        super(CertificadoForm, self).__init__(*args, **kwargs)

        lista_evento = [('','Selecione...')]
        for ev in Evento.objects.filter(user=user):
            lista_evento.append( (ev.id,ev) )
        self.fields['evento'].choices = lista_evento

    ## Imagen delantera del cetificado
    imagen_delantera = forms.ImageField()

    ## Coordenada Y para posicionar el nombre del suscriptor
    coordenada_y_nombre = forms.CharField(
        label=_("Coordenada Y del Nombre:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-md', 'data-toggle': 'tooltip',
            'title': _("Indique la coordenada Y para posicionar el nombre del suscriptor"),
            'min':'0', 'step':'1', 'value':'0',
        }),
    )

    ## Contiene los eventos que el usuario ha registrado
    evento = forms.ChoiceField(
        label=_("Evento:"),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _("Seleccione el evento"),
            }
        )
    )

    class Meta:
        model = Certificado
        exclude = ['evento',]
