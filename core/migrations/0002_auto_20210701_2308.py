# Generated by Django 3.2.3 on 2021-07-02 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='moneda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.moneda'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.TextField(max_length=250, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.TextField(max_length=50, verbose_name='Nombre Completo'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name='Telefono'),
        ),
    ]