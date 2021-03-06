# Generated by Django 3.0.11 on 2021-01-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0230_metoda_do_roku_uczelnia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ukryj_status_korekty",
            name="api",
            field=models.BooleanField(
                default=True,
                help_text="Dotyczy ukrywania prac w API JSON-REST oraz OAI-PMH",
                verbose_name="API",
            ),
        ),
        migrations.AlterField(
            model_name="ukryj_status_korekty",
            name="rankingi",
            field=models.BooleanField(default=True, verbose_name="Rankingi"),
        ),
        migrations.AlterField(
            model_name="ukryj_status_korekty",
            name="raporty",
            field=models.BooleanField(
                default=True,
                help_text="Ukrywa prace w raporcie autora, jednostki, uczelni",
                verbose_name="Raporty",
            ),
        ),
        migrations.AlterField(
            model_name="ukryj_status_korekty",
            name="sloty",
            field=models.BooleanField(
                default=True,
                help_text="Prace o wybranym statusie nie będą miały liczonych punktów i slotów w chwilizapisywania rekordu do bazy danych. Jeżeli zmieniasz to ustawienie dla prac które już są w bazie danych to ich punktacja zniknie z bazy w dniu następnym (skasowana zostanie podczas nocnego przeindeksowania bazy).",
                verbose_name="Raporty slotów",
            ),
        ),
    ]
