# Generated by Django 2.1.13 on 2019-11-03 14:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aut',
            fields=[
                ('idt_aut', models.TextField(primary_key=True, serialize=False)),
                ('imiona', models.TextField(blank=True, null=True)),
                ('nazwisko', models.TextField(blank=True, null=True)),
                ('ref', models.TextField(blank=True, null=True)),
                ('kad_nr', models.TextField(blank=True, null=True)),
                ('tel', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('www', models.TextField(blank=True, null=True)),
                ('imiona_bz', models.TextField(blank=True, null=True)),
                ('nazwisk_bz', models.TextField(blank=True, null=True)),
                ('tytul', models.TextField(blank=True, null=True)),
                ('stanowisko', models.TextField(blank=True, null=True)),
                ('prac_od', models.TextField(blank=True, null=True)),
                ('dat_zwol', models.TextField(blank=True, null=True)),
                ('fg', models.TextField(blank=True, null=True)),
                ('dop', models.TextField(blank=True, null=True)),
                ('nr_ewid', models.TextField(blank=True, null=True)),
                ('kad_s_jed', models.TextField(blank=True, null=True)),
                ('pbn_id', models.TextField(blank=True, null=True)),
                ('res_id', models.TextField(blank=True, null=True)),
                ('scop_id', models.TextField(blank=True, null=True)),
                ('orcid_id', models.TextField(blank=True, null=True)),
                ('exp_id', models.TextField(blank=True, null=True)),
                ('polon_id', models.TextField(blank=True, null=True)),
                ('usos_id', models.TextField(blank=True, null=True)),
                ('udf_id', models.TextField(blank=True, null=True)),
                ('control', models.TextField(blank=True, null=True)),
                ('uwagi', models.TextField(blank=True, null=True)),
                ('graf', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany autor',
                'verbose_name_plural': 'zaimportowani autorzy',
                'db_table': 'import_dbf_aut',
                'ordering': ('nazwisko', 'imiona'),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='B_A',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('lp', models.TextField(blank=True, null=True)),
                ('wspz', models.TextField(blank=True, null=True)),
                ('pkt_dod', models.TextField(blank=True, null=True)),
                ('wspz2', models.TextField(blank=True, null=True)),
                ('pkt2_dod', models.TextField(blank=True, null=True)),
                ('afiliacja', models.TextField(blank=True, null=True)),
                ('odp', models.TextField(blank=True, null=True)),
                ('study_ga', models.TextField(blank=True, null=True)),
                ('tytul', models.TextField(blank=True, null=True)),
                ('stanowisko', models.TextField(blank=True, null=True)),
                ('uwagi', models.TextField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_b_a',
                'ordering': ('idt__tytul_or_s', 'lp'),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='B_B',
            fields=[
                ('idt', models.TextField(primary_key=True, serialize=False)),
                ('lp', models.TextField(blank=True, null=True)),
                ('idt_bazy', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_b_b',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='B_E',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idt', models.IntegerField()),
                ('lp', models.TextField(blank=True, null=True)),
                ('idt_eng', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_b_e',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='B_L',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idt', models.IntegerField()),
                ('idt_l', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_b_l',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='B_N',
            fields=[
                ('idt', models.TextField(primary_key=True, serialize=False)),
                ('lp', models.TextField(blank=True, null=True)),
                ('idt_pbn', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_b_n',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='B_P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idt', models.IntegerField()),
                ('lp', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_b_p',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='B_U',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowane dane OA rekordu',
                'verbose_name_plural': 'zaimportowane dane OA rekordow',
                'db_table': 'import_dbf_b_u',
                'ordering': ('idt', 'comm'),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dys',
            fields=[
                ('orcid_id', models.TextField(primary_key=True, serialize=False)),
                ('a_n', models.TextField(blank=True, null=True)),
                ('a_w_etatu', models.TextField(blank=True, null=True)),
                ('a_dysc_1', models.TextField(blank=True, null=True)),
                ('a_dysc_2', models.TextField(blank=True, null=True)),
                ('a_dysc_1_e', models.TextField(blank=True, null=True)),
                ('a_dysc_2_e', models.TextField(blank=True, null=True)),
                ('b_n', models.TextField(blank=True, null=True)),
                ('b_w_etatu', models.TextField(blank=True, null=True)),
                ('b_dysc_1', models.TextField(blank=True, null=True)),
                ('b_dysc_2', models.TextField(blank=True, null=True)),
                ('b_dysc_1_e', models.TextField(blank=True, null=True)),
                ('b_dysc_2_e', models.TextField(blank=True, null=True)),
                ('c_n', models.TextField(blank=True, null=True)),
                ('c_w_etatu', models.TextField(blank=True, null=True)),
                ('c_dysc_1', models.TextField(blank=True, null=True)),
                ('c_dysc_2', models.TextField(blank=True, null=True)),
                ('c_dysc_1_e', models.TextField(blank=True, null=True)),
                ('c_dysc_2_e', models.TextField(blank=True, null=True)),
                ('d_n', models.TextField(blank=True, null=True)),
                ('d_w_etatu', models.TextField(blank=True, null=True)),
                ('d_dysc_1', models.TextField(blank=True, null=True)),
                ('d_dysc_2', models.TextField(blank=True, null=True)),
                ('d_dysc_1_e', models.TextField(blank=True, null=True)),
                ('d_dysc_2_e', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowana dyscyplina pracownika',
                'verbose_name_plural': 'zaimportowane dyscypliny pracowników',
                'db_table': 'import_dbf_dys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_ext',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ixb',
            fields=[
                ('idt_bazy', models.TextField(primary_key=True, serialize=False)),
                ('baza', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowana baza',
                'verbose_name_plural': 'zaimportowane bazy',
                'db_table': 'import_dbf_ixb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ixe',
            fields=[
                ('idt_eng', models.TextField(primary_key=True, serialize=False)),
                ('haslo', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowane hasło naukowe',
                'verbose_name_plural': 'zaimportowane hasła naukowe',
                'db_table': 'import_dbf_ixe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ixn',
            fields=[
                ('idt_pbn', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('pbn', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany identyfikator PBN',
                'verbose_name_plural': 'zaimportowane identyfikatory PBN',
                'db_table': 'import_dbf_ixn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ixp',
            fields=[
                ('idt_pol', models.TextField(primary_key=True, serialize=False)),
                ('haslo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_ixp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='J_H',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rok', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany rekord historii jednostek',
                'verbose_name_plural': 'zaimportowane rekordy historii jednostek',
                'db_table': 'import_dbf_j_h',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jed',
            fields=[
                ('idt_jed', models.TextField(primary_key=True, serialize=False)),
                ('nr', models.TextField(blank=True, null=True)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('wyd_skrot', models.TextField(blank=True, null=True)),
                ('sort', models.TextField(blank=True, null=True)),
                ('to_print', models.TextField(blank=True, null=True)),
                ('to_print2', models.TextField(blank=True, null=True)),
                ('to_print3', models.TextField(blank=True, null=True)),
                ('to_print4', models.TextField(blank=True, null=True)),
                ('to_print5', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('www', models.TextField(blank=True, null=True)),
                ('id_u', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_jed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jer',
            fields=[
                ('nr', models.TextField(primary_key=True, serialize=False)),
                ('od_roku', models.TextField(blank=True, null=True)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('wyd_skrot', models.TextField(blank=True, null=True)),
                ('id_u', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_jer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jez',
            fields=[
                ('skrot', models.TextField(primary_key=True, serialize=False)),
                ('nazwa', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany język',
                'verbose_name_plural': 'zaimportowane języki',
                'db_table': 'import_dbf_jez',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kad',
            fields=[
                ('nr', models.TextField(primary_key=True, serialize=False)),
                ('na', models.TextField(blank=True, null=True)),
                ('im1', models.TextField(blank=True, null=True)),
                ('im2', models.TextField(blank=True, null=True)),
                ('s_jed', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_kad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kbn',
            fields=[
                ('idt_kbn', models.TextField(primary_key=True, serialize=False)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('to_print', models.TextField(blank=True, null=True)),
                ('to_print2', models.TextField(blank=True, null=True)),
                ('to_print3', models.TextField(blank=True, null=True)),
                ('to_print4', models.TextField(blank=True, null=True)),
                ('to_print5', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany typ KBN',
                'verbose_name_plural': 'zaimportowane typy KBN',
                'db_table': 'import_dbf_kbn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kbr',
            fields=[
                ('idt_kbr', models.TextField(primary_key=True, serialize=False)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('to_print', models.TextField(blank=True, null=True)),
                ('to_print2', models.TextField(blank=True, null=True)),
                ('to_print3', models.TextField(blank=True, null=True)),
                ('to_print4', models.TextField(blank=True, null=True)),
                ('to_print5', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany rekord KBR',
                'verbose_name_plural': 'zaimportowane rekordy KBR',
                'db_table': 'import_dbf_kbr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ldy',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('dziedzina', models.TextField(blank=True, null=True)),
                ('dyscyplina', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowana dziedzina',
                'verbose_name_plural': 'zaimportowane dziedziny',
                'db_table': 'import_dbf_ldy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rok', models.TextField(blank=True, null=True)),
                ('kategoria', models.TextField(blank=True, null=True)),
                ('numer', models.TextField(blank=True, null=True)),
                ('tytul', models.TextField(blank=True, null=True)),
                ('issn', models.TextField(blank=True, null=True)),
                ('eissn', models.TextField(blank=True, null=True)),
                ('punkty', models.TextField(blank=True, null=True)),
                ('sobowtor', models.TextField(blank=True, null=True)),
                ('errissn', models.TextField(blank=True, null=True)),
                ('dblissn', models.TextField(blank=True, null=True)),
                ('dbltitul', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowana lista wydawców',
                'verbose_name_plural': 'zaimportowane listy wydawców',
                'db_table': 'import_dbf_lis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loc',
            fields=[
                ('ident', models.TextField(primary_key=True, serialize=False)),
                ('ext', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_loc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idt', models.TextField(blank=True, null=True)),
                ('idt_pbn', models.TextField(blank=True, null=True)),
                ('wyd_skrot', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_pba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pbb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep_f_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_pbb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pbc',
            fields=[
                ('idt', models.TextField(primary_key=True, serialize=False)),
                ('wyd_skrot', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_pbc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pbd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep_f_name', models.TextField(blank=True, null=True)),
                ('field_ignore_me', models.TextField(blank=True, db_column='_ignore_me', null=True)),
            ],
            options={
                'db_table': 'import_dbf_pbd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('kod_opisu', models.TextField(blank=True, null=True)),
                ('lp', models.PositiveSmallIntegerField()),
                ('tresc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany opis rekordu',
                'verbose_name_plural': 'zaimportowane opisy rekordow',
                'db_table': 'import_dbf_poz',
                'ordering': ('idt', 'kod_opisu', 'lp'),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('idt_pub', models.TextField(primary_key=True, serialize=False)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('to_print', models.TextField(blank=True, null=True)),
                ('to_print2', models.TextField(blank=True, null=True)),
                ('to_print3', models.TextField(blank=True, null=True)),
                ('to_print4', models.TextField(blank=True, null=True)),
                ('to_print5', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany charakter publikacji',
                'verbose_name_plural': 'zaimportowane charaktery publikacji',
                'db_table': 'import_dbf_pub',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rtf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idt', models.TextField(blank=True, null=True)),
                ('lp', models.TextField(blank=True, null=True)),
                ('len', models.TextField(blank=True, null=True)),
                ('rtf', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_rtf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='S_B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idt_sci', models.TextField(blank=True, null=True)),
                ('cit', models.TextField(blank=True, null=True)),
                ('doi', models.TextField(blank=True, null=True)),
                ('del_field', models.TextField(blank=True, db_column='del', null=True)),
                ('redaktor', models.TextField(blank=True, null=True)),
                ('dat_akt', models.TextField(blank=True, null=True)),
                ('autocyt', models.TextField(blank=True, null=True)),
                ('ut', models.TextField(blank=True, null=True)),
                ('ut0', models.TextField(blank=True, null=True)),
                ('uwagi', models.TextField(blank=True, null=True)),
                ('field_ignore_me', models.TextField(blank=True, db_column='_ignore_me', null=True)),
            ],
            options={
                'db_table': 'import_dbf_s_b',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sci',
            fields=[
                ('idt_sci', models.TextField(primary_key=True, serialize=False)),
                ('au', models.TextField(blank=True, null=True)),
                ('ti', models.TextField(blank=True, null=True)),
                ('src', models.TextField(blank=True, null=True)),
                ('ye', models.TextField(blank=True, null=True)),
                ('cont', models.TextField(blank=True, null=True)),
                ('ut', models.TextField(blank=True, null=True)),
                ('field_ignore_me', models.TextField(blank=True, db_column='_ignore_me', null=True)),
            ],
            options={
                'db_table': 'import_dbf_sci',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redaktor', models.TextField(blank=True, null=True)),
                ('file', models.TextField(blank=True, null=True)),
                ('login_t', models.TextField(blank=True, null=True)),
                ('logout_t', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_ses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowana wersja bazy',
                'verbose_name_plural': 'zaimportowane wersje bazy',
                'db_table': 'import_dbf_sys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usi',
            fields=[
                ('idt_usi', models.IntegerField(primary_key=True, serialize=False)),
                ('usm_f', models.TextField(blank=True, null=True)),
                ('usm_sf', models.TextField(blank=True, null=True)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowane źródło',
                'verbose_name_plural': 'zaimportowane źródła',
                'db_table': 'import_dbf_usi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wsx',
            fields=[
                ('idt_wsx', models.TextField(primary_key=True, serialize=False)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('wsp', models.TextField(blank=True, null=True)),
                ('field_ignore_me', models.TextField(blank=True, db_column='_ignore_me', null=True)),
            ],
            options={
                'db_table': 'import_dbf_wsx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wsy',
            fields=[
                ('idt_wsy', models.TextField(primary_key=True, serialize=False)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('wsp', models.TextField(blank=True, null=True)),
                ('field_ignore_me', models.TextField(blank=True, db_column='_ignore_me', null=True)),
            ],
            options={
                'db_table': 'import_dbf_wsy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wx2',
            fields=[
                ('idt_wsx', models.TextField(primary_key=True, serialize=False)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('wsp', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import_dbf_wx2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wyd',
            fields=[
                ('idt_wyd', models.TextField(primary_key=True, serialize=False)),
                ('skrot', models.TextField(blank=True, null=True)),
                ('nazwa', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'zaimportowany wydział',
                'verbose_name_plural': 'zaimportowane wydzialy',
                'db_table': 'import_dbf_wyd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bib',
            fields=[
                ('idt', models.IntegerField(primary_key=True, serialize=False)),
                ('tytul_or', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('zrodlo', models.TextField(blank=True, null=True)),
                ('szczegoly', models.TextField(blank=True, null=True)),
                ('uwagi', models.TextField(blank=True, null=True)),
                ('charakter', models.TextField(blank=True, null=True)),
                ('impact', models.TextField(blank=True, null=True)),
                ('redakcja', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('rok', models.TextField(blank=True, null=True)),
                ('sort', models.TextField(blank=True, null=True)),
                ('sort2', models.TextField(blank=True, null=True)),
                ('export', models.TextField(blank=True, null=True)),
                ('import_field', models.TextField(blank=True, db_column='import', null=True)),
                ('naz_imie', models.TextField(blank=True, null=True)),
                ('redaktor', models.TextField(blank=True, null=True)),
                ('redaktor0', models.TextField(blank=True, null=True)),
                ('tytul_or_s', models.TextField(blank=True, null=True)),
                ('title_s', models.TextField(blank=True, null=True)),
                ('zrodlo_s', models.TextField(blank=True, null=True)),
                ('szczegol_s', models.TextField(blank=True, null=True)),
                ('mem_fi_ext', models.TextField(blank=True, null=True)),
                ('dat_akt', models.TextField(blank=True, null=True)),
                ('kbn', models.TextField(blank=True, null=True)),
                ('kbr', models.TextField(blank=True, null=True)),
                ('afiliowana', models.TextField(blank=True, null=True)),
                ('recenzowan', models.TextField(blank=True, null=True)),
                ('jezyk', models.TextField(blank=True, null=True)),
                ('jezyk2', models.TextField(blank=True, null=True)),
                ('punkty_kbn', models.TextField(blank=True, db_column='pk', null=True)),
                ('x_skrot', models.TextField(blank=True, null=True)),
                ('wspx', models.TextField(blank=True, null=True)),
                ('x2_skrot', models.TextField(blank=True, null=True)),
                ('wspx2', models.TextField(blank=True, null=True)),
                ('y_skrot', models.TextField(blank=True, null=True)),
                ('wspy', models.TextField(blank=True, null=True)),
                ('wspq', models.TextField(blank=True, null=True)),
                ('ic', models.TextField(blank=True, null=True)),
                ('rok_inv', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('lf', models.TextField(blank=True, null=True)),
                ('rok_punkt', models.TextField(blank=True, null=True)),
                ('form', models.TextField(blank=True, null=True)),
                ('k_z', models.TextField(blank=True, null=True)),
                ('uwagi2', models.TextField(blank=True, null=True)),
                ('dat_utw', models.TextField(blank=True, null=True)),
                ('pun_wl', models.TextField(blank=True, null=True)),
                ('study_gr', models.TextField(blank=True, null=True)),
                ('sort_fixed', models.TextField(blank=True, null=True)),
                ('zaznacz_field', models.TextField(blank=True, db_column='zaznacz_', null=True)),
                ('idt2', models.TextField(blank=True, null=True)),
                ('pun_max', models.TextField(blank=True, null=True)),
                ('pun_erih', models.TextField(blank=True, null=True)),
                ('kwartyl', models.TextField(blank=True, null=True)),
                ('issn', models.TextField(blank=True, null=True)),
                ('eissn', models.TextField(blank=True, null=True)),
                ('wok_id', models.TextField(blank=True, null=True)),
                ('sco_id', models.TextField(blank=True, null=True)),
                ('mnsw_fixed', models.TextField(blank=True, null=True)),
                ('liczba_aut', models.TextField(blank=True, null=True)),
                ('pro_p_wydz', models.TextField(blank=True, null=True)),
                ('snip', models.TextField(blank=True, null=True)),
                ('sjr', models.TextField(blank=True, null=True)),
                ('cites', models.TextField(blank=True, null=True)),
                ('if5', models.TextField(blank=True, null=True)),
                ('lis_numer', models.TextField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('analyzed', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'zaimportowany rekord bibliografi',
                'verbose_name_plural': 'zaimportowane rekordy bibliografi',
                'db_table': 'import_dbf_bib',
            },
        ),
        migrations.CreateModel(
            name='Bib_Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elem_id', models.PositiveSmallIntegerField(db_index=True)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('source', models.CharField(max_length=10)),
                ('idt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_dbf.Bib')),
            ],
            options={
                'ordering': ('idt', 'source'),
            },
        ),
    ]
