# -*- encoding: utf-8 -*-

"""
Klasy abstrakcyjne
"""
from datetime import datetime
from decimal import Decimal
from django.core.exceptions import ValidationError

from django.db import models
from django.utils import timezone
from djorm_pgfulltext.fields import VectorField
from lxml.etree import SubElement

from bpp.fields import YearField, DOIField
from bpp.models.util import ModelZOpisemBibliograficznym


class ModelZeZnakamiWydawniczymi(models.Model):

    liczba_znakow_wydawniczych = models.IntegerField(
        'Liczba znaków wydawniczych', blank=True, null=True,
        db_index=True)

    class Meta:
        abstract = True

class ModelZAdnotacjami(models.Model):
    """Zawiera adnotację  dla danego obiektu, czyli informacje, które
    użytkownik może sobie dowolnie uzupełnić.
    """
    ostatnio_zmieniony = models.DateTimeField(auto_now=True, null=True, db_index=True)

    adnotacje = models.TextField(help_text="""Pole do użytku wewnętrznego -
    wpisane tu informacje nie są wyświetlane na stronach WWW dostępnych
    dla użytkowników końcowych.""", null=True, blank=True, db_index=True)

    class Meta:
        abstract = True


class ModelZPBN_ID(models.Model):
    """Zawiera informacje o PBN_ID
    """
    pbn_id = models.IntegerField(
        verbose_name='Identyfikator PBN',
        help_text="Identyfikator w systemie Polskiej Bibliografii Naukowej (PBN)",
        null=True, blank=True, unique=True, db_index=True)

    class Meta:
        abstract = True


class ModelZNazwa(models.Model):
    """Nazwany model."""
    nazwa = models.CharField(max_length=512, unique=True)

    def __unicode__(self):
        return self.nazwa

    class Meta:
        abstract = True
        ordering = ['nazwa']


class NazwaISkrot(ModelZNazwa):
    """Model z nazwą i ze skrótem"""
    skrot = models.CharField(max_length=128, unique=True)

    class Meta:
        abstract = True


class NazwaWDopelniaczu(models.Model):
    nazwa_dopelniacz_field = models.CharField(
        u"Nazwa w dopełniaczu", max_length=512, null=True, blank=True)

    class Meta:
        abstract = True

    def nazwa_dopelniacz(self):
        if not hasattr(self, 'nazwa'):
            return self.nazwa_dopelniacz_field
        if self.nazwa_dopelniacz_field is None \
                or self.nazwa_dopelniacz_field == '':
            return self.nazwa
        return self.nazwa_dopelniacz_field


class ModelZISSN(models.Model):
    """Model z numerem ISSN oraz E-ISSN"""
    issn = models.CharField("ISSN", max_length=32, blank=True, null=True)
    e_issn = models.CharField("e-ISSN", max_length=32, blank=True, null=True)

    class Meta:
        abstract = True


class ModelZISBN(models.Model):
    """Model z numerem ISBN oraz E-ISBN"""
    isbn = models.CharField("ISBN", max_length=64, blank=True, null=True, db_index=True)
    e_isbn = models.CharField("E-ISBN", max_length=64, blank=True, null=True, db_index=True)

    class Meta:
        abstract = True


class ModelZInformacjaZ(models.Model):
    """Model zawierający pole 'Informacja z' - czyli od kogo została
    dostarczona informacja o publikacji (np. od autora, od redakcji)."""
    informacja_z = models.ForeignKey('Zrodlo_Informacji', null=True, blank=True)

    class Meta:
        abstract = True


class DwaTytuly(models.Model):
    """Model zawierający dwa tytuły: tytuł oryginalny pracy oraz tytuł
    przetłumaczony."""
    tytul_oryginalny = models.TextField("Tytuł oryginalny", db_index=True)
    tytul = models.TextField("Tytuł", null=True, blank=True, db_index=True)

    class Meta:
        abstract = True


class ModelZeStatusem(models.Model):
    """Model zawierający pole statusu korekty, oraz informację, czy
    punktacja została zweryfikowana."""
    status_korekty = models.ForeignKey('Status_Korekty', default=1)

    class Meta:
        abstract = True


class ModelZRokiem(models.Model):
    """Model zawierający pole "Rok" """
    rok = YearField(
        help_text="""Rok uwzględniany przy wyszukiwaniu i raportach
        KBN/MNiSW)""", db_index=True)

    class Meta:
        abstract = True


