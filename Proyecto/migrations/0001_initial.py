# Generated by Django 5.0.6 on 2024-05-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(upload_to='construred/proyectos/')),
                ('Descripcion', models.TextField()),
                ('FechaInicio', models.DateField()),
                ('FechaFinal', models.DateField()),
            ],
        ),
    ]
