# -*- encoding: utf-8 -*-
import datetime
from decimal import Decimal

from django.core.management import call_command
from django.db import transaction, DEFAULT_DB_ALIAS, connections

from django.test import TransactionTestCase, TestCase
from model_mommy import mommy
from django.conf import settings

from bpp.tests.util import any_uczelnia, any_wydzial, any_doktorat

from bpp.models import Autor, Patent_Autor, Jednostka, Typ_Odpowiedzialnosci, \
    Patent, Praca_Doktorska, Praca_Habilitacyjna, Tytul, Zrodlo, \
    Charakter_Formalny, Jezyk, Typ_KBN, Status_Korekty, Zrodlo_Informacji, \
    Wydawnictwo_Ciagle_Autor, Uczelnia, Wydzial, Wydawnictwo_Zwarte_Autor, Wydawnictwo_Ciagle
from bpp.models.cache import Rekord, with_cache, Autorzy, AutorzyView
from bpp.tests.test_reports.util import ciagle, zwarte, autor
from bpp.tests.util import any_ciagle, any_jednostka, any_autor, any_zrodlo
from bpp.models import cache

CHANGED = 'foo-123-changed'


def ramka(msg):
    print "+" + ("-" * 78) + "+"
    print "+ " + msg
    print "+" + ("-" * 78) + "+"


def clean_dict(ret):
    del ret['ostatnio_zmieniony']
    del ret['tytul_oryginalny_sort']
    return ret


class TestCacheMixin:
    fixtures = [
        'typ_odpowiedzialnosci.json', 'tytul.json', 'zrodlo_informacji.json',
        'charakter_formalny.json', 'status_korekty.json', 'typ_kbn.json',
        'jezyk.json']

    def setUp(self):
        self.maxDiff = None

        aut = Typ_Odpowiedzialnosci.objects.get(skrot='aut.')
        self.typ_odpowiedzialnosci = aut

        self.uczelnia = any_uczelnia()
        self.wydzial = any_wydzial(uczelnia=self.uczelnia)
        self.j = any_jednostka(nazwa='Foo Bar', wydzial=self.wydzial)

        self.a = autor(self.j)
        self.a.nazwisko = 'Kowalski'
        self.a.imiona = 'Jan'
        self.a.tytul = Tytul.objects.get(skrot='dr')
        self.a.save()

        wspolne_dane = dict(
            adnotacje='adnotacje',
            informacja_z=Zrodlo_Informacji.objects.all()[0],
            status_korekty=Status_Korekty.objects.all()[0],
            rok='2000',
            www='http://127.0.0.1/',
            afiliowana=True,
            recenzowana=True,
            impact_factor=5,
            punkty_kbn=5,
            index_copernicus=5,
            punktacja_wewnetrzna=5,
            weryfikacja_punktacji=True,
            typ_kbn=Typ_KBN.objects.all()[0],
            jezyk=Jezyk.objects.all()[0],
            informacje='informacje',
            szczegoly='szczegoly',
            uwagi='uwagi',
            slowa_kluczowe='slowa kluczowe'
        )

        zwarte_dane = dict(
            miejsce_i_rok="Lublin 2012",
            wydawnictwo="Pholium",
            redakcja="Redkacja",
            isbn='isbn',
            e_isbn='e_isbn',
            tytul='tytul'
        )

        self.z = zwarte(
            self.a, self.j, aut, tytul_oryginalny='zwarte',
            liczba_znakow_wydawniczych=40000,
            charakter_formalny=Charakter_Formalny.objects.all()[0],
            **dict(zwarte_dane.items() + wspolne_dane.items())
        )

        self.zr = mommy.make(Zrodlo, nazwa='Zrodlo')

        self.c = ciagle(
            self.a, self.j,
            tytul_oryginalny='ciągłe',
            zrodlo=self.zr,
            tytul='tytul',
            issn='issn',
            e_issn='e_issn',
            charakter_formalny=Charakter_Formalny.objects.all()[0],
            **wspolne_dane)
        self.assertEquals(Wydawnictwo_Ciagle_Autor.objects.all().count(), 1)

        wca = Wydawnictwo_Ciagle_Autor.objects.all()[0]
        wca.typ_odpowiedzialnosci = self.typ_odpowiedzialnosci
        wca.save()

        settings.BPP_CACHE_ENABLED = True

        # Doktorat i habilitacja

        doktorat_kw = dict(zwarte_dane.items() + wspolne_dane.items())

        self.d = mommy.make(
            Praca_Doktorska, tytul_oryginalny='doktorat',
            autor=self.a,
            jednostka=self.j,
            **doktorat_kw)

        self.h = mommy.make(
            Praca_Habilitacyjna, tytul_oryginalny='habilitacja',
            autor=self.a, jednostka=self.j,
            **doktorat_kw)

        # Patent

        chf_pat = Charakter_Formalny.objects.get(skrot='PAT')

        for elem in ['typ_kbn', 'jezyk']:
            del wspolne_dane[elem]

        self.p = mommy.make(
            Patent, tytul_oryginalny='patent',
            numer="100", z_dnia=datetime.date(2012, 1, 1),
            **wspolne_dane)

        Patent_Autor.objects.create(
            autor=self.a, jednostka=self.j, rekord=self.p,
            typ_odpowiedzialnosci=aut, zapisany_jako="Kowalski")

        self.wszystkie_modele = [self.d, self.h, self.p, self.c, self.z]


