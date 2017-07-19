# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-19 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0095_issn_dla_zwartego'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='bppuser',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='jednostka',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='konferencja',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='praca_doktorska',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='praca_habilitacyjna',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='uczelnia',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_ciagle',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='wydawnictwo_zwarte',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='wydzial',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
        migrations.AlterField(
            model_name='zrodlo',
            name='adnotacje',
            field=models.TextField(blank=True, db_index=True, default='', help_text='Pole do użytku wewnętrznego -\n        wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych\n        dla użytkowników końcowych.'),
        ),
    ]
