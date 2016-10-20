# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import usuarios.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil_cliente', to='empresas.Empresa')),
            ],
            options={
                'verbose_name_plural': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_contacto', models.CharField(max_length=12)),
                ('extencion', models.CharField(max_length=10)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to=usuarios.models.colaborador_upload_to, validators=[usuarios.models.Colaborador.validate_image])),
            ],
            options={
                'verbose_name_plural': 'colaboradores',
            },
        ),
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('I', 'Colaborador'), ('E', 'Cliente')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_extendido', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='colaborador',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='colaborador', to='usuarios.UserExtended'),
        ),
        migrations.AddField(
            model_name='clienteempresa',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='cliente_empresa', to='usuarios.UserExtended'),
        ),
    ]
