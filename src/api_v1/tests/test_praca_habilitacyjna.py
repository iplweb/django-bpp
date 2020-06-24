from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils.timezone import localtime


@pytest.mark.django_db
def test_rest_api_praca_habilitacyjna_detail(client, praca_habilitacyjna):
    res = client.get(
        reverse("api_v1:praca_habilitacyjna-detail", args=(praca_habilitacyjna.pk,))
    )
    assert res.status_code == 200


@pytest.mark.django_db
def test_rest_api_praca_habilitacyjna_list(client, praca_habilitacyjna):
    res = client.get(reverse("api_v1:praca_habilitacyjna-list"))
    assert res.status_code == 200


@pytest.mark.django_db
def test_rest_api_praca_habilitacyjna_filtering_1(api_client, praca_habilitacyjna):
    czas = localtime(praca_habilitacyjna.ostatnio_zmieniony).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    res = api_client.get(
        reverse("api_v1:praca_habilitacyjna-list") + f"?ostatnio_zmieniony_after={czas}"
    )
    assert res.json()["count"] == 1


@pytest.mark.django_db
def test_rest_api_praca_habilitacyjna_filtering_2(api_client, praca_habilitacyjna):
    czas = localtime(
        praca_habilitacyjna.ostatnio_zmieniony + timedelta(seconds=1)
    ).strftime("%Y-%m-%d %H:%M:%S")

    res = api_client.get(
        reverse("api_v1:praca_habilitacyjna-list") + f"?ostatnio_zmieniony_after={czas}"
    )
    assert res.json()["count"] == 0


@pytest.mark.django_db
def test_rest_api_praca_habilitacyjna_filtering_rok(
    api_client, praca_habilitacyjna, rok
):
    res = api_client.get(
        reverse("api_v1:praca_habilitacyjna-list") + f"?rok_min={rok+1}"
    )
    assert res.json()["count"] == 0