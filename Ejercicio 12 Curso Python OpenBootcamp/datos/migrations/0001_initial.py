# Generated by Django 4.2.1 on 2023-06-02 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Pon el nombre del director', max_length=64)),
                ('fecha', models.DateField(help_text='Fecha de nacimiento del director', max_length=15)),
                ('genero', models.CharField(help_text='Pon el genero del director', max_length=10)),
                ('lugar', models.CharField(help_text='Inserte el lugar de nacimiento del director', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Pon el nombre de la película', max_length=128)),
                ('descripcion', models.TextField(help_text='Ingrese aquí la descripción de la película', max_length=300)),
                ('fecha', models.DateField(help_text='Fecha original de salida de la película', max_length=15)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='datos.director')),
            ],
        ),
    ]
