# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-08 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celeryui', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='report'),
        ),
    ]
