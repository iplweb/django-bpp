from decimal import Decimal
from math import sqrt

from .common import SlotMixin


class SlotKalkulator_Wydawnictwo_Ciagle_Prog1(SlotMixin):
    """
    Artykuł z czasopisma z listy ministerialnej.
    Dla roku 2017, 2018: punkty KBN >= 30
    """

    def punkty_pkd(self, dyscyplina):
        if self.ma_dyscypline(dyscyplina):
            return self.original.punkty_kbn

    def slot_dla_autora_z_dyscypliny(self, dyscyplina):
        azd = self.autorzy_z_dyscypliny(dyscyplina).count()
        if azd == 0:
            return
        return Decimal("1") / azd

    def slot_dla_dyscypliny(self, dyscyplina):
        if self.ma_dyscypline(dyscyplina):
            return Decimal("1")


class KPrzezMMixin:
    def k_przez_m(self, dyscyplina):
        if self.wszyscy() == 0:
            return
        return self.autorzy_z_dyscypliny(dyscyplina).count() / self.wszyscy()


class SlotKalkulator_Wydawnictwo_Ciagle_Prog2(KPrzezMMixin, SlotMixin):
    """
    Artykuł z czasopisma z listy ministerialnej.

    Dla roku 2017-2018: punkty KBN 20 lub 25
    """

    def pierwiastek_k_przez_m(self, dyscyplina):
        k_przez_m = self.k_przez_m(dyscyplina)
        if k_przez_m is None:
            return
        return sqrt(k_przez_m)

    def punkty_pkd(self, dyscyplina):
        if self.ma_dyscypline(dyscyplina):
            return self.original.punkty_kbn * max(self.pierwiastek_k_przez_m(dyscyplina), 0.1)

    def slot_dla_autora_z_dyscypliny(self, dyscyplina):
        if not self.ma_dyscypline(dyscyplina):
            return

        azd = self.autorzy_z_dyscypliny(dyscyplina).count()
        if azd > 0:
            return self.pierwiastek_k_przez_m(dyscyplina) * 1 / azd

    def slot_dla_dyscypliny(self, dyscyplina):
        if not self.ma_dyscypline(dyscyplina):
            return

        return self.pierwiastek_k_przez_m(dyscyplina)


class SlotKalkulator_Wydawnictwo_Ciagle_Prog3(KPrzezMMixin, SlotMixin):
    """
    Artykuł z czasopisma z listy ministerialnej.

    Dla roku 2017-2018: punkty KBN poniżej 20 lub 5
    """

    def punkty_pkd(self, dyscyplina):
        if self.ma_dyscypline(dyscyplina):
            k_przez_m = self.k_przez_m(dyscyplina)
            if k_przez_m is None:
                return
            return self.original.punkty_kbn * max(k_przez_m, 0.1)

    def jeden_przez_wszyscy(self):
        w = self.wszyscy()
        if w == 0:
            return
        return 1 / w

    def slot_dla_autora_z_dyscypliny(self, dyscyplina):
        if not self.ma_dyscypline(dyscyplina):
            return
        return self.jeden_przez_wszyscy()

    def slot_dla_dyscypliny(self, dyscyplina):
        if not self.ma_dyscypline(dyscyplina):
            return
        return self.jeden_przez_wszyscy() * self.autorzy_z_dyscypliny(dyscyplina).count()