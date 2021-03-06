# -*- encoding: utf-8 -*-
import multiprocessing

from django.conf import settings
from django.core.management import BaseCommand

from bpp.models import (
    Wydawnictwo_Ciagle,
    Wydawnictwo_Zwarte,
    Patent,
    rebuild_ciagle,
    rebuild_zwarte,
    rebuild_patent,
    rebuild_praca_doktorska,
    rebuild_praca_habilitacyjna,
    Praca_Habilitacyjna,
    Praca_Doktorska,
)
from bpp.util import (
    no_threads,
    partition_count,
    disable_multithreading_by_monkeypatching_pool,
)


def subprocess_setup(*args):
    from django.db import connection

    connection.connect()


class Command(BaseCommand):
    help = "Odbudowuje cache"

    def add_arguments(self, parser):
        parser.add_argument("--disable-multithreading", action="store_true")

    def handle(self, disable_multithreading, *args, **options):

        if not settings.TESTING:
            from django import db

            db.connections.close_all()

        pool_size = no_threads(0.75)
        pool = multiprocessing.Pool(processes=pool_size, initializer=subprocess_setup)
        if disable_multithreading:
            disable_multithreading_by_monkeypatching_pool(pool)

        pc = pool.apply(partition_count, args=(Praca_Habilitacyjna.objects, pool_size))
        pool.starmap(rebuild_praca_habilitacyjna, pc)

        pc = pool.apply(partition_count, args=(Praca_Doktorska.objects, pool_size))
        pool.starmap(rebuild_praca_doktorska, pc)

        pc = pool.apply(partition_count, args=(Wydawnictwo_Ciagle.objects, pool_size))
        pool.starmap(rebuild_ciagle, pc)

        pc = pool.apply(partition_count, args=(Wydawnictwo_Zwarte.objects, pool_size))
        pool.starmap(rebuild_zwarte, pc)

        pc = pool.apply(partition_count, args=(Patent.objects, pool_size))
        pool.starmap(rebuild_patent, pc)
