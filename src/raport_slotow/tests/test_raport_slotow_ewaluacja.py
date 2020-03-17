import pytest
from django.urls import reverse

from raport_slotow.models import RaportUczelniaEwaluacjaView


def test_raport_slotow_ewaluacja_parametry_view(admin_client):
    res = admin_client.get(reverse("raport_slotow:index-ewaluacja"))
    assert res.status_code == 200


def test_raport_slotow_ewaluacja_parametry_view_post(admin_client):
    res = admin_client.post(
        reverse("raport_slotow:index-ewaluacja"), {"rok": 2020, "_export": "html"},
    )
    assert res.status_code == 302


def test_raport_slotow_ewaluacja_raport(admin_client, praca_z_dyscyplina):
    res = admin_client.get(
        reverse("raport_slotow:raport-ewaluacja") + "?_export=html&rok=2020"
    )
    assert res.status_code == 200


def test_raport_slotow_ewaluacja_raport_xlsx(admin_client, praca_z_dyscyplina):
    res = admin_client.get(
        reverse("raport_slotow:raport-ewaluacja") + "?_export=xlsx&rok=2020"
    )
    assert res.status_code == 200


@pytest.mark.django_db
def test_RaportUczelniaEwaluacjaView_model(praca_z_dyscyplina):
    assert RaportUczelniaEwaluacjaView.objects.all().count() == 1
