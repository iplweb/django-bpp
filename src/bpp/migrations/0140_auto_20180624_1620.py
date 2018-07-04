# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-24 14:20
from __future__ import unicode_literals

import bpp.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0139_uczelnia_pokazuj_liczbe_cytowan_na_stronie_autora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konferencja',
            name='baza_inna',
            field=models.CharField(blank=True, help_text='Wpisz listę innych baz czasopism i abstraktów, w których indeksowana była ta konferencja. Rozdziel średnikiem.', max_length=200, null=True, verbose_name='Indeksowana w...'),
        ),
        migrations.AlterField(
            model_name='uczelnia',
            name='pokazuj_raport_jednostek',
            field=bpp.models.fields.OpcjaWyswietlaniaField(choices=[('always', 'zawsze'), ('logged-in', 'tylko dla zalogowanych'), ('never', 'nigdy')], default='logged-in', max_length=50, verbose_name='Pokazuj raport jednostek'),
        ),
        migrations.AlterField(
            model_name='uczelnia',
            name='pokazuj_raport_wydzialow',
            field=bpp.models.fields.OpcjaWyswietlaniaField(choices=[('always', 'zawsze'), ('logged-in', 'tylko dla zalogowanych'), ('never', 'nigdy')], default='logged-in', max_length=50, verbose_name='Pokazuj raport wydziałów'),
        ),
    ]