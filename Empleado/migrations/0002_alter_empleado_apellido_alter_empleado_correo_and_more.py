# Generated by Django 5.0.4 on 2024-04-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='Apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Correo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Telefono',
            field=models.CharField(max_length=9),
        ),
    ]
