# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-24 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0141_konferencja_typ_konferencji'),
    ]

    operations = [
        migrations.AddField(
            model_name='uczelnia',
            name='wydruk_logo',
            field=models.BooleanField(default=False, verbose_name='Pokazuj logo na wydrukach'),
        ),
        migrations.AddField(
            model_name='uczelnia',
            name='wydruk_parametry_zapytania',
            field=models.BooleanField(default=True, verbose_name='Pokazuj parametry zapytania na wydrukach'),
        ),
        migrations.AlterField(
            model_name='konferencja',
            name='typ_konferencji',
            field=models.SmallIntegerField(blank=True, choices=[(1, '🚆 krajowa'), (2, '✈ ️międzynarodowa'), (3, '🚲 lokalna')], null=True),
        ),
    ]