class ModelZWWW(models.Model):
    """Model zawierający adres strony WWW"""
    www = models.URLField("Adres WWW (płatny dostęp)", max_length=1024, blank=True, null=True)
    dostep_dnia = models.DateField(
        "Dostęp dnia (płatny dostęp)", blank=True, null=True,
        help_text="""Data dostępu do strony WWW.""")

    public_www = models.URLField("Adres WWW (wolny dostęp)", max_length=2048, blank=True, null=True)
    public_dostep_dnia = models.DateField(
        "Dostęp dnia (wolny dostęp)", blank=True, null=True,
        help_text="""Data wolnego dostępu do strony WWW.""")

    class Meta:
        abstract = True


class ModelZPubmedID(models.Model):
    pubmed_id = models.BigIntegerField("PubMed ID", blank=True, null=True, help_text="Identyfikator PubMed (PMID)")

    class Meta:
        abstract = True

class ModelZDOI(models.Model):
    doi = DOIField("DOI", null=True, blank=True, db_index=True)

    class Meta:
        abstract = True


class ModelAfiliowanyRecenzowany(models.Model):
    """Model zawierający informacje o afiliowaniu/recenzowaniu pracy."""
    afiliowana = models.BooleanField(default=False, db_index=True)
    recenzowana = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True


class ModelPunktowanyBaza(models.Model):
    impact_factor = models.DecimalField(
        max_digits=6, decimal_places=3,
        default=Decimal("0.000"), db_index=True)
    punkty_kbn = models.DecimalField(
        "Punkty KBN", max_digits=6, decimal_places=2,
        default=Decimal("0.00"), db_index=True)
    index_copernicus = models.DecimalField(
        "Index Copernicus", max_digits=6, decimal_places=2,
        default=Decimal("0.00"), db_index=True)
    punktacja_wewnetrzna = models.DecimalField(
        "Punktacja wewnętrzna", max_digits=6, decimal_places=2,
        default=Decimal("0.00"), db_index=True)

    kc_impact_factor = models.DecimalField(
        "KC: Impact factor", max_digits=6, decimal_places=2,
        default=None, blank=True, null=True, help_text="""Jeżeli wpiszesz
        wartość w to pole, to zostanie ona użyta w raporcie dla Komisji
        Centralnej w punkcie IXa tego raportu.""", db_index=True)
    kc_punkty_kbn = models.DecimalField(
        "KC: Punkty KBN", max_digits=6, decimal_places=2,
        default=None, blank=True, null=True, help_text="""Jeżeli wpiszesz
        wartość w to pole, to zostanie ona użyta w raporcie dla Komisji
        Centralnej w punkcie IXa i IXb tego raportu.""", db_index=True)
    kc_index_copernicus = models.DecimalField(
        "KC: Index Copernicus", max_digits=6, decimal_places=2,
        default=None, blank=True, null=True, help_text="""Jeżeli wpiszesz
        wartość w to pole, to zostanie ona użyta w raporcie dla Komisji
        Centralnej w punkcie IXa i IXb tego raportu.""")

    class Meta:
        abstract = True


class ModelPunktowany(ModelPunktowanyBaza):
    """Model zawiereający informację o punktacji."""

    weryfikacja_punktacji = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def ma_punktacje(self):
        """Zwraca 'True', jeżeli ten rekord ma jakąkolwiek punktację,
        czyli jeżeli dowolne z jego pól ma wartość nie-zerową"""

        for pole in POLA_PUNKTACJI:
            f = getattr(self, pole)

            if f is None:
                continue

            if type(f) == Decimal:
                if not f.is_zero():
                    return True
            else:
                if f != 0:
                    return True

        return False


POLA_PUNKTACJI = [
    x.name for x in ModelPunktowany._meta.fields
    if x.name not in ['weryfikacja_punktacji', ]]

from bpp.models.system import Charakter_Formalny


class ModelTypowany(models.Model):
    """Model zawierający typ KBN oraz język."""
    typ_kbn = models.ForeignKey('Typ_KBN', verbose_name="Typ KBN")
    jezyk = models.ForeignKey('Jezyk', verbose_name="Język")

    class Meta:
        abstract = True


