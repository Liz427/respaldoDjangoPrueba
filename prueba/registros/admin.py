from django.contrib import admin

from .models import Alumnos

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Agregando campos de sólo lectura (readonly)
    list_display = ('matricula', 'nombre', 'carrera', 'turno') #Agregando columnas para mostrar los alumnos registrados
    search_fields = ('matricula', 'nombre', 'carrera', 'turno') #Agregando barra de búsqueda
    date_hierarchy = 'created' #Agregando búsqueda por fecha
    list_filter = ('carrera', 'turno') #Agregando filtro lateral

admin.site.register(Alumnos, AdministrarModelo)