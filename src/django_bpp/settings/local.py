# -*- encoding: utf-8 -*-

# Lokalny development (na moim Maku)

import os

def setenv_default(varname, default_value):
    if os.environ.get(varname) is None:
        os.environ[varname] = default_value

setenv_default("DJANGO_SETTINGS_MODULE", "django_bpp.settings.local")
setenv_default("DJANGO_BPP_SECRET_KEY", "0xdeadbeef 2")

from .base import *

DEBUG = True

SENDFILE_BACKEND = 'sendfile.backends.simple'

SELENIUM_DRIVER = "Firefox"

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

MEDIA_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'media')
)
SENDFILE_ROOT = MEDIA_ROOT

COMPRESS_ENABLED = False # not DEBUG
COMPRESS_OFFLINE = False

# host dla HTMLu oraz linii polecen, reszta dla linii polecen (bo HTML sie autokonfiguruje...)
NOTIFICATIONS_HOST = 'mac'
NOTIFICATIONS_PORT = 9090
NOTIFICATIONS_PROTOCOL = 'http'

HTML_MINIFY = False

CELERY_ALWAYS_EAGER = False # True # False
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

EMAIL_PORT = 2525

PUNKTUJ_MONOGRAFIE = False

DEBUG_TOOLBAR = False

if DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'bpp.middleware.NonHtmlDebugToolbarMiddleware'
    ]

    INSTALLED_APPS.append('debug_toolbar')

DATABASES['default']['CONN_MAX_AGE'] = 10