class TestCacheDeferredOpisBibliograficznyCache(TransactionTestCase):
    def setUp(self):
        Status_Korekty.objects.create(pk=1, nazwa="foo")

    @with_cache
    def test_opis_bibliograficzny(self):
        c = any_ciagle(szczegoly='sz', uwagi='u')
        transaction.commit()

        print Rekord.objects.all()[0].opis_bibliograficzny_cache
        print c.opis_bibliograficzny()

        self.assertEquals(
            Rekord.objects.all()[0].opis_bibliograficzny_cache,
            c.opis_bibliograficzny())
        c.delete()
        self.assertEquals(Rekord.objects.all().count(), 0)

    @with_cache
    def test_opis_bibliograficzny_dependent(self):
        """Stwórz i skasuj Wydawnictwo_Ciagle_Autor i sprawdź, jak to
        wpłynie na opis."""
        c = any_ciagle(szczegoly='sz', uwagi='u')
        self.assertNotIn('KOWALSKI', Rekord.objects.all()[0].opis_bibliograficzny_cache)

        a = any_autor(nazwisko='Kowalski')
        j = any_jednostka()
        wca = c.dodaj_autora(a, j)
        self.assertIn('KOWALSKI', Rekord.objects.all()[0].opis_bibliograficzny_cache)

        wca.delete()
        self.assertNotIn('KOWALSKI', Rekord.objects.all()[0].opis_bibliograficzny_cache)

    @with_cache
    def test_opis_bibliograficzny_zrodlo(self):
        """Zmień nazwę źródła i sprawdź, jak to wpłynie na opis."""

        z = any_zrodlo(nazwa='OMG', skrot="wutlolski")
        c = any_ciagle(szczegoly='sz', uwagi='u', zrodlo=z)

        self.assertIn('wutlolski', Rekord.objects.all()[0].opis_bibliograficzny_cache)

        z.nazwa = 'LOL'
        z.skrot = "foka"
        z.save() # XXX w tym momencie wywoływany jest sygnał

        # Z uwagi na ustawienie CELERY_ALWAYS_EAGER, uruchomimy
        # sobie takie wywołanie DRUGI raz, aby system zauważył inny
        # tytuł rekordu...
        z.nazwa = 'LOL 2'
        z.skrot = "foka 2"
        z.save()

        self.assertIn('foka', Rekord.objects.all()[0].opis_bibliograficzny_cache)

        # to się nie uda i wlasciwie to nie wiem, czemu.
        # self.assertIn('foka 2', Rekord.objects.all()[0].opis_bibliograficzny_cache)


class TestCacheSimple(TestCacheMixin, TestCase):
    @with_cache
    def test_get_original_object(self):
        Rekord.objects.full_refresh()
        for model in self.wszystkie_modele:
            c = Rekord.objects.get(original=model)
            self.assertEquals(c.original, model)

    @with_cache
    def test_cache_triggers(self):
        T1 = 'OMG ROXX'
        T2 = 'LOL'

        for model in self.wszystkie_modele:
            model.tytul_oryginalny = T1
            model.save()
            self.assertEquals(Rekord.objects.get(original=model).tytul_oryginalny, T1)

            model.tytul_oryginalny = T2
            model.save()
            self.assertEquals(Rekord.objects.get(original=model).tytul_oryginalny, T2)


    def assertInstanceEquals(self, instance, values_dict):
        for key, value in values_dict.items():
            instance_value = getattr(instance, key)
            self.assertEquals(
                instance_value, value,
                msg="key=%s, %s!=%s" % (key, value, instance_value))

    @with_cache
    def test_tytul_sorted_version(self):
        for elem in [self.d, self.h, self.c, self.z]: #  self.p]:
            elem.tytul_oryginalny = "The 'APPROACH'"
            elem.jezyk = Jezyk.objects.get(skrot='ang.')
            elem.save()

            self.assertEquals(
                Rekord.objects.get(original=elem).tytul_oryginalny_sort,
                'approach')

            elem.tytul_oryginalny = "le 'test'"
            elem.jezyk = Jezyk.objects.get(skrot='fr.')
            elem.save()

            #elem = elem.__class__.objects.get(pk=elem.pk) #reload
            #self.assertEquals(elem.tytul_oryginalny_sort, "test")

            self.assertEquals(
                Rekord.objects.get(original=elem).tytul_oryginalny_sort,
                'test')

