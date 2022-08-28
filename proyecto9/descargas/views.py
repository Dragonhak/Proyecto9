from django.views.generic   import ListView, CreateView
from .models                import Archivo
from django.urls            import reverse_lazy
from django.shortcuts       import redirect

class agregarArchivo(CreateView):
   model = Archivo
   fields = '__all__'
   template_name = 'descargas/subirArchivo.html'
   context_object_name = 'agregarArchivo'

   def get_success_url(self, **kwargs):
        return reverse_lazy("listaArchivos")


class listaArchivos(ListView):
    model = Archivo
    template_name = 'descargas/listaArchivo.html'
    context_object_name = 'listaArchivos'

def borrarArchivo(request, archivoId):
	a = Archivo.objects.get(id=archivoId)
	a.delete()
	return redirect("listaArchivos")