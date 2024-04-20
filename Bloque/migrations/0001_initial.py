# Generated by Django 5.0.4 on 2024-04-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(verbose_name=10)),
                ('FechaInicio', models.DateField()),
                ('FechaFinal', models.DateField()),
                ('CostoFinal', models.IntegerField()),
            ],
        ),
    ]