class BazaModeluOdpowiedzialnosciAutorow(models.Model):
    """Bazowa klasa dla odpowiedzialności autorów (czyli dla przypisania
    autora do czegokolwiek innego). Zawiera wszystkie informacje dla autora,
    czyli: powiązanie ForeignKey, jednostkę, rodzaj zapisu nazwiska, ale
    nie zawiera podstawowej informacji, czyli powiązania"""
    autor = models.ForeignKey('Autor')
    jednostka = models.ForeignKey('Jednostka')
    kolejnosc = models.IntegerField('Kolejność', default=0)
    typ_odpowiedzialnosci = models.ForeignKey('Typ_Odpowiedzialnosci',
                                              verbose_name="Typ odpowiedzialności")
    zapisany_jako = models.CharField(max_length=512)

    class Meta:
        abstract = True
        ordering = ('kolejnosc', 'typ_odpowiedzialnosci__skrot')

    def __unicode__(self):
        return unicode(self.autor) + u" - " + unicode(self.jednostka.skrot)

    # XXX TODO sprawdzanie, żęby nie było dwóch autorów o tej samej kolejności

    def save(self, *args, **kw):
        if self.autor.jednostki.filter(pk=self.jednostka.pk).count() == 0:
            self.jednostka.dodaj_autora(self.autor)
        return super(BazaModeluOdpowiedzialnosciAutorow, self).save(*args, **kw)


