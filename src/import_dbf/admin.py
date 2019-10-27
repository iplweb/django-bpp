from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from import_dbf import models as import_dbf_models
from import_dbf.models import Bib, Aut, Jed, B_A, B_U, Poz, Usi, Ses, Wx2, Ixn, Wyd, Ldy, B_E, Lis, B_L, J_H, Pub, Kbn, \
    Jez, Loc


class ImportDbfBaseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ImportDbfBaseAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


class PozInline(admin.TabularInline):
    model = Poz
    extra = 0

@admin.register(Bib)
class BibAdmin(ImportDbfBaseAdmin):
    list_display = ['idt', 'tytul_or', 'title', 'zrodlo', 'szczegoly', 'uwagi']
    search_fields = ['tytul_or', 'title', 'zrodlo', 'szczegoly', 'uwagi', "zrodlo_s"]
    list_filter = ['kbr', 'lf', 'study_gr', 'kwartyl']
    readonly_fields = ['object_id', 'content_type']

    inlines = [PozInline]


@admin.register(Aut)
class AutAdmin(ImportDbfBaseAdmin):
    list_display = ['nazwisko', 'imiona', 'tytul', 'stanowisko', 'prac_od', 'dat_zwol', 'orcid_id', 'exp_id', 'ref',
                    'kad_nr', 'idt_jed', 'tel', 'email', 'fg', 'pbn_id']
    search_fields = ['nazwisko', 'imiona', 'ref', 'tel', 'email']
    autocomplete_fields = ['idt_jed']
    list_filter = ['fg', 'tytul']
    readonly_fields = ['bpp_autor', ]


@admin.register(Kbn)
class KbnAdmin(ImportDbfBaseAdmin):
    list_display = ['idt_kbn', 'nazwa', 'skrot', 'to_print', 'to_print2', 'to_print3']
    list_filter = ['to_print', 'to_print2']
    readonly_fields = ['bpp_id']


@admin.register(Jez)
class JezAdmin(ImportDbfBaseAdmin):
    list_display = ['nazwa', 'skrot', ]
    readonly_fields = ['bpp_id']


@admin.register(Jed)
class JedAdmin(ImportDbfBaseAdmin):
    list_display = ['nazwa', 'skrot', 'wyd_skrot', 'email', 'www', 'to_print']
    search_fields = ['nazwa', 'skrot']
    list_filter = ['to_print', 'wyd_skrot']
    readonly_fields = ['bpp_jednostka']


@admin.register(B_A)
class B_AAdmin(ImportDbfBaseAdmin):
    list_display = ['idt', 'idt_aut', 'idt_jed', 'lp']


@admin.register(Poz)
class PozAdmin(ImportDbfBaseAdmin):
    list_display = ['idt', 'kod_opisu', 'lp', 'tresc']
    search_fields = ['idt__tytul_or', 'tresc']
    autocomplete_fields = ['idt']
    list_select_related = ['idt']
    list_filter = ['kod_opisu']


@admin.register(B_U)
class BUAdmin(ImportDbfBaseAdmin):
    list_display = ['idt', 'idt_usi', 'comm']
    autocomplete_fields = ['idt_usi', 'idt']


@admin.register(Usi)
class UsiAdmin(ImportDbfBaseAdmin):
    list_display = ['idt_usi', 'usm_f', 'usm_sf', 'skrot', 'nazwa']
    search_fields = ['idt_usi', 'skrot', 'nazwa']
    list_filter = ['usm_f', 'usm_sf']
    autocomplete_fields = ['bpp_id']


@admin.register(Ses)
class SesAdmin(ImportDbfBaseAdmin):
    list_display = ['redaktor', 'file', 'login_t', 'logout_t']


@admin.register(Wx2)
class Wx2Admin(ImportDbfBaseAdmin):
    list_display = ['idt_wsx', 'skrot', 'nazwa', 'wsp']


@admin.register(Ixn)
class IxnAdmin(ImportDbfBaseAdmin):
    list_display = ['idt_pbn', 'pbn']


@admin.register(Wyd)
class WydAdmin(ImportDbfBaseAdmin):
    list_display = ['skrot', 'nazwa']


@admin.register(Ldy)
class WydAdmin(ImportDbfBaseAdmin):
    list_display = ['id', 'dziedzina', 'dyscyplina']


@admin.register(B_E)
class B_EAdmin(ImportDbfBaseAdmin):
    list_display = ['idt', 'lp', 'idt_eng']


@admin.register(Lis)
class LisAdmin(ImportDbfBaseAdmin):
    list_display = ['rok', 'kategoria', 'numer', 'tytul', 'issn', 'punkty', 'sobowtor', 'errissn', 'dblissn',
                    'dbltitul']
    list_filter = ['rok', 'kategoria', 'punkty']
    search_fields = ['rok', 'kategoria', 'numer', 'tytul', 'issn']


@admin.register(B_L)
class B_LAdmin(ImportDbfBaseAdmin):
    list_display = ['idt', 'idt_l']


@admin.register(J_H)
class J_HAdmin(ImportDbfBaseAdmin):
    list_display = ['idt_jed_f', 'idt_jed_t', 'rok']


@admin.register(Pub)
class PubAdmin(ImportDbfBaseAdmin):
    list_display = ['idt_pub', 'skrot', 'nazwa', 'to_print']
    readonly_fields = ['bpp_id']


@admin.register(Loc)
class LocAdmin(ImportDbfBaseAdmin):
    list_display = ['ident', 'ext']


for elem in import_dbf_models.__all__:
    klass = getattr(import_dbf_models, elem)

    try:
        @admin.register(klass)
        class KlassAdmin(ImportDbfBaseAdmin):
            pass
    except AlreadyRegistered:
        pass
