# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-08 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_dyscyplin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='import_dyscyplin',
            name='web_page_uid',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
