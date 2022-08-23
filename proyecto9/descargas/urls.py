from django.urls        import path
from .                  import views

urlpatterns = [
    path('listaArchivos', views.listaArchivos.as_view(), name='listaArchivos'),
    path('agregarArchivo', views.agregarArchivo.as_view(), name='agregarArchivo'),
    #path('<int:eventoId>/', views.detalleEventos, name='detalleEventos'),
    #path('participar/<int:eventoId>/<int:usuarioId>', views.participarEU, name='participarEU'),
    #path('cancelparticipar/<int:eventId>/<int:userId>', views.cancelPartEU, name='cancelPartEU'),
    #path('buscarEvento', views.buscarEvento, name='buscarEvento'),
    #path('modEvento/<int:pk>/', views.modEvento.as_view(), name='modEvento'),
    #path('borrarEvento/<int:eventoId>/', views.borrarEvento, name='borrarEvento'),
    #
]

