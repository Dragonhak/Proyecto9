from django.db            import models
from usuarios.models      import Usuario

class Usuario(models.Model):

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

    titulo = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    lugar = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    categoria = models.CharField(max_length=20, choices = CATEGORIA_CHOICES)
    modalidad = models.CharField(max_length=20, choices = MODALIDAD_CHOICES)
    gratuito = models.BooleanField(null = False)
    participantes = models.ManyToManyField(Usuario)

    class Meta:
        db_table="eventos"

    def __str__(self):
        return f"{self.titulo} {self.desc} {self.lugar} {self.fecha} {self.categoria} {self.modalidad} {self.gratuito}"
	