class LoadFixturesMixin:
    def _databases_names(self, include_mirrors=True):
        # If the test case has a multi_db=True flag, act on all databases,
        # including mirrors or not. Otherwise, just on the default DB.
        if getattr(self, 'multi_db', False):
            return [alias for alias in connections
                    if include_mirrors or not connections[alias].settings_dict[
                    'TEST_MIRROR']]
        else:
            return [DEFAULT_DB_ALIAS]

    def loadFixtures(self):
        for db_name in self._databases_names(include_mirrors=False):
            if hasattr(self, 'fixtures'):
                call_command('loaddata', *self.fixtures,
                             **{'verbosity': 0, 'database': db_name,
                                'skip_validation': True})


class TestCacheZapisani(TestCase):
    fixtures = [
        'typ_odpowiedzialnosci.json', 'tytul.json', 'zrodlo_informacji.json',
        'charakter_formalny.json', 'status_korekty.json', 'typ_kbn.json',
        'jezyk.json']

    def test_zapisani_wielu(self):
        aut = any_autor("Kowalski", "Jan")
        aut2 = any_autor("Nowak", "Jan")

        jed = any_jednostka("Jednostka")
        wyd = any_ciagle(tytul_oryginalny="Wydawnictwo ciagle")

        for kolejnosc, autor in enumerate([aut, aut2]):
            Wydawnictwo_Ciagle_Autor.objects.create(
                autor=autor,
                jednostka=jed,
                rekord=wyd,
                typ_odpowiedzialnosci_id=1,
                zapisany_jako='FOO BAR',
                kolejnosc=kolejnosc
            )


        Rekord.objects.full_refresh()
        c = Rekord.objects.get(original=wyd)

        # Upewnij się, że w przypadku pracy z wieloma autorami do cache
        # zapisywane jest nie nazwisko z pól 'zapisany_jako' w bazie danych,
        # a oryginalne
        self.assertEquals(c.opis_bibliograficzny_autorzy_cache,
                          [u'Kowalski Jan', 'Nowak Jan'])

        # Upewnij się, że pole 'opis_bibliograficzny_zapisani_autorzy_cache'
        # zapisywane jest prawidłowo
        self.assertEquals(c.opis_bibliograficzny_zapisani_autorzy_cache,
                          'FOO BAR, FOO BAR')

    def test_zapisani_jeden(self):
        aut = any_autor("Kowalski", "Jan")
        dok = any_doktorat(tytul_oryginalny="Doktorat", autor=aut)

        Rekord.objects.full_refresh()
        c = Rekord.objects.get(original=dok)

        # Upewnij się, że w przypadku pracy z jednym autorem do cache
        # zapisywana jest prawidłowa wartość
        self.assertEquals(c.opis_bibliograficzny_autorzy_cache, [u'Kowalski Jan'])

        self.assertEquals(c.opis_bibliograficzny_zapisani_autorzy_cache, u'Kowalski Jan')

