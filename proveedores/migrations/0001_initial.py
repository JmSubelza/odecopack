# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaPrecio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cantidad_minima', models.DecimalField(decimal_places=3, max_digits=10)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedores.Moneda')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='listaprecio',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
        migrations.AlterUniqueTogether(
            name='listaprecio',
            unique_together=set([('producto', 'cantidad_minima')]),
        ),
    ]