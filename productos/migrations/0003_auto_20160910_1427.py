# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20160910_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='referencia',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
