# Generated by Django 4.0.6 on 2022-08-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]