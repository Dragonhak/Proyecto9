from turtle import Turtle
from django.shortcuts               import render
from .models                        import Evento, EventoUsuario
from django.views.generic           import ListView, CreateView, UpdateView, DeleteView, DetailView

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
    model = Evento
    context_object_name = 'lista_eventos'
    template_name = "eventos/listaEventos.html"
    paginate_by = 12
       
    #Redefino para pasar variables de contexto adicionales
	#def get_context_data(self, **kwargs):
        #Primero se trae el contexto actual
		#context = super(listaEventos, self).get_context_data(**kwargs)
        #Nuevo dato que quiero pasar..
        #context['some_data'] = 'This is just some data'
		#return context
    
    def get_queryset(self):
        queryset = Evento.objects.order_by('fecha')
        return queryset

class detalleEventos(DetailView):
    model = Evento
    context_object_name = 'evento'
    template_name = "eventos/detalleEventos.html"

"""Por funcion
def detalleEventos(request,pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        raise Http404("Book does not exist")

    #evento=get_object_or_404(Evento, pk=pk)

    return render(
        request,
        'eventos/detalleEventos.html',
        context={'evento':evento,}
    )
"""


def isParticipante(request, eventoId, usuarioId):
    try:
        eu = EventoUsuario.objects.get(eventoId,usuarioId)
        return True
    except EventoUsuario.DoesNotExist:
        return False
    
def participar(request, eventoId, usuarioId):
    
    EventoUsuario.objects.create(eventoId,usuarioId)

    return render(
        request,
        'eventos/detalleEventos.html',
        context={}
    )


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