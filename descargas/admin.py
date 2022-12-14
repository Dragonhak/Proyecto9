from django.contrib import admin

from .models import Archivo

class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'desc', 'arch', 'extension', 'fecha')
    list_filter = ('fecha', 'nombre', 'extension')

admin.site.register(Archivo, ArchivoAdmin)
