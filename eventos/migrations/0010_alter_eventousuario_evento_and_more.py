# Generated by Django 4.0.6 on 2022-08-04 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0009_alter_eventousuario_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventousuario',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.evento', unique=True),
        ),
        migrations.AlterField(
            model_name='eventousuario',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]