# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20161020_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_dos_por_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_productos', to='productos_categorias.CategoriaDosCategoria', verbose_name='categoría dos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mis_productos', to='productos.ColorProducto', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mis_productos', to='productos.MaterialProducto', verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='serie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mis_productos', to='productos.SerieProducto', verbose_name='serie'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_por_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mis_productos', to='productos_categorias.TipoProductoCategoría', verbose_name='tipo'),
        ),
    ]
