# Generated by Django 4.0.6 on 2022-08-04 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_eventousuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventousuario',
            options={'ordering': ['evento', 'usuario']},
        ),
        migrations.RenameField(
            model_name='eventousuario',
            old_name='evento_id',
            new_name='evento',
        ),
        migrations.RenameField(
            model_name='eventousuario',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]