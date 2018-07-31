from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.views import View
from .models import Evento, Certificado
from .forms import EventoForm, CertificadoForm
from usuario.models import Suscriptor, Perfil
from usuario.forms import SuscriptorForm

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from PIL import Image, ImageDraw
from io import BytesIO
# Create your views here.

class EventoListView(ListView):
    ##Clase que permite a un usuario listar los eventos que ha registrado
    model = Evento
    template_name = 'evento/listar.html'

    def get_queryset(self):
        ##Método que obtiene la lista de eventos que están asociados al usuario
        queryset = Evento.objects.filter(user=self.request.user)
        return queryset

class EventoCreateView(CreateView):
    #Clase que permite a un usuario registrar eventos
    model = Evento
    form_class = EventoForm
    template_name = 'evento/registrar.html'
    success_url = reverse_lazy('evento:listar')

    def form_valid(self, form):
        #Metodo que valida si el formulario es correcto
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(EventoCreateView, self).form_valid(form)
        
