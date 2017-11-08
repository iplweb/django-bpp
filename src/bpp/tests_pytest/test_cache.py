# -*- encoding: utf-8 -*-
# TODO: przenies do bpp/tests/test_cache.py
import pytest
from model_mommy import mommy

from bpp.models.autor import Autor
from bpp.models.cache import Rekord, Autorzy, defer_zaktualizuj_opis
from bpp.models.openaccess import Wersja_Tekstu_OpenAccess, \
    Licencja_OpenAccess, Czas_Udostepnienia_OpenAccess
from bpp.models.struktura import Jednostka
from bpp.models.system import Typ_Odpowiedzialnosci, Jezyk, Charakter_Formalny, \
    Typ_KBN
from bpp.models.wydawnictwo_ciagle import Wydawnictwo_Ciagle, \
    Wydawnictwo_Ciagle_Autor
from bpp.models.zrodlo import Zrodlo
from bpp.tasks import zaktualizuj_opis


def pierwszy_rekord():
    return Rekord.objects.all()[0].opis_bibliograficzny_cache


def test_opis_bibliograficzny(db, standard_data):
    wc = mommy.make(Wydawnictwo_Ciagle, szczegoly='Sz', uwagi='U')

    rekord_opis = Rekord.objects.all()[0].opis_bibliograficzny_cache
    wc_opis = wc.opis_bibliograficzny()
    assert rekord_opis == wc_opis


def test_kasowanie(db, standard_data):
    assert Rekord.objects.count() == 0

    wc = mommy.make(Wydawnictwo_Ciagle)
    assert Rekord.objects.count() == 1

    wc.delete()
    assert Rekord.objects.count() == 0


def test_opis_bibliograficzny_dependent(db, standard_data):
    """Stwórz i skasuj Wydawnictwo_Ciagle_Autor i sprawdź, jak to
    wpłynie na opis."""

    c = mommy.make(Wydawnictwo_Ciagle, szczegoly='sz', uwagi='u')
    assert 'KOWALSKI' not in c.opis_bibliograficzny()
    assert 'KOWALSKI' not in pierwszy_rekord()

    a = mommy.make(Autor, imiona='Jan', nazwisko='Kowalski')
    j = mommy.make(Jednostka)
    wca = c.dodaj_autora(a, j)
    assert 'KOWALSKI' in c.opis_bibliograficzny()
    assert 'KOWALSKI' in pierwszy_rekord()

    wca.delete()
    assert 'KOWALSKI' not in c.opis_bibliograficzny()
    assert 'KOWALSKI' not in pierwszy_rekord()


def test_opis_bibliograficzny_zrodlo(db, standard_data):
    """Zmień nazwę źródła i sprawdź, jak to wpłynie na opis."""
    from bpp.models import cache
    assert cache._CACHE_ENABLED

    from django.conf import settings
    assert settings.TESTING == True
    assert settings.CELERY_ALWAYS_EAGER == True

    z = mommy.make(Zrodlo, nazwa='OMG', skrot='wutlolski')
    c = mommy.make(Wydawnictwo_Ciagle, szczegoly='SZ', uwagi='U', zrodlo=z)

    assert 'wutlolski' in c.opis_bibliograficzny()
    assert 'wutlolski' in pierwszy_rekord()

    z.nazwa = 'LOL'
    z.skrot = 'FOKA'

    assert 'wutlolski' not in c.opis_bibliograficzny()
    assert 'FOKA' in c.opis_bibliograficzny()

    assert 'wutlolski' in pierwszy_rekord()


    assert cache._CACHE_ENABLED

    z.save()

    assert 'FOKA' in c.opis_bibliograficzny()
    assert 'FOKA' in pierwszy_rekord()

    z.nazwa = 'LOL 2'
    z.skrot = "foka 2"
    z.save()

    assert 'foka 2' in c.opis_bibliograficzny()
    assert 'foka 2' in pierwszy_rekord()

@pytest.mark.django_db
def test_post_save_cache(doktorat):
    assert Rekord.objects.all().count() == 1

    doktorat.tytul = 'zmieniono'
    doktorat.save()

    assert Rekord.objects.get_original(doktorat).tytul == 'zmieniono'


def test_deletion_cache(doktorat):
    assert Rekord.objects.all().count() == 1

    doktorat.delete()
    assert Rekord.objects.all().count() == 0

