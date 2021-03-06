# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 11:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0087_pokazuj_ic_pkt_wew'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='orcid',
            field=models.CharField(blank=True, help_text='Open Researcher and Contributor ID, vide http://www.orcid.org', max_length=19, null=True, validators=[django.core.validators.RegexValidator(code='orcid_invalid_format', message='Identyfikator ORCID to 4 grupy po 4 cyfry w każdej, oddzielone myślnikami', regex='^\\d\\d\\d\\d-\\d\\d\\d\\d-\\d\\d\\d\\d-\\d\\d\\d\\d$')], verbose_name='Identyfikator ORCID'),
        ),
    ]
