# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id_cguno', models.PositiveIntegerField(default=0)),
                ('descripcion_estandar', models.CharField(max_length=200)),
                ('descripcion_comercial', models.CharField(max_length=200)),
                ('referencia', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('paso', models.PositiveIntegerField(default=0)),
                ('ancho', models.PositiveIntegerField(default=0, verbose_name='Ancho (mm)')),
                ('longitud', models.DecimalField(decimal_places=2, default=1, max_digits=8, verbose_name='Longitud (m)')),
                ('total_filas', models.PositiveIntegerField(default=0)),
                ('con_empujador', models.BooleanField(default=False)),
                ('empujador_altura', models.PositiveIntegerField(default=0, verbose_name='Altura (mm)')),
                ('empujador_ancho', models.PositiveIntegerField(default=0, verbose_name='Ancho (mm)')),
                ('empujador_distanciado', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Distanciado (mm)')),
                ('empujador_identacion', models.CharField(default='N.A', max_length=10, verbose_name='Identacion')),
                ('empujador_filas_entre', models.PositiveIntegerField(blank=True, null=True, verbose_name='Filas entre Empujador')),
                ('empujador_total_filas', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Filas Empujador')),
                ('con_aleta', models.BooleanField(default=False)),
                ('aleta_altura', models.PositiveIntegerField(default=0, verbose_name='Altura (mm)')),
                ('aleta_identacion', models.CharField(default='N.A', max_length=10, verbose_name='Identacion')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo')),
                ('activo_componentes', models.BooleanField(default=False, verbose_name='En Compo.')),
                ('activo_proyectos', models.BooleanField(default=False, verbose_name='En Proy.')),
                ('activo_catalogo', models.BooleanField(default=False, verbose_name='En Cata.')),
                ('precio_banda', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ('precio_total', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ('costo_base_total', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ('rentabilidad', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ('costo_mano_obra', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
            ],
            options={
                'permissions': (('full_bandas', 'Full Bandas'),),
            },
        ),
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CostoEnsambladoBlanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('aleta', models.BooleanField(default=False)),
                ('empujador', models.BooleanField(default=False)),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Ensamblado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('precio_linea', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ('costo_cop_linea', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ('rentabilidad', models.DecimalField(decimal_places=4, default=0, max_digits=18)),
                ('ancho', models.PositiveIntegerField(default=0, verbose_name='Ancho (mm)')),
                ('cortado_a', models.CharField(blank=True, max_length=10, null=True)),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ensamblado', to='bandas.Banda')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ensamblado_created_by', to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ensamblados', to='productos.Producto')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ensamblado_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ValorCaracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('nomenclatura', models.CharField(blank=True, max_length=6, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandas.Caracteristica')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='costoensambladoblanda',
            unique_together=set([('aleta', 'empujador')]),
        ),
        migrations.AddField(
            model_name='banda',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_color', to='bandas.ValorCaracteristica'),
        ),
        migrations.AddField(
            model_name='banda',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banda_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='banda',
            name='empujador_tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_tipo_empujador', to='bandas.ValorCaracteristica', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='banda',
            name='ensamblaje',
            field=models.ManyToManyField(through='bandas.Ensamblado', to='productos.Producto'),
        ),
        migrations.AddField(
            model_name='banda',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_fabricante', to='bandas.ValorCaracteristica'),
        ),
        migrations.AddField(
            model_name='banda',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_material', to='bandas.ValorCaracteristica'),
        ),
        migrations.AddField(
            model_name='banda',
            name='material_varilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_material_varilla', to='bandas.ValorCaracteristica'),
        ),
        migrations.AddField(
            model_name='banda',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_serie', to='bandas.ValorCaracteristica'),
        ),
        migrations.AddField(
            model_name='banda',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandas_con_tipo', to='bandas.ValorCaracteristica'),
        ),
        migrations.AddField(
            model_name='banda',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banda_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='valorcaracteristica',
            unique_together=set([('caracteristica', 'nomenclatura'), ('caracteristica', 'nombre')]),
        ),
    ]
