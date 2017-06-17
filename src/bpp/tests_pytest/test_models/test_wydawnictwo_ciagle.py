# -*- encoding: utf-8 -*-

import time

import pytest
from lxml import etree

from bpp.admin.helpers import MODEL_PUNKTOWANY_KOMISJA_CENTRALNA, MODEL_PUNKTOWANY
from bpp.models.openaccess import Licencja_OpenAccess
from bpp.models.system import Status_Korekty


@pytest.mark.django_db
def test_models_wydawnictwo_ciagle_dirty_fields_ostatnio_zmieniony_dla_pbn(wydawnictwo_ciagle, wydawnictwo_zwarte,
                                                                           autor_jan_nowak, jednostka, statusy_korekt):
    Licencja_OpenAccess.objects.create(nazwa="lic 1 ", skrot="l1")
    Licencja_OpenAccess.objects.create(nazwa="lic 2 ", skrot="l2")

    # Licencje muszą być w bazie, jakiekolwiek
    assert Licencja_OpenAccess.objects.all().first() != Licencja_OpenAccess.objects.all().last()

    for wyd in wydawnictwo_ciagle, wydawnictwo_zwarte:
        wyd.openaccess_licencja = Licencja_OpenAccess.objects.all().first()
        wyd.save()

        ost_zm_pbn = wyd.ostatnio_zmieniony_dla_pbn

        time.sleep(0.5)

        wyd.status = Status_Korekty.objects.get(nazwa="w trakcie korekty")
        wyd.save()
        assert ost_zm_pbn == wyd.ostatnio_zmieniony_dla_pbn

        time.sleep(0.5)

        wyd.status = Status_Korekty.objects.get(nazwa="po korekcie")
        wyd.save()
        assert ost_zm_pbn == wyd.ostatnio_zmieniony_dla_pbn

        time.sleep(0.5)

        for fld in MODEL_PUNKTOWANY_KOMISJA_CENTRALNA + MODEL_PUNKTOWANY + ('adnotacje',):
            if fld == 'weryfikacja_punktacji':
                continue
            setattr(wyd, fld, 123)
            wyd.save()
            assert ost_zm_pbn == wyd.ostatnio_zmieniony_dla_pbn
            time.sleep(0.5)

        wyd.tytul_oryginalny = "1234 test zmian"
        wyd.save()

        try:
            assert ost_zm_pbn != wyd.ostatnio_zmieniony_dla_pbn
        except TypeError:
            pass  # TypeError: can't compare offset-naive and offset-aware datetimes

        time.sleep(0.5)

        ost_zm_pbn = wyd.ostatnio_zmieniony_dla_pbn

        aj = wyd.dodaj_autora(autor_jan_nowak, jednostka)
        wyd.refresh_from_db()
        assert ost_zm_pbn != wyd.ostatnio_zmieniony_dla_pbn

        ost_zm_pbn = wyd.ostatnio_zmieniony_dla_pbn

        aj.delete()
        wyd.refresh_from_db()
        assert ost_zm_pbn != wyd.ostatnio_zmieniony_dla_pbn

        # Test na foreign keys
        ost_zm_pbn = wyd.ostatnio_zmieniony_dla_pbn

        assert wyd.openaccess_licencja.pk != Licencja_OpenAccess.objects.all().last().pk
        wyd.openaccess_licencja = Licencja_OpenAccess.objects.all().last()
        wyd.save()

        wyd.refresh_from_db()
        assert ost_zm_pbn != wyd.ostatnio_zmieniony_dla_pbn


def test_export_pubmed_id(wydawnictwo_ciagle):
    wc = wydawnictwo_ciagle

    wc.pubmed_id = None
    wc.public_www = "http://www.onet.pl/"
    wc.www = None

    toplevel = etree.fromstring("<body></body>")
    wc.eksport_pbn_public_uri(toplevel)
    assert toplevel[0].attrib['href'] == "http://www.onet.pl/"

    wc.public_www = None
    wc.pubmed_id = "123"
    toplevel = etree.fromstring("<body></body>")
    wc.eksport_pbn_public_uri(toplevel)
    assert toplevel[0].attrib['href'] == "http://www.ncbi.nlm.nih.gov/pubmed/123"

    wc.public_www = None
    wc.pubmed_id = None
    wc.www = "http://www.onet.pl/"
    toplevel = etree.fromstring("<body></body>")
    wc.eksport_pbn_public_uri(toplevel)
    import pytest
    with pytest.raises(IndexError):
        toplevel[0]


@pytest.mark.parametrize("informacje,expected",
                         [("bez sensu", None),
                          ("2016 vol. 5 nr 10", "5"),
                          ("2019 Bd 4 nr. 3 test", "4")])
def test_eksport_pbn_get_volume(informacje, expected, wydawnictwo_ciagle):
    wydawnictwo_ciagle.informacje = informacje
    assert wydawnictwo_ciagle.eksport_pbn_get_volume() == expected


def test_eksport_pbn_volume(wydawnictwo_ciagle):
    toplevel = etree.fromstring("<body></body>")
    wydawnictwo_ciagle.informacje = "bez sensu"
    wydawnictwo_ciagle.eksport_pbn_volume(toplevel)
    assert toplevel[0].text == "brak"

    toplevel = etree.fromstring("<body></body>")
    wydawnictwo_ciagle.informacje = "2016 vol 4"
    wydawnictwo_ciagle.eksport_pbn_volume(toplevel)
    assert toplevel[0].text == "4"


@pytest.mark.parametrize("informacje,expected",
                         [("bez sensu", None),
                          ("2016 vol. 5 nr 10", "10"),
                          ("2019 Bd 4 nr. 3 test", "3"),
                          ("2019 Bd 4 nr 3 test", "3"),
                          ("2019 Bd 4 z. 3 test", "3"),
                          ("2019 Bd 4 h. 3 test", "3")])
def test_eksport_pbn_get_issue(informacje, expected, wydawnictwo_ciagle):
    wydawnictwo_ciagle.informacje = informacje
    assert wydawnictwo_ciagle.eksport_pbn_get_issue() == expected


def test_eksport_pbn_issue(wydawnictwo_ciagle):
    toplevel = etree.fromstring("<body></body>")
    wydawnictwo_ciagle.informacje = "2016 vol 4"
    wydawnictwo_ciagle.eksport_pbn_issue(toplevel)
    assert toplevel[0].text == "brak"

    toplevel = etree.fromstring("<body></body>")
    wydawnictwo_ciagle.informacje = "2016 vol 4 nr 5B"
    wydawnictwo_ciagle.eksport_pbn_issue(toplevel)
    assert toplevel[0].text == "5B"
