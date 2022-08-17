from django.db            import models  
from django.db.models     import constraints, UniqueConstraint
from psycopg2             import Timestamp
from usuarios.models      import Usuario
from django.utils         import timezone
from django.urls          import reverse

from django.contrib import admin

class Evento(models.Model):

    CATEGORIA_CHOICES = (
    ('Educativo', 'Educativo'),
    ('Cultural', 'Cultural'),
    ('Deportivo', 'Deportivo'),
    ('Ambiental', 'Ambiental'),
    ('Productivo', 'Productivo'),
    ('Economico', 'Económico'),
    ('Comunitario', 'Comunitario'),
    )

    MODALIDAD_CHOICES = (
    ('Online', 'Online'),
    ('Presencial', 'Presencial'),
    )

    GRATUITO_CHOICES = (
    ('SI', 'SI'),
    ('NO', 'NO'),
    )

    titulo = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    lugar = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    categoria = models.CharField(max_length=20, choices = CATEGORIA_CHOICES)
    modalidad = models.CharField(max_length=20, choices = MODALIDAD_CHOICES)
    gratuito = models.CharField(max_length=2, choices = GRATUITO_CHOICES, default='SI')
    participantes = models.ManyToManyField(Usuario, through='EventoUsuario')

    class Meta:
        db_table="eventos"
        ordering = ["-fecha", "titulo", "categoria"] 

    def __str__(self):
        return f"{self.titulo} - {self.desc} - {self.lugar} - {self.fecha} - {self.categoria} - {self.modalidad} - {self.gratuito}"
	
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    """@admin.display: Redefine el nombre de la función cuando la muestro en la grilla"""
    @admin.display(
        description='Participantes',
    )
    def cantParticipantes(self):
        return len(self.participantes.all())



class EventoUsuario(models.Model):

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table="EventoUsuario"
        ordering = ["evento", "usuario"] 
        #Restricción que no permite que un mismo evento tenga 2 veces el mismo usuario
        constraints = [
            constraints.UniqueConstraint(
                fields=['evento', 'usuario'], name="unique_evento_usuarios"
             ),
            models.CheckConstraint(
                name="prevent_repeat",
                check=~models.Q(evento=models.F("usuario")),
            )
        ]

    def __str__(self):
        return f"{self.evento} - {self.usuario}"
        
	    