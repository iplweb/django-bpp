# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_dyscyplin', '0010_auto_20180415_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='import_dyscyplin_row',
            name='nazwa_jednostki',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='import_dyscyplin_row',
            name='nazwa_wydzialu',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]