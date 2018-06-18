from django.contrib import admin

# Register your models here.

from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):

    ## Mostrar los campos
    list_display = ('user','telefono',)

    ## Filtrar por campos
    list_filter = ('user','telefono',)

    ## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('user',)

    ## Buscar por campos
    search_fields = ('telefono','user',)

## Registra el modelo Perfil en el panel administrativo
admin.site.register(Perfil, PerfilAdmin)
