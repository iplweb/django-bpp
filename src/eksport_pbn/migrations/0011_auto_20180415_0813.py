# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eksport_pbn', '0010_auto_20170721_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plikeksportupbn',
            name='do_roku',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plikeksportupbn',
            name='od_roku',
            field=models.IntegerField(),
        ),
    ]