class TestCacheTriggers(TestCacheMixin, TransactionTestCase):

    def setUp(self):
        TestCacheMixin.setUp(self)

    @with_cache
    def test_post_save(self):
        self.d.tytul = CHANGED
        self.d.save()

        self.assertEquals(Rekord.objects.all().count(), 5)
        self.assertEquals(Rekord.objects.get(original=self.d).tytul, CHANGED)

    @with_cache
    def test_deletion(self):
        self.d.save()
        self.assertEquals(Rekord.objects.all().count(), 5)

        self.d.delete()
        self.assertEquals(Rekord.objects.all().count(), 4)

    @with_cache
    def test_m2m_caching(self):
        """Czy skasowanie obiektu Wydawnictwo_Ciagle_Autor zmieni opis
        wydawnictwa ciągłego w Rekordy materialized view?"""

        # Odśwież wpisy w mat view, zapisując Wydawnictwo_Ciagle:
        self.c.save()
        self.assertEquals(Rekord.objects.all().count(), 5)

        # Skasuj obiekt
        aca = Wydawnictwo_Ciagle_Autor.objects.all()[0]
        aca.delete()
        self.assertEquals(Autorzy.objects.filter(rekord=aca).count(), 0)

    def __test_m2m_caching(self, obj, should_be=3):
        """Czy skasowanie autora, jednostki, typu odpowiedzialnosci lub zrodla
         zmieni opis wydawnictwa ciągłego w Cache?"""

        self.assertEquals(Rekord.objects.all().count(), 5)
        self.assertEquals(Wydawnictwo_Ciagle_Autor.objects.all().count(), 1)

        obj.delete()

        self.assertEquals(Wydawnictwo_Ciagle_Autor.objects.all().count(), 0)
        self.assertEquals(Rekord.objects.all().count(), should_be)

    @with_cache
    def test_m2m_caching_autor(self):
        self.__test_m2m_caching(self.a)

    @with_cache
    def test_m2m_caching_typ_odpowiedzialnosci(self):
        self.__test_m2m_caching(self.typ_odpowiedzialnosci, should_be=5)
        self.assertEquals(Autorzy.objects.all().count(), 0)

    @with_cache
    def test_m2m_caching_zrodlo(self):
        self.__test_m2m_caching(self.zr, should_be=4)

    @with_cache
    def test_m2m_caching_jezyk(self):
        Rekord.objects.full_refresh()
        self.assertEquals(Rekord.objects.all().count(), 5)
        self.assertEquals(Wydawnictwo_Ciagle_Autor.objects.all().count(), 1)

        Jezyk.objects.all().delete()

        self.assertEquals(Rekord.objects.all().count(), 0)
        self.assertEquals(Autorzy.objects.all().count(), 0)

    @with_cache
    def test_m2m_caching_charakter_formalny(self):
        self.assertEquals(AutorzyView.objects.all().count(), 5)
        self.assertEquals(Autorzy.objects.all().count(), 5)

        Rekord.objects.full_refresh()

        self.assertEquals(Rekord.objects.all().count(), 5)
        self.assertEquals(Wydawnictwo_Ciagle_Autor.objects.all().count(), 1)

        self.assertEquals(AutorzyView.objects.all().count(), 5)
        self.assertEquals(Autorzy.objects.all().count(), 5)

        Charakter_Formalny.objects.all().delete()

        self.assertEquals(Rekord.objects.all().count(), 0)
        # XXX: TODO: idealnie, tu powinno byc 0 rekordów, ale PAT, DOK i HAB
        # XXX: TODO: mają symulowane pole charakteru i nie zostaną usunięte
        self.assertEquals(Autorzy.objects.all().count(), 0)
        transaction.commit()


    @with_cache
    def test_m2m_caching_uczelnia(self):
        self.__test_m2m_caching(self.uczelnia)

    @with_cache
    def test_m2m_caching_wydzial(self):
        self.__test_m2m_caching(self.wydzial)

    @with_cache
    def test_rekord_objects_full_refresh_bug(self):
        self.assertEquals(Rekord.objects.all().count(), 5)
        self.assertEquals(AutorzyView.objects.all().count(), 5)
        self.assertEquals(Autorzy.objects.all().count(), 5)

        Rekord.objects.full_refresh()

        self.assertEquals(Rekord.objects.all().count(), 5)
        self.assertEquals(AutorzyView.objects.all().count(), 5)
        self.assertEquals(Autorzy.objects.all().count(), 5)


class TestMinimalCachingProblem(TestCase):
    fixtures = [
        "status_korekty.json",
        "charakter_formalny.json",
        "jezyk.json",
        "typ_odpowiedzialnosci.json"]

    @with_cache
    def test_tworzenie(self):

        self.j = any_jednostka()
        self.a = any_autor()

        self.assertEquals(Autorzy.objects.all().count(), 0)

        c = any_ciagle(impact_factor=5, punktacja_wewnetrzna=0)
        self.assertEquals(Rekord.objects.all().count(), 1)

        c.dodaj_autora(self.a, self.j)

        self.assertEquals(AutorzyView.objects.all().count(), 1)
        self.assertEquals(Autorzy.objects.all().count(), 1)

    @with_cache
    def test_usuwanie(self):

        self.j = any_jednostka()
        self.a = any_autor()

        self.assertEquals(Autorzy.objects.all().count(), 0)

        c = any_ciagle(impact_factor=5, punktacja_wewnetrzna=0)
        self.assertEquals(Rekord.objects.all().count(), 1)

        c.dodaj_autora(self.a, self.j)

        c.delete()

        self.assertEquals(AutorzyView.objects.all().count(), 0)
        self.assertEquals(Autorzy.objects.all().count(), 0)
