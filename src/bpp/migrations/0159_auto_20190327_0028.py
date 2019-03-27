# Generated by Django 2.1.7 on 2019-03-26 23:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0158_merge_20190325_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='orcid',
            field=models.CharField(blank=True, help_text='Open Researcher and Contributor ID, vide http://www.orcid.org', max_length=19, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='orcid_invalid_format', message='Identyfikator ORCID to 4 grupy po 4 cyfry w każdej, oddzielone myślnikami', regex='^\\d\\d\\d\\d-\\d\\d\\d\\d-\\d\\d\\d\\d-\\d\\d\\d(\\d|X)$')], verbose_name='Identyfikator ORCID'),
        ),
    ]
