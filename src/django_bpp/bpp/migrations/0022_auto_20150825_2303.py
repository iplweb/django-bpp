# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def dodaj_dane(apps, schema_editor):
    Jezyk = apps.get_model('bpp', 'Jezyk')

    ang, created = Jezyk.objects.get_or_create(skrot='ang.', nazwa='angielski')
    ang.skrot_dla_pbn = 'EN'
    ang.save()

    pl, created = Jezyk.objects.get_or_create(skrot='pol.', nazwa='polski')
    pl.skrot_dla_pbn = 'PL'
    pl.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0021_auto_20150825_2301'),
    ]

    operations = [
        migrations.RunPython(dodaj_dane)
    ]
