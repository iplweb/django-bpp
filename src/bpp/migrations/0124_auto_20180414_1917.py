# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0123_kod_dyscyplin'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='autor_dyscyplina',
            unique_together=set([('rok', 'autor')]),
        ),
    ]
