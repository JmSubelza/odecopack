# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 14:59
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bandas', '0001_initial'),
        ('listasprecios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('INI', 'Iniciado'), ('ENV', 'Enviada'), ('ELI', 'Rechazada'), ('REC', 'Recibida'), ('PRO', 'En Proceso'), ('FIN', 'Entragada Totalmente')], default='INI', max_length=10)),
                ('nro_contacto', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('nombres_contacto', models.CharField(blank=True, max_length=120)),
                ('pais', models.CharField(blank=True, max_length=120)),
                ('ciudad', models.CharField(blank=True, max_length=120)),
                ('apellidos_contacto', models.CharField(blank=True, max_length=120)),
                ('razon_social', models.CharField(blank=True, max_length=120)),
                ('nro_cotizacion', models.CharField(max_length=120)),
                ('fecha_envio', models.DateTimeField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=0, default=0, max_digits=18)),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('full_cotizacion', 'Full Cotizacion'),),
            },
            managers=[
                ('estados', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ItemCotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cantidad', models.DecimalField(decimal_places=3, max_digits=18)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=18)),
                ('total', models.DecimalField(decimal_places=0, max_digits=18)),
                ('dias_entrega', models.PositiveIntegerField(default=0)),
                ('banda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cotizaciones', to='bandas.Banda')),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cotizaciones.Cotizacion')),
                ('forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_cotizaciones', to='listasprecios.FormaPago')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cotizaciones', to='productos.Producto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RemisionCotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nro_remision', models.PositiveIntegerField()),
                ('nro_factura', models.PositiveIntegerField()),
                ('fecha_prometida_entrega', models.DateField()),
                ('entregado', models.BooleanField(default=False)),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_remisiones', to='cotizaciones.Cotizacion')),
            ],
            options={
                'verbose_name_plural': 'Remisiones x Cotización',
            },
        ),
        migrations.CreateModel(
            name='TareaCotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('esta_finalizada', models.BooleanField(default=False)),
                ('cotizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mis_tareas', to='cotizaciones.Cotizacion')),
            ],
            options={
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]