class ModelZeSzczegolami(models.Model):
    """Model zawierający pola: informacje, szczegóły, uwagi, słowa kluczowe."""
    informacje = models.TextField(
        "Informacje", null=True, blank=True)

    szczegoly = models.CharField(
        "Szczegóły", max_length=512, null=True, blank=True,
        help_text="Np. str. 23-45")

    uwagi = models.TextField(null=True, blank=True, db_index=True)

    slowa_kluczowe = models.TextField("Słowa kluczowe", null=True, blank=True)

    utworzono = models.DateTimeField("Utworzono", auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True


class ModelZCharakterem(models.Model):
    charakter_formalny = models.ForeignKey(
        Charakter_Formalny, verbose_name='Charakter formalny')

    class Meta:
        abstract = True


class ModelPrzeszukiwalny(models.Model):
    """Model zawierający pole pełnotekstowego przeszukiwania
    'search_index'"""

    search_index = VectorField()
    tytul_oryginalny_sort = models.TextField(db_index=True, default='')

    class Meta:
        abstract = True


class Wydawnictwo_Baza(ModelZOpisemBibliograficznym, ModelPrzeszukiwalny):
    def __unicode__(self):
        return self.tytul_oryginalny

    class Meta:
        abstract = True


class ModelHistoryczny(models.Model):
    rozpoczecie_funkcjonowania = models.DateField(
        "Rozpoczęcie funkcjonowania", blank=True, null=True)
    zakonczenie_funkcjonowania = models.DateField(
        "Zakończenie funkcjonowania", blank=True, null=True
    )

    class Meta:
        abstract = True


from django.core.validators import URLValidator

url_validator = URLValidator()

import re

ss_regex = re.compile(r"ss\. (?P<ile_stron>[0-9]+)")
s_regex = re.compile(r"s\. (?P<od_strony>[0-9]+)-(?P<do_strony>[0-9]+)")
single_s_regex = re.compile(r"s\. (?P<ile_stron>[0-9]+)")


class PBNSerializerHelperMixin:
    def eksport_pbn_zakres_stron(self):
        res = ss_regex.search(self.szczegoly)
        if res is not None:
            ile = res.groups()[0]
            return "1-%s" % ile

        res = s_regex.search(self.szczegoly)
        if res is not None:
            ile = res.groups()
            return "%s-%s" % (ile[0], ile[1])

        res = single_s_regex.search(self.szczegoly)
        if res is not None:
            ile = res.groups()[0]
            return "%s-%s" % (ile, ile)

    def eksport_pbn_pages(self, toplevel, wydzial=None, autorzy_klass=None):
        zakres = self.eksport_pbn_zakres_stron()
        if zakres:
            pages = SubElement(toplevel, "pages")
            pages.text = zakres

    eksport_pbn_TYP_KBN_MAP = {
        'PO': 'original-article',
        'PW': 'original-article',
        'PP': 'review-article',
        'PNP': 'popular-science-article',
        '000': 'others-citable'
    }

    def eksport_pbn_is(self, toplevel, wydzial=None, autorzy_klass=None):
        if self.charakter_formalny.charakter_pbn != None:
            return self.charakter_formalny.charakter_pbn.identyfikator

        is_text = None
        tks = self.typ_kbn.skrot
        if self.eksport_pbn_TYP_KBN_MAP.get(tks):
            is_text = self.eksport_pbn_TYP_KBN_MAP.get(tks)

        if is_text:
            _is = SubElement(toplevel, 'is')
            _is.text = is_text

    def eksport_pbn_system_identifier(self, toplevel, wydzial=None, autorzy_klass=None):
        system_identifier = SubElement(toplevel, 'system-identifier')

        # W zależności od rodzaju klasy 'self', dodaj cyferkę i kilka zer. W ten sposób
        # symlujemy unikalne ID dla każdej oodzielnej tabeli. Generalnie w systemie bpp
        # Wydawnictwo_Zwarte oraz Wydawnictwo_Ciagle może mieć ten sam numer ID, ponieważ
        # są to różne tabele, śledzone oddzielnie. Aby jednakże w PBN te ID były unikalne,
        # dodajemy przedrostki.
        #
        # Maksymalny int 32-bity: 2147483647
        # sys.maxint na MacOS X:  9223372036854775807
        #
        # ... zatem, do Wydawnictwo_Ciagle dopisujemy jedynkę i tyle zer, żeby zmieściś się w 10 znakach
        # ... tak samo do Wydawnictwo_Zwarte, tylko, ze tam damy dwójkę
        #
        # kilka miliardów publikacji w każdej kategorii "should be enough for anyone"
        #

        # teraz omijamy cyrkularny import za pomocą tego hacka:
        s = str(self.__class__)
        global_id = 3

        if 'Wydawnictwo_Zwarte' in s:
            global_id = 1
        elif 'Wydawnictwo_Ciagle' in s:
            global_id = 2
        else:
            raise NotImplementedError

        system_identifier.text = "%i%.9i" % (global_id, self.pk)

    def eksport_pbn_title(self, toplevel, wydzial=None, autorzy_klass=None):
        title = SubElement(toplevel, 'title')
        title.text = self.tytul_oryginalny

    def eksport_pbn_author(self, toplevel, wydzial, autorzy_klass):
        for autor_wyd in autorzy_klass.objects.filter(rekord=self, typ_odpowiedzialnosci__skrot='aut.'):
            if autor_wyd.autor.afiliacja_na_rok(self.rok, wydzial, rozszerzona=True):
                toplevel.append(autor_wyd.autor.eksport_pbn_serializuj(affiliated=True, employed=True))

    def eksport_pbn_other_contributors(self, toplevel, wydzial, autorzy_klass):
        dopisani_autorzy = 0
        wszyscy_autorzy = self.autorzy.all().count()
        for autor_wyd in autorzy_klass.objects.filter(rekord=self, typ_odpowiedzialnosci__skrot='aut.'):
            if autor_wyd.autor.afiliacja_na_rok(self.rok, wydzial, rozszerzona=True):
                dopisani_autorzy += 1
        other_contributors = SubElement(toplevel, 'other-contributors')
        other_contributors.text = str(wszyscy_autorzy - dopisani_autorzy)

    def eksport_pbn_lang(self, toplevel, wydzial=None, autorzy_klass=None):
        lang = SubElement(toplevel, 'lang')
        lang.text = self.jezyk.get_skrot_dla_pbn()

    def eksport_pbn_keywords(self, toplevel, wydzial=None, autorzy_klass=None):
        if self.slowa_kluczowe:
            lang = self.jezyk.get_skrot_dla_pbn()
            keywords = SubElement(toplevel, 'keywords', lang=lang)
            for elem in self.slowa_kluczowe.split(","):
                k = SubElement(keywords, 'k')
                k.text = elem.strip()

    def eksport_pbn_public_uri(self, toplevel, wydzial=None, autorzy_klass=None):
        def exp_www(www):
            try:
                url_validator(www)
                public_uri = SubElement(toplevel, "public-uri", href=www)
            except (ValueError, ValidationError):
                pass

        if self.public_www:
            exp_www(self.public_www)

        elif self.www:
            exp_www(self.www)


    def eksport_pbn_open_access(self, toplevel, wydzial=None, autorzy_klass=None):

        open_access = None

        if self.openaccess_wersja_tekstu is not None:
            if open_access is None:
                open_access = SubElement(toplevel, 'open-access')

            text_version = SubElement(open_access, "open-access-text-version")
            text_version.text = self.openaccess_wersja_tekstu.skrot
            has_stuff = True

        if self.openaccess_licencja is not None:
            if open_access is None:
                open_access = SubElement(toplevel, 'open-access')

            license = SubElement(open_access, "open-access-license")
            license.text = self.openaccess_licencja.skrot

        if self.openaccess_czas_publikacji is not None:
            if open_access is None:
                open_access = SubElement(toplevel, 'open-access')

            release_time = SubElement(open_access, "open-access-release-time")
            release_time.text = self.openaccess_czas_publikacji.skrot

        if self.openaccess_ilosc_miesiecy:
            if open_access is None:
                open_access = SubElement(toplevel, 'open-access')

            months = SubElement(open_access, "open-access-months")
            months.text = str(self.openaccess_ilosc_miesiecy)

        if self.openaccess_tryb_dostepu is not None:
            if open_access is None:
                open_access = SubElement(toplevel, 'open-access')

            mode = SubElement(open_access, "open-access-mode")
            mode.text = self.openaccess_tryb_dostepu.skrot


    def eksport_pbn_publication_date(self, toplevel, wydzial=None, autorzy_klass=None):
        publication_date = SubElement(toplevel, 'publication-date')
        publication_date.text = str(self.rok)

    def eksport_pbn_doi(self, toplevel, wydzial=None, autorzy_klass=None):
        if self.doi:
            doi = SubElement(toplevel, 'doi')
            doi.text = self.doi

    def eksport_pbn_run_serialization_functions(self, names, toplevel, wydzial, autorzy_klass):
        for elem in names:
            func = "eksport_pbn_" + elem.replace("-", "_")
            f = getattr(self, func, None)
            if f and hasattr(f, "__call__"):
                f(toplevel, wydzial, autorzy_klass)

    def eksport_pbn_serializuj(self, toplevel, wydzial, autorzy_klass):
        self.eksport_pbn_run_serialization_functions(
            ['title', 'author', "other-contributors", "doi",
             "lang", "abstract", "keywords", "public-uri", "publication-date",
             "conference", "size", "is", "system-identifier"],
            toplevel, wydzial, autorzy_klass)


class ModelZOpenAccess(models.Model):
    openaccess_wersja_tekstu = models.ForeignKey(
        'Wersja_Tekstu_OpenAccess',
        verbose_name="OpenAccess: wersja tekstu",
        blank=True, null=True)

    openaccess_licencja = models.ForeignKey(
        "Licencja_OpenAccess",
        verbose_name="OpenAccess: licencja",
        blank=True,
        null=True)

    openaccess_czas_publikacji = models.ForeignKey(
        "Czas_Udostepnienia_OpenAccess",
        verbose_name="OpenAccess: czas udostępnienia",
        blank=True,
        null=True)

    openaccess_ilosc_miesiecy = models.PositiveIntegerField(
        "OpenAccess: ilość miesięcy",
        blank=True,
        null=True,
        help_text="Ilość miesięcy jakie upłynęły od momentu opublikowania do momentu udostępnienia"
    )

    class Meta:
        abstract = True


class ModelZDOI(models.Model):
    doi = DOIField("DOI", null=True, blank=True, db_index=True)
    class Meta:
        abstract = True


class ModelZAktualizacjaDlaPBN(models.Model):
    #
    # Obiekt subklasujący tę klasę musi subklasować również DirtyFieldsMixin
    #

    ostatnio_zmieniony_dla_pbn = models.DateTimeField(
        "Ostatnio zmieniony (dla PBN)",
        auto_now_add=True,
        help_text="""Ostatnia aktualizacja rekordu - zmiana dowolnego z pól za wyjątkiem bloków pól: „punktacja”,
        „punktacja komisji centralnej”, „adnotacje” oraz pole „status korekty”."""
    )

    def save(self, *args, **kw):
        if self.pk is not None:
            if self.is_dirty():
                flds = self.get_dirty_fields(verbose=True)
                flds_keys = flds.keys()
                from bpp.admin.helpers import MODEL_PUNKTOWANY, MODEL_PUNKTOWANY_KOMISJA_CENTRALNA

                for elem in MODEL_PUNKTOWANY + MODEL_PUNKTOWANY_KOMISJA_CENTRALNA + \
                        ('ostatnio_zmieniony', 'ostatnio_zmieniony_dla_pbn', 'opis_bibliograficzny_cache',
                         'search_index', 'tytul_oryginalny_sort'):
                    if elem in flds_keys:
                        flds_keys.remove(elem)

                if flds_keys:
                    self.ostatnio_zmieniony_dla_pbn = timezone.now()

        super(ModelZAktualizacjaDlaPBN, self).save(*args, **kw)

    class Meta:
        abstract = True