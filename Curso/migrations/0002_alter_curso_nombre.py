# Generated by Django 5.0.4 on 2024-04-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='Nombre',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]