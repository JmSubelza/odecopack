# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20160910_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('numero', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
