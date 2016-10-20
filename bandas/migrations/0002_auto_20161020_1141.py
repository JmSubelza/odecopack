# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='valorcaracteristica',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='valorcaracteristica',
            name='caracteristica',
        ),
        migrations.AlterField(
            model_name='banda',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_color', to='productos_caracteristicas.ColorProducto'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='empujador_tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_tipo_empujador', to='productos_categorias.TipoProductoCategoría', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_fabricante', to='productos_caracteristicas.FabricanteProducto'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_material', to='productos_caracteristicas.MaterialProducto'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='material_varilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_material_varilla', to='productos_caracteristicas.MaterialProducto'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_serie', to='productos_caracteristicas.SerieProducto'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_tipo', to='productos_categorias.TipoProductoCategoría'),
        ),
        migrations.DeleteModel(
            name='Caracteristica',
        ),
        migrations.DeleteModel(
            name='ValorCaracteristica',
        ),
    ]
