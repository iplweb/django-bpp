# Generated by Django 3.0.11 on 2021-01-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0229_nowe_sumy_status_korekty"),
    ]

    operations = [
        migrations.AddField(
            model_name="uczelnia",
            name="metoda_do_roku_formularze",
            field=models.CharField(
                choices=[
                    ("jan_prev_then_current", "do stycznia poprzedni, potem obecny"),
                    ("max_rec", "najwiekszy rok rekordu w bazie"),
                ],
                default="jan_prev_then_current",
                help_text="Decyduje o sposobie wyświetlania maksymalnej daty 'Do roku' w formularzach. ",
                max_length=30,
                verbose_name="Data w polu 'do roku' w formularzach",
            ),
        ),
    ]
