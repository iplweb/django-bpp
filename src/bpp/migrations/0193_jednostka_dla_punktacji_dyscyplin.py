# Generated by Django 2.2.7 on 2020-01-06 15:53

from django.db import migrations, models
import django.db.models.deletion

from bpp.models import Uczelnia

class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0192_auto_20191107_0853'),
    ]

    operations = [
        migrations.RunSQL("DELETE FROM bpp_cache_punktacja_autora;"),
        migrations.AddField(
            model_name='cache_punktacja_autora',
            name='jednostka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bpp.Jednostka'),
            preserve_default=False,
        ),
    ]
