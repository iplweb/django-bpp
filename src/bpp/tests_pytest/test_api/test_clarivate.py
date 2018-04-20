from django.urls import reverse
from mock import Mock


def test_Uczelnia_wosclient(uczelnia):
    res = uczelnia.wosclient()
    assert res is not None


def test_GetWoSAMRInformation_post_no_args(wd_app, uczelnia):
    res = wd_app.post(reverse("bpp:api_wos_amr", args=(uczelnia.slug,)))
    assert res.json['status'] == 'error'


def test_GetWoSAMRInformation_post_good(wd_app, uczelnia, mocker):
    m = Mock()
    m.query_single = Mock(return_value={'timesCited': '-1'})
    fn = mocker.patch("bpp.models.struktura.Uczelnia.wosclient", return_value=m)

    res = wd_app.post(
        reverse("bpp:api_wos_amr", args=(uczelnia.slug,)),
        params={'pmid': '31337'}
    )

    assert res.json['status'] == 'ok'
    assert res.json['timesCited'] == '-1'


def test_GetWoSAMRInformation_post_error(wd_app, mocker):
    m = Mock()
    m.query_single = Mock(side_effect=Exception("lel"))
    fn = mocker.patch("bpp.models.struktura.Uczelnia.wosclient", return_value=m)

    res = wd_app.post(
        reverse("bpp:api_wos_amr", args=(uczelnia.slug,)),
        params={'pmid': '31337'}
    )

    assert res.json['status'] == 'error'
    assert res.json['info'].find("lel") >= 0
