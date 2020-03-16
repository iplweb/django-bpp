import urllib
from datetime import datetime
from urllib.parse import urlencode

from django.contrib.postgres.aggregates.general import StringAgg
from django.db import connection
from django.db.models import F, Max, Min, Sum, Window
from django.db.models.fields import TextField
from django.db.models.functions import Cast
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import FormView, TemplateView
from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin

from bpp.models import (
    Autor,
    Cache_Punktacja_Autora_Query,
    Cache_Punktacja_Autora_Query_View,
    Cache_Punktacja_Autora_Sum,
    Cache_Punktacja_Autora_Sum_Group_Ponizej,
    Cache_Punktacja_Autora_Sum_Gruop,
    Cache_Punktacja_Autora_Sum_Ponizej,
    Dyscyplina_Naukowa,
)
from bpp.models.dyscyplina_naukowa import Autor_Dyscyplina
from bpp.views.mixins import UczelniaSettingRequiredMixin
from django_bpp.version import VERSION
from raport_slotow.filters import (
    RaportSlotowUczelniaFilter,
    RaportZerowyFilter,
    RaportSlotowUczelniaBezJednostekIWydzialowFilter,
)
from raport_slotow.forms import (
    AutorRaportSlotowForm,
    ParametryRaportSlotowUczelniaForm,
    ParametryRaportSlotowEwaluacjaForm,
)
from raport_slotow.models import RaportZerowyEntry
from raport_slotow.tables import (
    RaportSlotowAutorTable,
    RaportSlotowUczelniaBezJednostekIWydzialowTable,
    RaportSlotowUczelniaTable,
    RaportSlotowZerowyTable,
)
from raport_slotow.util import (
    MyExportMixin,
    MyTableExport,
    clone_temporary_table,
    create_temporary_table_as,
    insert_into,
)


class WyborOsoby(UczelniaSettingRequiredMixin, FormView):
    template_name = "raport_slotow/index.html"
    form_class = AutorRaportSlotowForm
    uczelnia_attr = "pokazuj_raport_slotow_autor"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Wybór autora"
        return context

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        return HttpResponseRedirect(
            reverse(
                "raport_slotow:raport",
                kwargs={
                    "autor": form.cleaned_data["obiekt"].slug,
                    "od_roku": form.cleaned_data["od_roku"],
                    "do_roku": form.cleaned_data["do_roku"],
                },
            )
            + "?_export="
            + form.cleaned_data["_export"]
        )


class RaportSlotow(
    UczelniaSettingRequiredMixin, MyExportMixin, MultiTableMixin, TemplateView
):
    template_name = "raport_slotow/raport_slotow_autor.html"
    table_class = RaportSlotowAutorTable
    uczelnia_attr = "pokazuj_raport_slotow_autor"
    export_formats = ["html", "xlsx"]

    def create_export(self, export_format):
        tables = self.get_tables()
        n = int(self.request.GET.get("n", 0))
        exporter = MyTableExport(
            export_format=export_format,
            table=tables[n],
            export_description=[
                ("Nazwa raportu:", "raport slotów - autor"),
                ("Autor:", str(self.autor)),
                (f"Dyscyplina:", str(tables[n].dyscyplina_naukowa or "żadna")),
                (f"Od roku:", self.od_roku),
                (f"Do roku:", self.do_roku),
                ("Wygenerowano:", timezone.now()),
                ("Wersja oprogramowania BPP", VERSION),
            ],
        )
        return exporter.response(filename=self.get_export_filename(export_format, n))

    def get_tables(self):
        self.autor = get_object_or_404(Autor, slug=self.kwargs.get("autor"))
        try:
            self.od_roku = int(self.kwargs.get("od_roku"))
            self.do_roku = int(self.kwargs.get("do_roku"))
        except (TypeError, ValueError):
            raise Http404

        cpaq = Cache_Punktacja_Autora_Query_View.objects.filter(
            autor=self.autor,
            rekord__rok__gte=self.od_roku,
            rekord__rok__lte=self.do_roku,
            pkdaut__gt=0,
        )

        ret = []
        for elem in cpaq.values_list("dyscyplina", flat=True).order_by().distinct():
            table_class = self.get_table_class()
            table = table_class(
                data=cpaq.filter(dyscyplina_id=elem).select_related(
                    "rekord", "dyscyplina", "rekord__zrodlo"
                )
            )
            RequestConfig(
                self.request, paginate=self.get_table_pagination(table)
            ).configure(table)
            table.dyscyplina_naukowa = Dyscyplina_Naukowa.objects.get(pk=elem)
            ret.append(table)

        if not ret:
            table_class = self.get_table_class()
            table = table_class(data=cpaq.select_related("rekord", "dyscyplina"))
            RequestConfig(
                self.request, paginate=self.get_table_pagination(table)
            ).configure(table)
            table.dyscyplina_naukowa = None
            ret.append(table)

        return ret

    def get_queryset(self):
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RaportSlotow, self).get_context_data(**kwargs)
        context["autor"] = self.autor
        context["od_roku"] = self.od_roku
        context["do_roku"] = self.do_roku
        return context

    def get_export_filename(self, export_format, n):
        return f"raport_slotow_{self.autor.slug}_{self.od_roku}-{self.do_roku}-{n}.{export_format}"
