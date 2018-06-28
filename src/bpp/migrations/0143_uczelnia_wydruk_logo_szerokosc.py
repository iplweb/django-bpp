# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0142_auto_20180624_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='uczelnia',
            name='wydruk_logo_szerokosc',
            field=models.BooleanField(default=250, help_text='Podaj wartość w pikselach. Wysokość zostanie przeskalowanaproporcjonalnie. ', verbose_name='Szerokość logo na wydrukach'),
        ),
    ]
