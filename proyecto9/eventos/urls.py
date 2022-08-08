from django.urls        import path
from .                  import views

urlpatterns = [
    #path('', views.home, name="home"),
    #path('<int:anio>/<str:mes>/', views.home, name="home"),
    #path('', views.bienvenidos, name="bienvenidos"),
    #path('conocenos', views.conocenos, name="conocenos"),
    #path('contactanos', views.contactanos, name="contactanos"),
    path('', views.listaEventos.as_view(), name='listaEventos'),
]

