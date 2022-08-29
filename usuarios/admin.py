from django.contrib         import admin
from .models                import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'dni', 'username', 'email')
    """fields modifica lo que se ve en el formulario"""
    fields = ['username', 'password', 'first_name', 'last_name', 'dni', 'email', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']

admin.site.register(Usuario, UsuarioAdmin)
