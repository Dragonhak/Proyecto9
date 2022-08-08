# Generated by Django 4.0.6 on 2022-08-04 21:45

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=250)),
                ('lugar', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.CharField(choices=[('Educativo', 'Educativo'), ('Cultural', 'Cultural'), ('Deportivo', 'Deportivo'), ('Ambiental', 'Ambiental'), ('Productivo', 'Productivo'), ('Economico', 'Económico'), ('Comunitario', 'Comunitario')], max_length=20)),
                ('modalidad', models.CharField(choices=[('Online', 'Online'), ('Presencial', 'Presencial')], max_length=20)),
                ('gratuito', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=2)),
                ('participantes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'eventos',
                'ordering': ['-fecha', 'titulo', 'categoria'],
            },
        ),
    ]
