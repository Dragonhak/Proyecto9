from django.urls        import path
from .                  import views

urlpatterns = [
    path('listaArchivos', views.listaArchivos.as_view(), name='listaArchivos'),
    path('agregarArchivo', views.agregarArchivo.as_view(), name='agregarArchivo'),
    path('borrarArchivo/<int:archivoId>/', views.borrarArchivo, name='borrarArchivo'),
]

