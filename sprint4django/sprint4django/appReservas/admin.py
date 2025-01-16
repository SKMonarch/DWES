from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Usuario, Evento, Reserva, Comentario

# Personalización para el modelo Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol', 'first_name', 'last_name', 'biografia', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('rol',)

# Personalización para el modelo Evento
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_hora', 'capacidad', 'organizador', 'imagen_url')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha_hora', 'organizador')
    list_per_page = 10

# Personalización para el modelo Reserva
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'entradas', 'estado')
    search_fields = ('usuario__username', 'evento__titulo')
    list_filter = ('estado',)


# Personalización para el modelo Comentario
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'texto', 'fecha_creacion')
    search_fields = ('usuario__username', 'evento__titulo', 'texto')
    list_filter = ('fecha_creacion',)

# Registro de modelos en el panel de administración
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
