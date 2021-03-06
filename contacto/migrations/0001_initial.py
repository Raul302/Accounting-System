# Generated by Django 3.0.5 on 2020-04-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=100, verbose_name='Apellido')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Correo')),
                ('edad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'name',
                'ordering': ['nombre'],
            },
        ),
    ]
