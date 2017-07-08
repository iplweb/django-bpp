# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-08 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0079_wydzial_skrot_nazwy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wydzial',
            name='skrot',
            field=models.CharField(help_text='Skrót nazwy wydziału, wersja minimalna, np. "WL"', max_length=10, unique=True, verbose_name='Skrót'),
        ),
    ]
