# Generated by Django 5.0.4 on 2024-04-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(unique=True, verbose_name=80)),
                ('DuracionHora', models.IntegerField()),
                ('Costo', models.IntegerField()),
            ],
        ),
    ]
