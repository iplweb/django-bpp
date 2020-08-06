from django.core.files.base import ContentFile
from django.db import transaction

import notifications
from conftest import NORMAL_DJANGO_USER_LOGIN
from import_dyscyplin.models import Import_Dyscyplin
from import_dyscyplin.tasks import przeanalizuj_import_dyscyplin


def test_przeanalizuj_import_dyscyplin(
    test1_xlsx, normal_django_user, mocker, transactional_db
):

    web_page_uid = "foobar_uid"

    with transaction.atomic():
        i = Import_Dyscyplin.objects.create(
            owner=normal_django_user, web_page_uid=web_page_uid
        )
        i.plik.save("test1.xls", ContentFile(open(test1_xlsx, "rb").read()))
        path = i.plik.path

    mocker.patch("notifications.send_redirect")

    przeanalizuj_import_dyscyplin.delay(i.pk)

    link = "/import_dyscyplin/detail/%s/?notification=1" % i.pk

    notifications.send_redirect.assert_called_once_with(
        NORMAL_DJANGO_USER_LOGIN, link, web_page_uid
    )
