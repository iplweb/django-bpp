# -*- encoding: utf-8 -*-
# -*- encoding: utf-8 -*-

"""W tym pakiecie znajdują się procedury generujące raporty, które są dostępne
"od ręki" -- generowane za pomocą WWW"""
from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, ButtonHolder, \
    Submit, Hidden, Row, Column as F4Column
from dal import autocomplete
from django import forms
from django.core import validators
from django_tables2.export.export import TableExport

from bpp.models import Wydzial
from bpp.models.autor import Autor
from bpp.models.struktura import Jednostka


def ustaw_rok(rok, lata):
    lata = list(lata)
    try:
        rok.field.min_value = lata[0]
    except IndexError:
        pass

    try:
        rok.field.max_value = lata[-1]
        rok.field.initial = lata[-2]
    except IndexError:
        pass

    if rok.field.max_value is not None:
        rok.field.validators.append(validators.MaxValueValidator(rok.field.max_value))
    if rok.field.min_value is not None:
        rok.field.validators.append(validators.MinValueValidator(rok.field.min_value))


class KronikaUczelniForm(forms.Form):
    rok = forms.IntegerField()

    def __init__(self, lata, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Kronika Uczelni',
                'rok',
                Hidden("report", "kronika-uczelni")
            ),
            ButtonHolder(
                Submit('submit', 'Zamów', css_class='button white')
            )
        )
        super(KronikaUczelniForm, self).__init__(*args, **kwargs)
        ustaw_rok(self['rok'], lata)


class RaportJednostekForm(forms.Form):
    jednostka = forms.ModelChoiceField(
        queryset=Jednostka.objects.filter(widoczna=True),
        widget=autocomplete.ModelSelect2(
            url='bpp:jednostka-widoczna-autocomplete')
    )

    od_roku = forms.IntegerField()
    do_roku = forms.IntegerField()
    output = forms.BooleanField(label="Pobierz jako plik Microsoft Word", required=False)

    def __init__(self, lata, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = "#RaportJednostek"

        self.helper.layout = Layout(
            Fieldset(
                'Raport jednostek',
                Row(F4Column('jednostka', css_class='large-12 small-12')),
                Row(F4Column('od_roku', css_class='large-6 small-6'),
                    F4Column('do_roku', css_class='large-6 small-6')),
                Row(F4Column('output', css_class='large-12 small-12')),
                Hidden("report", "raport-jednostek")
            ),
            ButtonHolder(
                Submit('submit', 'Wyświetl', css_class='button'),
            )
        )

        super(RaportJednostekForm, self).__init__(*args, **kwargs)
        ustaw_rok(self['od_roku'], lata)
        ustaw_rok(self['do_roku'], lata)


class RaportAutorowForm(forms.Form):
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='bpp:autor-z-uczelni-autocomplete')
    )
    od_roku = forms.IntegerField()
    do_roku = forms.IntegerField()
    output = forms.BooleanField(label="Pobierz jako plik Microsoft Word", required=False)

    def __init__(self, lata, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = "#RaportAutorow"

        # self.helper.form_action = "./prepare/"
        self.helper.layout = Layout(
            Fieldset(
                'Raport autorów',
                Row(F4Column('autor', css_class='large-12 small-12')),
                Row(F4Column('od_roku', css_class='large-6 small-6'),
                    F4Column('do_roku', css_class='large-6 small-6')),
                Row(F4Column("output", css_class="large-12 small-12")),
                Hidden("report", "raport-autorow")
            ),
            ButtonHolder(
                Submit('submit', 'Szukaj', css_class='button white')
            )
        )

        super(RaportAutorowForm, self).__init__(*args, **kwargs)
        ustaw_rok(self['od_roku'], lata)
        ustaw_rok(self['do_roku'], lata)


class RaportDlaKomisjiCentralnejForm(forms.Form):
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='bpp:autor-z-uczelni-autocomplete')
    )

    rok_habilitacji = forms.IntegerField(required=False)

    def __init__(self, lata, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = "#RaportDlaKomisjiCentralnej"
        # self.helper.form_action = "./prepare/"
        self.helper.layout = Layout(
            Fieldset(
                'Raport dla Komisji Centralnej',
                'autor',
                'rok_habilitacji',
                Hidden("report", "raport-dla-komisji-centralnej")
            ),
            ButtonHolder(
                Submit('submit', 'Zamów', css_class='button white')
            )
        )

        super(RaportDlaKomisjiCentralnejForm, self).__init__(*args, **kwargs)
        ustaw_rok(self['rok_habilitacji'], lata)


class WydzialChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.nazwa


OUTPUT_FORMATS = [
    ('html', 'wyświetl w przeglądarce'),
]

OUTPUT_FORMATS.extend(zip(
    list(TableExport.FORMATS.keys()),
    list(TableExport.FORMATS.keys()),
))


class RankingAutorowForm(forms.Form):
    wydzialy = WydzialChoiceField(
        label="Ogranicz do wydziału (wydziałów):",
        required=False,
        widget=forms.SelectMultiple(attrs={'size': '15'}),
        queryset=Wydzial.objects.filter(widoczny=True, zezwalaj_na_ranking_autorow=True),
        help_text="Jeżeli nie wybierzesz żadnego wydziału, system wygeneruje "
                  "dane dla wszystkich wydziałów. Przytrzymaj przycisk CTRL ("
                  "CMD na Maku) gdy klikasz, aby wybrać więcej, niż jeden "
                  "wydział lub odznaczyć już zaznaczony wydział. ")

    od_roku = forms.IntegerField()
    do_roku = forms.IntegerField()

    _export = forms.ChoiceField(
        label="Format wyjściowy",
        required=True,
        choices=OUTPUT_FORMATS
    )

    def __init__(self, lata, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Fieldset(
                'Ranking autorów',
                Row(
                    F4Column('od_roku', css_class='large-6 small-6'),
                    F4Column('do_roku', css_class='large-6 small-6'),
                ),
                Row(
                    F4Column('_export', css_class='large-12 small-12')
                ),
                Row(
                    F4Column('wydzialy', css_class='large-12 small-12')
                ),
                Hidden("report", "ranking-autorow")
            ),
            ButtonHolder(
                Submit('submit', 'Otwórz', css_class='button white')
            )
        )

        super(RankingAutorowForm, self).__init__(*args, **kwargs)
        ustaw_rok(self['od_roku'], lata)
        ustaw_rok(self['do_roku'], lata)
