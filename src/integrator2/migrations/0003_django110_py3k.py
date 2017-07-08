# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-08 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrator2', '0002_auto_20160124_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaministerialnaintegration',
            name='file',
            field=models.FileField(upload_to='integrator2', verbose_name='Plik'),
        ),
        migrations.AlterField(
            model_name='listaministerialnaintegration',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nazwa pliku'),
        ),
        migrations.AlterField(
            model_name='listaministerialnaintegration',
            name='status',
            field=models.IntegerField(choices=[(0, 'dodany'), (1, 'w trakcie analizy'), (2, 'przetworzony'), (3, 'przetworzony z błędami')], default=0),
        ),
    ]
