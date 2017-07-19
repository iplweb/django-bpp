# -*- encoding: utf-8 -*-

from dal import autocomplete
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from bpp.admin.filters import LiczbaZnakowFilter
from bpp.admin.helpers import *
from bpp.models import Zrodlo, Wydawnictwo_Ciagle  # Publikacja_Habilitacyjna
# Proste tabele
from bpp.models.konferencja import Konferencja
from bpp.models.wydawnictwo_ciagle import Wydawnictwo_Ciagle_Autor
from .common import CommitedModelAdmin, \
    KolumnyZeSkrotamiMixin, generuj_inline_dla_autorow


#
# Wydaniwcto Ciągłe
#


# Widget do automatycznego uzupełniania punktacji wydawnictwa ciągłego

class Button(forms.Widget):
    """
    A widget that handles a submit button.
    """

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(
            self.attrs,
            type="button",
            name=name)

        return mark_safe('<input type="button"%s value="%s" />' % (
            forms.widgets.flatatt(final_attrs),
            final_attrs['label'],
        ))


class Wydawnictwo_CiagleForm(forms.ModelForm):
    zrodlo = forms.ModelChoiceField(
        queryset=Zrodlo.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='bpp:zrodlo-autocomplete')
    )

    uzupelnij_punktacje = forms.CharField(
        initial=None,
        max_length=50,
        required=False,
        label="Uzupełnij punktację",
        widget=Button(dict(
            id='id_uzupelnij_punktacje',
            label="Uzupełnij punktację",
        ))
    )

    konferencja = forms.ModelChoiceField(
        required=False,
        queryset=Konferencja.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='bpp:konferencja-autocomplete',
            attrs=dict(style="width: 746px;")
        )
    )

    class Meta:
        fields = "__all__"

        widgets = {
            'strony': forms.TextInput(attrs=dict(style="width: 150px")),
            'tom': forms.TextInput(attrs=dict(style="width: 150px")),
            'nr_zeszytu': forms.TextInput(attrs=dict(style="width: 150px"))
        }


class Wydawnictwo_CiagleAdmin(KolumnyZeSkrotamiMixin,
                              AdnotacjeZDatamiOrazPBNMixin,
                              CommitedModelAdmin):
    formfield_overrides = NIZSZE_TEXTFIELD_Z_MAPA_ZNAKOW

    form = Wydawnictwo_CiagleForm

    list_display = ['tytul_oryginalny',
                    'zrodlo_col',
                    'rok',
                    'typ_kbn__skrot',
                    'charakter_formalny__skrot',
                    'liczba_znakow_wydawniczych',
                    'ostatnio_zmieniony']

    list_select_related = ['zrodlo', 'typ_kbn', 'charakter_formalny']

    search_fields = [
        'tytul', 'tytul_oryginalny', 'szczegoly', 'uwagi', 'informacje',
        'slowa_kluczowe', 'rok', 'id',
        'issn', 'e_issn', 'zrodlo__nazwa', 'zrodlo__skrot', 'adnotacje',
        'liczba_znakow_wydawniczych',
        'konferencja__nazwa'
    ]

    list_filter = ['status_korekty', 'afiliowana', 'recenzowana', 'typ_kbn',
                   'charakter_formalny', 'jezyk', LiczbaZnakowFilter, 'rok',
                   'openaccess_tryb_dostepu',
                   'openaccess_wersja_tekstu',
                   'openaccess_licencja',
                   'openaccess_czas_publikacji',
                   ]

    fieldsets = (
        ('Wydawnictwo ciągłe', {
            'fields':
                DWA_TYTULY
                + ('zrodlo', 'konferencja',)
                + MODEL_ZE_SZCZEGOLAMI
                + ('nr_zeszytu',)
                + MODEL_Z_ROKIEM
        }),
        EKSTRA_INFORMACJE_WYDAWNICTWO_CIAGLE_FIELDSET,
        MODEL_TYPOWANY_FIELDSET,
        MODEL_PUNKTOWANY_WYDAWNICTWO_CIAGLE_FIELDSET,
        MODEL_PUNKTOWANY_KOMISJA_CENTRALNA_FIELDSET,
        POZOSTALE_MODELE_WYDAWNICTWO_CIAGLE_FIELDSET,
        ADNOTACJE_Z_DATAMI_ORAZ_PBN_FIELDSET,
        OPENACCESS_FIELDSET)

    inlines = (
        generuj_inline_dla_autorow(Wydawnictwo_Ciagle_Autor),
    )

    def zrodlo_col(self, obj):
        try:
            return obj.zrodlo.nazwa
        except Zrodlo.DoesNotExist:
            return ''

    zrodlo_col.admin_order_field = 'zrodlo__nazwa'
    zrodlo_col.short_description = "Źródło"


admin.site.register(Wydawnictwo_Ciagle, Wydawnictwo_CiagleAdmin)