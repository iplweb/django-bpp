# Generated by Django 3.0.4 on 2020-04-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0209_auto_20200421_0013"),
    ]

    operations = [
        migrations.AddField(
            model_name="uczelnia",
            name="sortuj_jednostki_alfabetycznie",
            field=models.BooleanField(
                default=True,
                help_text="Jeżeli ustawione na 'FAŁSZ', sortowanie jednostek będzie odbywało się ręcznie \n        tzn za pomocą ustalonej przez administratora systemu kolejności. ",
            ),
        ),
    ]
