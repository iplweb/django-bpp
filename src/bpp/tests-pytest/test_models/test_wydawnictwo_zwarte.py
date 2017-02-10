# -*- encoding: utf-8 -*-

import pytest
from lxml.etree import Element
from model_mommy import mommy

from bpp.models.autor import Autor
from bpp.models.struktura import Wydzial, Jednostka, Uczelnia
from bpp.models.system import Typ_Odpowiedzialnosci, Charakter_Formalny
from bpp.models.wydawnictwo_zwarte import Wydawnictwo_Zwarte


def test_serializuj_pbn_zwarte(wydawnictwo_zwarte_z_autorem, wydzial):
    wydawnictwo_zwarte_z_autorem.eksport_pbn_serializuj(wydzial)


def test_liczba_arkuszy_wydawniczych(wydawnictwo_zwarte_z_autorem):
    wydawnictwo_zwarte_z_autorem.liczba_znakow_wydawniczych = 41000
    assert wydawnictwo_zwarte_z_autorem.liczba_arkuszy_wydawniczych() == "1.02"

    wydawnictwo_zwarte_z_autorem.liczba_znakow_wydawniczych = 39000
    assert wydawnictwo_zwarte_z_autorem.liczba_arkuszy_wydawniczych() == "0.97"

    wydawnictwo_zwarte_z_autorem.liczba_znakow_wydawniczych = 60000
    assert wydawnictwo_zwarte_z_autorem.liczba_arkuszy_wydawniczych() == "1.50"

    wydawnictwo_zwarte_z_autorem.liczba_znakow_wydawniczych = 20000
    assert wydawnictwo_zwarte_z_autorem.liczba_arkuszy_wydawniczych() == "0.50"


def test_eksport_pbn_size(wydawnictwo_zwarte_z_autorem):
    """
    :type wydawnictwo_zwarte_z_autorem: bpp.models.Wydawnictwo_Zwarte
    """
    wydawnictwo_zwarte_z_autorem.liczba_znakow_wydawniczych = 20000
    toplevel = Element("fa")
    wydawnictwo_zwarte_z_autorem.eksport_pbn_size(toplevel)
    assert toplevel.getchildren()[0].text == "0.50"


@pytest.mark.django_db
def test_eksport_pbn_wydawnictwo_nadrzedne_liczba_autorow():
    """

    :type wydawnictwo_zwarte_z_autorem: bpp.models.Wydawnictwo_Zwarte
    :return:
    """

    u = mommy.make(Uczelnia)

    w1 = mommy.make(Wydzial, uczelnia=u)
    w2 = mommy.make(Wydzial, uczelnia=u)

    a1 = mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")
    a2 = mommy.make(Autor, imiona="Stefan", nazwisko="Nowak")

    j1 = mommy.make(Jednostka, wydzial=w1, uczelnia=u)
    j2 = mommy.make(Jednostka, wydzial=w2, uczelnia=u)

    chf_ksp, created = Charakter_Formalny.objects.get_or_create(skrot='KSP', nazwa="Książka w języku polskim")
    if created:
        chf_ksp.ksiazka_pbn = True
        chf_ksp.save()

    chf_roz, created = Charakter_Formalny.objects.get_or_create(skrot='ROZ', nazwa="Rozdział książki")
    if created:
        chf_roz.rozdzial_pbn = True
        chf_roz.save()

    wz_root = mommy.make(Wydawnictwo_Zwarte, charakter_formalny=chf_ksp, szczegoly="s. 123",
                         calkowita_liczba_autorow=50)
    wz_child1 = mommy.make(Wydawnictwo_Zwarte, wydawnictwo_nadrzedne=wz_root, charakter_formalny=chf_roz,
                           szczegoly="s. 10-15")
    wz_child2 = mommy.make(Wydawnictwo_Zwarte, wydawnictwo_nadrzedne=wz_root, charakter_formalny=chf_roz,
                           szczegoly="s. 16-25")

    Typ_Odpowiedzialnosci.objects.get_or_create(skrot="aut.")
    Typ_Odpowiedzialnosci.objects.get_or_create(skrot="red.")

    wz_root.dodaj_autora(a1, j1, typ_odpowiedzialnosci_skrot="red.")
    wz_root.dodaj_autora(a2, j2, typ_odpowiedzialnosci_skrot="red.")

    wz_child1.dodaj_autora(a1, j1, typ_odpowiedzialnosci_skrot="aut.")
    wz_child1.dodaj_autora(a2, j2, typ_odpowiedzialnosci_skrot="aut.")

    wz_child2.dodaj_autora(a1, j1, typ_odpowiedzialnosci_skrot="aut.")
    wz_child2.dodaj_autora(a2, j2, typ_odpowiedzialnosci_skrot="aut.")

    ret = wz_root.eksport_pbn_serializuj(w1)

    assert len(ret.findall("editor")) == 1
    assert ret.find("other-editors").text == "1"

    assert len(ret.findall("author")) == 1
    assert ret.find("other-contributors").text == "49"


