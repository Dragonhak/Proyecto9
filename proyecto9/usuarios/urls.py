from django.urls        import path
from .                  import views

urlpatterns = [
    path("Registrarme/", views.registrar_usuario, name="registrar")
]