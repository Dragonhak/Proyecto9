from django.db import models

class Saludo(models.Model):
    nombre = models.CharField(max_length=255)