@pytest.mark.django_db
def test_wca_delete_cache(wydawnictwo_ciagle_z_dwoma_autorami):
    """Czy skasowanie obiektu Wydawnictwo_Ciagle_Autor zmieni opis
    wydawnictwa ciągłego w Rekordy materialized view?"""

    assert Rekord.objects.all().count() == 1
    assert Wydawnictwo_Ciagle_Autor.objects.all().count() == 2

    r = Rekord.objects.all()[0]
    assert 'NOWAK' in r.opis_bibliograficzny_cache
    assert 'KOWALSKI' in r.opis_bibliograficzny_cache

    Wydawnictwo_Ciagle_Autor.objects.all()[0].delete()
    aca = Wydawnictwo_Ciagle_Autor.objects.all()[0]
    aca.delete()

    assert Autorzy.objects.filter_rekord(aca).count() == 0
    assert Rekord.objects.all().count() == 1

    r = Rekord.objects.all()[0]
    assert 'NOWAK' not in r.opis_bibliograficzny_cache
    assert 'KOWALSKI' not in r.opis_bibliograficzny_cache

@pytest.mark.django_db
def test_caching_kasowanie_autorow(wydawnictwo_ciagle_z_dwoma_autorami):
    for wca in Wydawnictwo_Ciagle_Autor.objects.all().only('autor'):
        wca.autor.delete()

    assert Wydawnictwo_Ciagle_Autor.objects.count() == 0
    assert Rekord.objects.all().count() == 1

    r = Rekord.objects.all()[0]
    assert 'NOWAK' not in r.opis_bibliograficzny_cache
    assert 'KOWALSKI' not in r.opis_bibliograficzny_cache

@pytest.mark.django_db
def test_caching_kasowanie_typu_odpowiedzialnosci_autorow(wydawnictwo_ciagle_z_dwoma_autorami):
    assert Wydawnictwo_Ciagle_Autor.objects.filter(rekord=wydawnictwo_ciagle_z_dwoma_autorami).count() == 2

    Typ_Odpowiedzialnosci.objects.all().delete()

    assert Wydawnictwo_Ciagle_Autor.objects.count() == 0
    assert Rekord.objects.all().count() == 1

    r = Rekord.objects.all()[0]
    assert 'NOWAK' not in r.opis_bibliograficzny_cache
    assert 'KOWALSKI' not in r.opis_bibliograficzny_cache


@pytest.mark.django_db
def test_caching_kasowanie_zrodla(wydawnictwo_ciagle_z_dwoma_autorami):
    assert Zrodlo.objects.all().count() == 1

    z = Zrodlo.objects.all()[0]
    z.delete()  # WCA ma zrodlo.on_delete=SET_NULL

    assert Rekord.objects.all().count() == 1
    assert Wydawnictwo_Ciagle.objects.all().count() == 1

    r = Rekord.objects.all()[0]
    assert 'NOWAK' in r.opis_bibliograficzny_cache
    assert 'KOWALSKI' in r.opis_bibliograficzny_cache
    assert z.skrot not in r.opis_bibliograficzny_cache
    assert "None" not in r.opis_bibliograficzny_cache


@pytest.mark.django_db
def test_caching_kasowanie_jezyka(wydawnictwo_ciagle_z_dwoma_autorami):
    xng = Jezyk.objects.create(skrot="xng.", nazwa="taki", pk=500)
    wydawnictwo_ciagle_z_dwoma_autorami.jezyk = xng
    wydawnictwo_ciagle_z_dwoma_autorami.save()

    assert Rekord.objects.all().count() == 1
    xng.delete()

    assert Rekord.objects.all().count() == 0

@pytest.mark.django_db
@pytest.mark.parametrize(
    "attrname, klass, skrot, ma_zostac",
    [("typ_kbn", Typ_KBN, "PO", 0),
     ("charakter_formalny", Charakter_Formalny, "PAT", 0),
     ("openaccess_wersja_tekstu", Wersja_Tekstu_OpenAccess, "FINAL_AUTHOR", 1),
     ("openaccess_licencja", Licencja_OpenAccess, "CC-BY-ND", 1),
     ("openaccess_czas_publikacji", Czas_Udostepnienia_OpenAccess,
      "AT_PUBLICATION", 1)])
def test_usuwanie_powiazanych_vs_rekord(
        wydawnictwo_ciagle_z_dwoma_autorami,
        patent,
        standard_data,
        openaccess_data,
        attrname,
        klass,
        skrot,
        ma_zostac):

    o = klass.objects.get(skrot=skrot)
    setattr(wydawnictwo_ciagle_z_dwoma_autorami, attrname, o)
    wydawnictwo_ciagle_z_dwoma_autorami.save()

    setattr(patent, attrname, o)
    patent.save()

    assert Rekord.objects.all().count() == 2
    o.delete()
    assert Rekord.objects.all().count() == ma_zostac


@pytest.mark.django_db
def test_caching_kasowanie_typu_kbn(
        wydawnictwo_ciagle_z_dwoma_autorami,
        standard_data):
    tk = Typ_KBN.objects.all().first()

    wydawnictwo_ciagle_z_dwoma_autorami.typ_kbn = tk
    wydawnictwo_ciagle_z_dwoma_autorami.save()

    assert Rekord.objects.all().count() == 1
    tk.delete()

    assert Rekord.objects.all().count() == 0


