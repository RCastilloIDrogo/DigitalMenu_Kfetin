# Generated by Django 5.1.6 on 2025-03-20 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_venta_detalleventa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cajero',
        ),
        migrations.DeleteModel(
            name='DetalleVenta',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]
