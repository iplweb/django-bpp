# Generated by Django 2.1.7 on 2019-08-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0171_auto_20190806_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poziom_wydawcy',
            name='rok',
            field=models.IntegerField(db_index=True),
        ),
        migrations.RunSQL("CREATE INDEX bpp_wydawnictwo_zwarte_wydawca_rok ON bpp_wydawnictwo_zwarte(wydawca_id, rok)"),
        migrations.RunSQL("CREATE INDEX bpp_praca_doktorska_wydawca_rok ON bpp_praca_doktorska(wydawca_id, rok)"),
        migrations.RunSQL("CREATE INDEX bpp_praca_habilitacyjna_wydawca_rok ON bpp_praca_habilitacyjna(wydawca_id, rok)"),
    ]
