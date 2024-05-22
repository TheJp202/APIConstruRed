# Generated by Django 5.0.6 on 2024-05-20 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Descripcion', models.TextField()),
                ('PrecioContrato', models.IntegerField()),
                ('Estado', models.CharField(default='Pendiente', max_length=50)),
                ('Proyecto', models.ForeignKey(db_column='idProyecto', on_delete=django.db.models.deletion.CASCADE, to='Proyecto.proyecto')),
            ],
        ),
    ]