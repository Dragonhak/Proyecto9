from django.contrib         import admin
from .models                import Evento, EventoUsuario


#Trae el modelo de todos los usuarios, TabularInline o StackedInline (el tipo como se muestra)
class EventoUsuarioInstanceInline(admin.TabularInline):
    model = EventoUsuario

"""Re-defino lo que se muestra en el admin"""
#--
class EventoAdmin(admin.ModelAdmin):
    #list_display: lo que se ve en la grilla de eventos
    list_display = ('fecha', 'titulo', 'desc', 'lugar', 'categoria', 'modalidad', 'gratuito','cantParticipantes')
    list_filter = ('fecha', 'categoria', 'titulo')
    #Coloco en el formulario para que desde ahi se puedan agregar los usuarios que participan en el evento
    inlines = [EventoUsuarioInstanceInline]

admin.site.register(Evento, EventoAdmin)
#--
#--
class EventoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('evento', 'usuario')

admin.site.register(EventoUsuario, EventoUsuarioAdmin)
#--