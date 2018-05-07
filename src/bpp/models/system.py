# -*- encoding: utf-8 -*-

"""
Małe klasy pomocnicze dla całego systemu
"""

from django.db import models
from django.utils import six

from bpp.models import const
from bpp.models.abstract import ModelZNazwa, NazwaISkrot

NAZWY_PRIMO = [
    "",
    "Artykuł",
    "Książka",
    "Zasób tekstowy",
    "Rozprawa naukowa",
    "Recenzja",
    "Artykuł prasowy",
    "Rozdział",
    "Czasopismo",
    "Dane badawcze",
    "Materiał konferencyjny",
    "Obraz",
    "Baza",
    "Zestaw danych statystycznych",
    "Multimedia",
    "Inny"
]

NAZWY_PRIMO = list(zip(NAZWY_PRIMO, NAZWY_PRIMO))

RODZAJE_DOKUMENTOW_PBN = [("article", "Artykuł"),
                          ("book", "Książka"),
                          ("chapter", "Rozdział")]

@six.python_2_unicode_compatible
class Charakter_PBN(models.Model):
    wlasciwy_dla = models.CharField(
        "Właściwy dla...",
        max_length=20,
        choices=RODZAJE_DOKUMENTOW_PBN)
    identyfikator = models.CharField(max_length=100)
    opis = models.CharField(max_length=500)
    help_text = models.TextField(blank=True)

    class Meta:
        ordering = ['identyfikator']
        verbose_name = 'Charakter PBN'
        verbose_name_plural = 'Charaktery PBN'

    def __str__(self):
        return self.opis


class Charakter_Formalny(NazwaISkrot):
    """Bazowa klasa dla charakterów formalnych. """

    publikacja = models.BooleanField(help_text="""Jest charakterem dla publikacji""", default=False)
    streszczenie = models.BooleanField(help_text="""Jest charakterem dla streszczeń""", default=False)

    nazwa_w_primo = models.CharField("Nazwa w Primo", max_length=100, help_text="""
    Nazwa charakteru formalnego w wyszukiwarce Primo, eksponowana przez OAI-PMH. W przypadku,
    gdy to pole jest puste, prace o danym charakterze formalnym nie będą udostępniane przez
    protokół OAI-PMH.
    """, blank=True, default="", choices=NAZWY_PRIMO, db_index=True)

    charakter_pbn = models.ForeignKey(Charakter_PBN,
                                      verbose_name="Charakter PBN",
                                      blank=True, null=True, default=None,
                                      help_text="""Wartość wybrana w tym polu zostanie użyta jako zawartość tagu <is>
                                      w plikach eksportu do PBN""")

    artykul_pbn = models.BooleanField(verbose_name="Artykuł w PBN", help_text="""Wydawnictwa ciągłe posiadające
     ten charakter formalny zostaną włączone do eksportu PBN jako artykuły""", default=False)
    ksiazka_pbn = models.BooleanField(verbose_name="Książka w PBN", help_text="""Wydawnictwa zwarte posiadające ten
    charakter formalny zostaną włączone do eksportu PBN jako ksiażki""", default=False)
    rozdzial_pbn = models.BooleanField(verbose_name="Rozdział w PBN", help_text="""Wydawnictwa zwarte posiadające ten
    charakter formalny zostaną włączone do eksportu PBN jako rozdziały""", default=False)

    class Meta:
        ordering = ['nazwa']
        app_label = 'bpp'
        verbose_name = "charakter formalny"
        verbose_name_plural = 'charaktery formalne'


class Status_Korekty(ModelZNazwa):
    class Meta:
        verbose_name = 'status korekty'
        verbose_name_plural = 'statusy korekty'
        app_label = 'bpp'


class Zrodlo_Informacji(ModelZNazwa):
    class Meta:
        verbose_name = 'źródło informacji o bibliografii'
        verbose_name_plural = 'źródła informacji o bibliografii'
        app_label = 'bpp'


@six.python_2_unicode_compatible
class Typ_Odpowiedzialnosci(NazwaISkrot):
    typ_ogolny = models.SmallIntegerField(
        "Ogólny typ odpowiedzialności",
        choices=[
            (const.TO_AUTOR, "autor"),
            (const.TO_REDAKTOR, "redaktor"),
            (const.TO_INNY, "inny"),
            (const.TO_TLUMACZ, "tłumacz"),
            (const.TO_KOMENTATOR, "komentator"),
            (const.TO_RECENZENT, "recenzent"),
            (const.TO_OPRACOWAL, "opracował")
    ],
        default=const.TO_AUTOR,
        help_text="""Pole to jest używane celem rozróżniania typu odpowiedzialności
        na cele eksportu do PBN (autor i redaktor) oraz może być też wykorzystywane
        np. w raportach autorów i jednostek. 
        """,
        db_index=True
    )

    class Meta:
        verbose_name = 'typ odpowiedzialności'
        verbose_name_plural = 'typy odpowiedzialności'
        ordering = ['nazwa']
        app_label = 'bpp'

    def __str__(self):
        return self.nazwa


class Jezyk(NazwaISkrot):
    skrot_dla_pbn = models.CharField(max_length=10, verbose_name="Skrót dla PBN", help_text="""
    Skrót nazwy języka używany w plikach eksportu do PBN.""", blank=True)

    class Meta:
        verbose_name = 'język'
        verbose_name_plural = 'języki'
        ordering = ['nazwa']
        app_label = 'bpp'

    def get_skrot_dla_pbn(self):
        if self.skrot_dla_pbn:
            return self.skrot_dla_pbn

        return self.skrot


class Typ_KBN(NazwaISkrot):
    artykul_pbn = models.BooleanField("Artykuł w PBN", help_text="""Wydawnictwa ciągłe posiadające
    ten typ KBN zostaną włączone do eksportu PBN jako artykuły""", default=False)


    charakter_pbn = models.ForeignKey(
        Charakter_PBN,
        verbose_name="Charakter PBN",
        blank=True,
        null=True,
        default=None,
        help_text="""Wartość wybrana w tym polu zostanie użyta jako 
        fallback, tzn. jeżeli dla charakteru formalnego danego rekordu nie 
        określono odpowiedniego charakteru PBN, to zostanie użyta wartość 
        tego pola, o ile wybrana. """
    )

    class Meta:
        verbose_name = 'typ KBN'
        verbose_name_plural = 'typy KBN'
        ordering = ['nazwa']
        app_label = 'bpp'


class Rodzaj_Prawa_Patentowego(ModelZNazwa):
    class Meta:
        verbose_name = "rodzaj prawa patentowego"
        verbose_name_plural = "rodzaje praw patentowych"
        ordering = ['nazwa',]
        app_label = 'bpp'


class Zewnetrzna_Baza_Danych(NazwaISkrot):
    class Meta:
        verbose_name = "zewnętrzna baza danych"
        verbose_name_plural = "zenwętrzne bazy danych"
        ordering = ['nazwa', ]
        app_label = 'bpp'
