from django.urls        import path
from .                  import views

urlpatterns = [
    path('', views.listaEventos.as_view(), name='listaEventos'),
    #path('<int:pk>/', views.detalleEventos.as_view(), name='detalleEventos'),
    path('<int:eventoId>/', views.detalleEventos, name='detalleEventos'),
    path('participar/<int:eventoId>/<int:usuarioId>', views.participarEU, name='participarEU'),
    path('cancelparticipar/<int:eventId>/<int:userId>', views.cancelPartEU, name='cancelPartEU'),
    path('buscarEvento', views.buscarEvento, name='buscarEvento'),
    #
]

