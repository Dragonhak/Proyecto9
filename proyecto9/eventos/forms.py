from django                    import forms
from .models                   import Evento

class EventoForm(forms.ModelForm):
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

    titulo = forms.CharField(label="Titulo", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese un titulo"}))
    desc = forms.CharField(label="Descripcion", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese una descripcion"}))
    lugar = forms.CharField(label="Lugar", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese un Lugar"}))
    #fecha = forms.DateTimeField(label="Fecha", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese una Fecha"}))
    #categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, required=True)
    #modalidad = forms.CharField(max_length=20, choices = MODALIDAD_CHOICES)
    #gratuito = forms.CharField(max_length=2, choices = GRATUITO_CHOICES, default='SI')
    class Meta:
        model = Evento
        fields = ("titulo", "desc", "lugar", "fecha","categoria","modalidad","gratuito")