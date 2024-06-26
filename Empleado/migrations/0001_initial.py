# Generated by Django 5.0.6 on 2024-05-20 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rol', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Foto', models.ImageField(blank=True, upload_to='construred/empleados/')),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('DNI', models.CharField(max_length=20, unique=True)),
                ('FechaContratacion', models.DateField()),
                ('Telefono', models.CharField(max_length=20)),
                ('Correo', models.EmailField(max_length=50, unique=True)),
                ('Contraseña', models.CharField(max_length=128)),
                ('Rol', models.ForeignKey(db_column='idRol', on_delete=django.db.models.deletion.CASCADE, to='Rol.rol')),
            ],
        ),
    ]
