from django.urls        import path
from .                  import views
#from django.conf.urls   import url

urlpatterns = [
    path("Registrarme/", views.registrar_usuario, name="registrar")
]