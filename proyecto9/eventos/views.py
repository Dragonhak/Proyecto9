from django.shortcuts               import render
from .models                        import Evento, EventoUsuario
from django.views.generic           import ListView, CreateView, UpdateView, DeleteView


# Create your views here.
"""
def index(request):

    #Función vista para la página inicio del sitio.

    # Genera contadores de algunos de los objetos principales
    e = Evento.objects.all()
    # Libros disponibles (status = 'a')
    num_instances_available=Evento.objects.filter(gratuito__exact='SI').count()
    num_eventoUsuario=EventoUsuario.objects.count()  # El 'all()' esta implícito por defecto.

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'home/index.html',
        context={'e':e,'num_instances_available':num_instances_available,'num_eventoUsuario':num_eventoUsuario},
    )
"""
class listaEventos(ListView):
	template_name = "eventos/listaEventos.html"
	model = Evento
	context_object_name = 'lista_eventos'
	paginate_by = 12

	def get_context_data(self, **kwargs):
		context = super(listaEventos, self).get_context_data(**kwargs)
		return context

"""
    return render(request, 'home.html', {
        "anio": anio,
        "mes": mes,
        "numero_mes": numero_mes,
        "calendario": calendario,
        })

def bienvenidos(request):
    return render(request, "index.html")

def conocenos(request):
    return render(request, "conocenos.html")

def contactanos(request):
    return render(request, "contactanos.html")

	def get_queryset(self):
		return Evento.objects.order_by("fecha")
        
"""