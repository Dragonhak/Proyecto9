from django.shortcuts       import render
from django.views.generic   import ListView, CreateView
from .models                import Archivo
from django.urls            import reverse_lazy

class agregarArchivo(CreateView):
   model = Archivo
   fields = '__all__'
   template_name = 'descargas/subirArchivo.html'
   context_object_name = 'agregarArchivo'

   def get_success_url(self, **kwargs):
        return reverse_lazy("listaArchivos")


class listaArchivos(ListView):
    model = Archivo
    #fields = '__all__'
    template_name = 'descargas/listaArchivo.html'
    context_object_name = 'listaArchivos'
