# Generated by Django 5.0.4 on 2024-04-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0002_alter_estudiante_apellido_alter_estudiante_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='DNI',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
