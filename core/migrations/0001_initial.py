# Generated by Django 3.2.3 on 2021-07-01 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('idMoneda', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Moneda')),
                ('nombreMoneda', models.CharField(max_length=50, verbose_name='Moneda')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idPais', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Pais')),
                ('nombrePais', models.CharField(max_length=50, verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Numero identificacion')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre Completo')),
                ('telefono', models.CharField(blank=True, max_length=50, verbose_name='Telefono')),
                ('direccion', models.CharField(blank=True, max_length=250, verbose_name='Direccion')),
                ('email', models.CharField(blank=True, max_length=250, verbose_name='Email')),
                ('password', models.CharField(blank=True, max_length=50, verbose_name='Password')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais')),
            ],
        ),
    ]