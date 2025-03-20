# Generated by Django 5.1.6 on 2025-03-20 15:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0002_plato_imagen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('metodo_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('saldo', 'Saldo Prepago')], default='efectivo', max_length=10)),
                ('cajero', models.ForeignKey(limit_choices_to={'role': 'mesero'}, on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=6)),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.plato')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='ventas.venta')),
            ],
        ),
    ]
