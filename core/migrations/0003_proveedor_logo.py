# Generated by Django 3.2.3 on 2021-07-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210701_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='logo',
            field=models.ImageField(null=True, upload_to='proveedores'),
        ),
    ]