@pytest.mark.django_db
def test_caching_kasowanie_charakteru_formalnego(
        wydawnictwo_ciagle_z_dwoma_autorami, patent, autor_jan_kowalski,
        jednostka, standard_data):
    patent.dodaj_autora(autor_jan_kowalski, jednostka)

    cf = Charakter_Formalny.objects.all().first()

    wydawnictwo_ciagle_z_dwoma_autorami.charakter_formalny = cf
    wydawnictwo_ciagle_z_dwoma_autorami.save()

    assert Rekord.objects.all().count() == 2
    Charakter_Formalny.objects.all().delete()

    assert Rekord.objects.all().count() == 0

@pytest.mark.django_db
def test_caching_kasowanie_wydzialu(autor_jan_kowalski, jednostka, wydzial,
                                    wydawnictwo_ciagle,
                                    typy_odpowiedzialnosci):
    assert jednostka.wydzial == wydzial

    wydawnictwo_ciagle.dodaj_autora(autor_jan_kowalski, jednostka)

    assert Rekord.objects.all().count() == 1
    assert Jednostka.objects.all().count() == 1
    wydzial.delete()

    assert Rekord.objects.all().count() == 1
    assert Rekord.objects.all()[0].original.autorzy.all().count() == 0
    assert Jednostka.objects.all().count() == 0

@pytest.mark.django_db
def test_caching_kasowanie_uczelni(autor_jan_kowalski, jednostka, wydzial,
                                   uczelnia, wydawnictwo_ciagle,
                                   typy_odpowiedzialnosci):
    assert wydzial.uczelnia == uczelnia
    assert jednostka.wydzial == wydzial
    wydawnictwo_ciagle.dodaj_autora(autor_jan_kowalski, jednostka)

    assert Rekord.objects.all().count() == 1
    assert Jednostka.objects.all().count() == 1
    uczelnia.delete()

    assert Rekord.objects.all().count() == 1
    assert Rekord.objects.all()[0].original.autorzy.all().count() == 0
    assert Jednostka.objects.all().count() == 0


@pytest.mark.django_db
def test_caching_full_refresh(wydawnictwo_ciagle_z_dwoma_autorami):
    assert Rekord.objects.all().count() == 1
    Rekord.objects.full_refresh()
    assert Rekord.objects.all().count() == 1

@pytest.mark.django_db
def test_caching_kolejnosc(wydawnictwo_ciagle_z_dwoma_autorami):

    a = list(Wydawnictwo_Ciagle_Autor.objects.all().order_by('kolejnosc'))
    assert len(a) == 2

    x = Rekord.objects.get_original(wydawnictwo_ciagle_z_dwoma_autorami)
    assert "[AUT.] KOWALSKI JAN, NOWAK JAN" in x.opis_bibliograficzny_cache

    k = a[0].kolejnosc
    a[0].kolejnosc = a[1].kolejnosc
    a[1].kolejnosc = k
    a[0].save()
    a[1].save()

    x = Rekord.objects.get_original(wydawnictwo_ciagle_z_dwoma_autorami)
    assert "[AUT.] NOWAK JAN, KOWALSKI JAN" in x.opis_bibliograficzny_cache


@pytest.mark.django_db
def test_defer_zaktualizuj_opis(settings):
    settings.CELERY_ALWAYS_EAGER = False
    w = mommy.make(Wydawnictwo_Ciagle)
    w.tytul_oryginalny = "foobar"
    defer_zaktualizuj_opis(w)
    settings.CELERY_ALWAYS_EAGER = True

@pytest.mark.django_db
def test_defer_zaktualizuj_opis_task(settings):
    w = mommy.make(Wydawnictwo_Ciagle)
    w.tytul_oryginalny = "foobar"
    w.save()

    zaktualizuj_opis('bpp', 'wydawnictwo_ciagle', w.pk, called_by="tests")


@pytest.mark.django_db
def test_aktualizacja_rekordu_autora(typy_odpowiedzialnosci):
    w = mommy.make(Wydawnictwo_Ciagle)

    a = mommy.make(Autor)
    b = mommy.make(Autor)

    j = mommy.make(Jednostka)
    r = w.dodaj_autora(a, j, zapisany_jako="Test")

    assert b.pk not in Rekord.objects.all().first().autorzy.all().values_list(
        "autor", flat=True)

    r.autor = b
    r.save()

    # czy cache jest odświeżone
    assert b.pk in Rekord.objects.all().first().autorzy.all().values_list(
        "autor", flat=True)
