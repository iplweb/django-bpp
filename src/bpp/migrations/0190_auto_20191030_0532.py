# Generated by Django 2.1.10 on 2019-10-30 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0189_auto_20191027_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='praca_doktorska',
            name='pmc_id',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='PubMed Central ID'),
        ),
        migrations.AddField(
            model_name='praca_habilitacyjna',
            name='pmc_id',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='PubMed Central ID'),
        ),
        migrations.AddField(
            model_name='wydawnictwo_ciagle',
            name='pmc_id',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='PubMed Central ID'),
        ),
        migrations.AddField(
            model_name='wydawnictwo_zwarte',
            name='pmc_id',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='PubMed Central ID'),
        ),
    ]
