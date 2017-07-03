# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-16 20:01


import autoslug.fields
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0073_auto_20170616_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=1024, populate_from=b'get_full_name', unique=True),
        ),
        migrations.AlterField(
            model_name='bppuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='jednostka',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'nazwa', unique=True),
        ),
        migrations.AlterField(
            model_name='uczelnia',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'skrot', unique=True),
        ),
        migrations.AlterField(
            model_name='wydzial',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=512, populate_from=b'nazwa', unique=True),
        ),
        migrations.AlterField(
            model_name='zrodlo',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'nazwa', unique=True),
        ),
    ]
