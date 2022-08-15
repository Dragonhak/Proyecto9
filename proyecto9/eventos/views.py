from turtle import Turtle
from django.shortcuts               import render
from .models                        import Evento, EventoUsuario
from django.views.generic           import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts               import redirect
from django.http                    import Http404
from .forms                         import EventoForm
from django.urls                    import reverse_lazy

# Create your views here.

class listaEventos(ListView):
    model = Evento
    context_object_name = 'lista_eventos'
    template_name = "eventos/listaEventos.html"
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Evento.objects.order_by('fecha')
        return queryset

class modEvento(UpdateView):
    model = Evento
    form_class = EventoForm
    context_object_name = 'mod_evento'
    template_name = "eventos/modEvento.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("productos:admin_listar")

class insEvento(CreateView):
    model = Evento
    form_class = EventoForm
    context_object_name = 'insEvento'
    template_name = "eventos/insEvento.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("listaEventos")

#@superuser_required()
def borrarEvento(request, eventoId):
	e = Evento.objects.get(id=eventoId)
	e.delete()
	return redirect("listaEventos")

"""
class borrarEvento(DeleteView):
    model = Evento
    form_class = EventoForm
    context_object_name = 'borrarEvento'
    template_name = "eventos/insEvento.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("listaEventos")
"""
"""
class detalleEventos(DetailView):
    model = Evento
    context_object_name = 'evento'
    template_name = "eventos/detalleEventos.html"
    
    #Redefino para pasar variables de contexto adicionales
    def get_context_data(self, **kwargs):
        context = super(detalleEventos, self).get_context_data(**kwargs)
        #Nuevo dato que quiero pasar..
        context ['isParticipante'] = self.titulo
        return context
    
    """

#Por funcion
def detalleEventos(request,eventoId):
    
    isExisteEU = True
    try:
        evento = Evento.objects.get(id = eventoId)
        eu = EventoUsuario.objects.get(evento_id = eventoId, usuario_id = request.user.id)     
    except Evento.DoesNotExist:
        raise Http404("No existe Evento")
    except EventoUsuario.DoesNotExist:
        isExisteEU = False

    #evento=get_object_or_404(Evento, pk=pk)

    return render(
        request,
        'eventos/detalleEventos.html',
        context={'evento':evento,
        'isExisteEU':isExisteEU,        
        }
    )
    
def cancelPartEU(request, eventId, userId):
    EventoUsuario.objects.get(evento_id = eventId, usuario_id = userId).delete()
    return redirect('detalleEventos', eventoId = eventId)
    
def participarEU(request, eventoId, usuarioId): 
    EventoUsuario.objects.create(evento_id = eventoId, usuario_id = usuarioId)
    return redirect('detalleEventos', eventoId = eventoId)

def buscarEvento(request):
    if request.method == "POST":
        cat = request.POST['cat']
        fch = request.POST['fch']
        if cat == '' and fch == '':
            return redirect('listaEventos')
        else:
            if cat == '':
                lista_eventos = Evento.objects.filter(fecha__contains = fch)
            elif fch == '':
                lista_eventos = Evento.objects.filter(categoria__contains = cat)
            else:
                lista_eventos = Evento.objects.filter(categoria__contains = cat).filter(fecha__contains = fch)
            return render(request,'eventos/listaEventos.html', 
            {'cat':cat,
            'fch':fch,
            'lista_eventos':lista_eventos})
    else:
        return render(request,'eventos', 
        {})
