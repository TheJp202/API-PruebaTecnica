# Generated by Django 5.0.4 on 2024-04-20 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cargo', '0002_alter_cargo_nombre'),
        ('Empleado', '0002_alter_empleado_apellido_alter_empleado_correo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdCargo', models.ForeignKey(db_column='IdCargo', on_delete=django.db.models.deletion.CASCADE, to='Cargo.cargo')),
                ('IdEmpleado', models.ForeignKey(db_column='IdEmpleado', on_delete=django.db.models.deletion.CASCADE, to='Empleado.empleado')),
            ],
        ),
    ]
