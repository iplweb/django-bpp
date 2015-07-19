# -*- encoding: utf-8 -*-
from collections import namedtuple
import json

from django.test import TestCase
from bpp.models.zrodlo import Punktacja_Zrodla
from bpp.tests.util import any_zrodlo, CURRENT_YEAR, any_autor, \
    any_habilitacja, any_jednostka
from bpp.views.api import PunktacjaZrodlaView, RokHabilitacjiView, \
    UploadPunktacjaZrodlaView, OstatniaJednostkaView

FakeRequest = namedtuple("FakeRequest", ["POST"])


class TestRokHabilitacjiView(TestCase):
    fixtures = ['charakter_formalny.json', 'typ_odpowiedzialnosci.json']

    def test_rokhabilitacjiview(self):
        a = any_autor()
        h = any_habilitacja(tytul_oryginalny='Testowa habilitacja', rok=CURRENT_YEAR)
        h.autor = a
        h.save()

        request = FakeRequest({'autor_pk': a.pk})

        rhv = RokHabilitacjiView()

        res = rhv.post(request)
        self.assertContains(res, str(CURRENT_YEAR), status_code=200)
        self.assertEquals(json.loads(res.content)['rok'], CURRENT_YEAR)

        h.delete()
        res = rhv.post(request)
        self.assertContains(res, "Habilitacja", status_code=404)

        a.delete()
        res = rhv.post(request)
        self.assertContains(res, "Autor", status_code=404)


class TestPunktacjaZrodlaView(TestCase):
    def test_punktacjazrodlaview(self):
        z = any_zrodlo()
        Punktacja_Zrodla.objects.create(
            zrodlo=z, rok=CURRENT_YEAR,
            impact_factor=50)

        res = PunktacjaZrodlaView().post(None, z.pk, CURRENT_YEAR)
        analyze = json.loads(str(res.content))
        self.assertEquals(analyze['impact_factor'], '50.000')

        res = PunktacjaZrodlaView().post(None, z.pk, CURRENT_YEAR + 100)
        self.assertContains(res, "Rok", status_code=404)

    def test_punktacjazrodlaview_404(self):
        res = PunktacjaZrodlaView().post(None, 1, CURRENT_YEAR)
        self.assertContains(res, "Zrodlo", status_code=404)


class TestUploadPunktacjaZrodlaView(TestCase):
    def test_upload_punktacja_zrodla_404(self):
        res = UploadPunktacjaZrodlaView().post(None, 1, CURRENT_YEAR)
        self.assertContains(res, "Zrodlo", status_code=404)

    def test_upload_punktacja_zrodla_simple(self):
        z = any_zrodlo()
        fr = FakeRequest(dict(impact_factor="50.00"))
        res = UploadPunktacjaZrodlaView().post(fr, z.pk, CURRENT_YEAR)
        self.assertEquals(Punktacja_Zrodla.objects.count(), 1)
        self.assertEquals(Punktacja_Zrodla.objects.all()[0].impact_factor, 50)

    def test_upload_punktacja_zrodla_overwrite(self):
        z = any_zrodlo()
        pz = Punktacja_Zrodla.objects.create(rok=CURRENT_YEAR, zrodlo=z,
                                             impact_factor=50)
        fr = FakeRequest(dict(impact_factor="60.00", punkty_kbn="60"))
        res = UploadPunktacjaZrodlaView().post(fr, z.pk, CURRENT_YEAR)
        self.assertContains(res, "exists", status_code=200)

        fr = FakeRequest(dict(impact_factor="60.00", overwrite="1"))
        res = UploadPunktacjaZrodlaView().post(fr, z.pk, CURRENT_YEAR)
        self.assertEquals(Punktacja_Zrodla.objects.count(), 1)
        self.assertEquals(Punktacja_Zrodla.objects.all()[0].impact_factor, 60)


class TestOstatniaJednostkaView(TestCase):
    def test_ostatnia_jednostka_view(self):
        ojv = OstatniaJednostkaView()
        a = any_autor()
        j = any_jednostka()
        j.dodaj_autora(a)

        fr = FakeRequest(dict(autor_id=a.pk))
        res = ojv.post(fr)
        self.assertContains(res, "jednostka_id", status_code=200)

    def test_ostatnia_jednostka_errors(self):
        ojv = OstatniaJednostkaView()
        fr = FakeRequest(dict(autor_id=None))

        res = ojv.post(fr)
        self.assertContains(res, "Autor", status_code=404)

        fr = FakeRequest(dict(autor_id=10))
        res = ojv.post(fr)
        self.assertContains(res, "Autor", status_code=404)

        a = any_autor()
        fr = FakeRequest(dict(autor_id=a.pk))
        res = ojv.post(fr)
        self.assertContains(res, "Jednostka", status_code=404)
