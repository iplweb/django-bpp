# Generated by Django 3.0.9 on 2020-10-07 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0223_auto_20200812_1930"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="element_repozytorium",
            options={
                "verbose_name": "element repozytorium",
                "verbose_name_plural": "elementy repozytorium",
            },
        ),
        migrations.CreateModel(
            name="Ukryj_Status_Korekty",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status_korekty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bpp.Status_Korekty",
                    ),
                ),
                (
                    "uczelnia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bpp.Uczelnia"
                    ),
                ),
            ],
            options={"unique_together": {("uczelnia", "status_korekty")},},
        ),
    ]
