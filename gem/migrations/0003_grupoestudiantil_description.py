# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gem', '0002_auto_20160310_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupoestudiantil',
            name='description',
            field=models.TextField(default='Descripcion', verbose_name='Descripcion'),
        ),
    ]