@pytest.mark.django_db
def test_eksport_pbn_wydawnictwo_nadrzedne_liczba_autorow_trzech():
    """

    :type wydawnictwo_zwarte_z_autorem: bpp.models.Wydawnictwo_Zwarte
    :return:
    """

    u = mommy.make(Uczelnia)

    w1 = mommy.make(Wydzial, uczelnia=u)
    w2 = mommy.make(Wydzial, uczelnia=u)

    a1 = mommy.make(Autor, imiona="Jan", nazwisko="Kowalski")
    a2 = mommy.make(Autor, imiona="Stefan", nazwisko="Nowak")
    a3 = mommy.make(Autor, imiona="Joe", nazwisko="Moore")

    j1 = mommy.make(Jednostka, wydzial=w1, uczelnia=u)
    j2 = mommy.make(Jednostka, wydzial=w2, uczelnia=u)

    chf_ksp, created = Charakter_Formalny.objects.get_or_create(skrot='KSP', nazwa="Książka w języku polskim")
    if created:
        chf_ksp.ksiazka_pbn = True
        chf_ksp.save()

    chf_roz, created = Charakter_Formalny.objects.get_or_create(skrot='ROZ', nazwa="Rozdział książki")
    if created:
        chf_roz.rozdzial_pbn = True
        chf_roz.save()

    wz_root = mommy.make(Wydawnictwo_Zwarte, charakter_formalny=chf_ksp, szczegoly="s. 123",
                         calkowita_liczba_autorow=50)
    wz_child1 = mommy.make(Wydawnictwo_Zwarte, wydawnictwo_nadrzedne=wz_root, charakter_formalny=chf_roz,
                           szczegoly="s. 10-15")
    wz_child2 = mommy.make(Wydawnictwo_Zwarte, wydawnictwo_nadrzedne=wz_root, charakter_formalny=chf_roz,
                           szczegoly="s. 16-25")

    Typ_Odpowiedzialnosci.objects.get_or_create(skrot="aut.")
    Typ_Odpowiedzialnosci.objects.get_or_create(skrot="red.")

    wz_root.dodaj_autora(a1, j1, typ_odpowiedzialnosci_skrot="red.")
    wz_root.dodaj_autora(a2, j2, typ_odpowiedzialnosci_skrot="red.")

    wz_child1.dodaj_autora(a1, j1, typ_odpowiedzialnosci_skrot="aut.")
    wz_child1.dodaj_autora(a2, j2, typ_odpowiedzialnosci_skrot="aut.")
    wz_child1.dodaj_autora(a3, j1, typ_odpowiedzialnosci_skrot="aut.")

    wz_child2.dodaj_autora(a1, j1, typ_odpowiedzialnosci_skrot="aut.")
    wz_child2.dodaj_autora(a2, j2, typ_odpowiedzialnosci_skrot="aut.")

    ret = wz_root.eksport_pbn_serializuj(w1)

    assert len(ret.findall("editor")) == 1
    assert ret.find("other-editors").text == "1"

    assert len(ret.findall("author")) == 2
    assert ret.find("other-contributors").text == "48"
