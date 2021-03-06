# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-08 12:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import import_dyscyplin.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Import_Dyscyplin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('plik', models.FileField(upload_to='')),
                ('rok', models.IntegerField(default=import_dyscyplin.models.obecny_rok)),
                ('stan', django_fsm.FSMField(choices=[('nowy', 'nowy'), ('przeanalizowany', 'przeanalizowany'), ('błędny', 'błędny'), ('dyscypliny zmatchowane', 'dyscypliny zmatchowane'), ('wydziały zmatchowane', 'wydziały zmatchowane'), ('jednostki zmatchowane', 'jednostki zmatchowane'), ('autorzy zmatchowani', 'autorzy zmatchowani'), ('plik zintegrowany', 'plik zintegrowany')], default='nowy', max_length=50, protected=True)),
                ('bledny', models.BooleanField(default=False)),
                ('info', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
