# Generated by Django 2.1.7 on 2019-07-09 20:46

from django.db import migrations

from bpp.migration_util import load_custom_sql


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0166_auto_20190708_0022'),
    ]

    operations = [
        migrations.RunPython(
            lambda *args, **kw: load_custom_sql("0167_dyscyplina_change_trigger_fix")
        ),
    ]