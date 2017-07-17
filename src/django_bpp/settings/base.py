# -*- encoding: utf-8 -*-

import os
import sys
import django
from datetime import timedelta

from django.core.exceptions import ImproperlyConfigured


def django_getenv(varname, default=None):
    value = os.getenv(varname, default)
    if value is None:
        raise ImproperlyConfigured("Please set %r variable" % varname)
    return value


# pycharm, leave this
os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Django
import random, string

TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'
LANGUAGES = (
    ('pl', 'Polish'),
)

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'bpp.finders.YarnFinder',
    'compressor.finders.CompressorFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=6uqi1)(qnzjo8q@-@m#egd8v#+zac6feh2h-b&amp;=3bczpfqxxd'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'loaders': [
                "admin_tools.template_loaders.Loader",
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'password_policies.context_processors.password_status',

                'bpp.context_processors.uczelnia.uczelnia',
                'bpp.context_processors.global_nav.user',
                'bpp.context_processors.google_analytics.google_analytics',

                'notifications.context_processors.notification_settings'

            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'password_policies.middleware.PasswordChangeMiddleware',

    'dj_pagination.middleware.PaginationMiddleware',

    'django_tables2_reports.middleware.TableReportMiddleware',

    'session_security.middleware.SessionSecurityMiddleware',
    'notifications.middleware.NotificationsMiddleware',
    'dogslow.WatchdogMiddleware',
)

DOGSLOW_LOGGER = 'dogslow'  # can be anything, but must match `logger` below
DOGSLOW_LOG_TO_SENTRY = True
DOGSLOW_LOG_LEVEL = 'WARNING'  # optional, defaults to 'WARNING'

INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'django_bpp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django_bpp.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'password_policies',

    'create_test_db',

    # 'debug_toolbar',

    'celery',

    'cookielaw',

    'dal',
    'dal_select2',

    'grappelli',
    'django.contrib.admin',

    'dj_pagination',

    'bpp',

    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django_tables2',
    'django_tables2_reports',

    # 'autocomplete_light',

    'messages_extends',

    'multiseek',
    'django_extensions',
    'celeryui',

    'crispy_forms',
    'crispy_forms_foundation',

    'compressor',

    'secure_input',
    'session_security',

    'notifications',
    'integrator2',

    'egeria',
    'eksport_pbn',

    'loginas',

    'robots',
    'webmaster_verification',
    'favicon',

]

if django.VERSION < (1,9):
    INSTALLED_APPS += ['django_18_fast_migrations',]

# Profile użytkowników
AUTH_USER_MODEL = "bpp.BppUser"

GRAPPELLI_INDEX_DASHBOARD = 'django_bpp.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = "BPP"
ADMIN_TOOLS_MENU = 'django_bpp.menu.CustomMenu'

PROJECT_ROOT = BASE_DIR

MULTISEEK_REGISTRY = 'bpp.multiseek_registry'

from bpp.util import slugify_function

AUTOSLUG_SLUGIFY_FUNCTION = slugify_function

LOGIN_REDIRECT_URL = '/'

# django
MEDIA_URL = '/media/'

INTERNAL_IPS = ('127.0.0.1',)

# djorm-pool
DJORM_POOL_OPTIONS = {
    "pool_size": 30,
    "max_overflow": 0,
    "recycle": 3600,  # the default value
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'dogslow': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'dogslow': {
            'level': 'WARNING',
            'handlers': ['dogslow'],  # or whatever you named your handler
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'celery.worker.job': {
            'level': 'ERROR',
            'handlers': ['sentry', 'console'],
            'propagate': False
        },
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

EXCEL_SUPPORT = 'openpyxl'

TOPLEVEL = 'common'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

PROJECT_APPS = (
    'bpp',
)


# Ustawienia ModelMommy

def autoslug_gen():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))


MOMMY_CUSTOM_FIELDS_GEN = {
    'autoslug.fields.AutoSlugField': autoslug_gen
}

CRISPY_ALLOWED_TEMPLATE_PACKS = ('foundation-5',)
CRISPY_TEMPLATE_PACK = 'foundation-5'

SESSION_ENGINE = 'redis_sessions.session'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

MAT_VIEW_REFRESH_COUNTDOWN = 30

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

SITE_ROOT = os.path.abspath(
    os.path.join(SCRIPT_PATH, '..', '..'))

STATIC_ROOT = os.path.join(SCRIPT_PATH, "..", "staticroot")


COMPRESS_ROOT = STATIC_ROOT

# Domyslnie, redis na Ubuntu pozwala na 16 baz danych
REDIS_DB_BROKER = 1
REDIS_DB_CELERY = 2
REDIS_DB_SESSION = 4
REDIS_DB_LOCKS = 6

from django_bpp.version import VERSION

if os.getenv("DJANGO_BPP_RAVEN_CONFIG_URL", None):
    RAVEN_CONFIG = {
        'dsn': django_getenv("DJANGO_BPP_RAVEN_CONFIG_URL"),
        'release': VERSION
    }

    INSTALLED_APPS.append('raven.contrib.django.raven_compat')

ALLOWED_HOSTS = [
    "127.0.0.1",
    django_getenv("DJANGO_BPP_HOSTNAME", "localhost"),
]

REDIS_HOST = django_getenv("DJANGO_BPP_REDIS_HOST", "localhost")
REDIS_PORT = int(django_getenv("DJANGO_BPP_REDIS_PORT", "6379"))

CELERY_HOST = django_getenv("DJANGO_BPP_CELERY_HOST", "localhost")
CELERY_PORT = int(django_getenv("DJANGO_BPP_CELERY_PORT", "5672"))
CELERY_USER = django_getenv("DJANGO_BPP_CELERY_USER", "guest")
CELERY_PASSWORD = django_getenv("DJANGO_BPP_CELERY_PASSWORD", "guest")
CELERY_VHOST = django_getenv("DJANGO_BPP_CELERY_VHOST", "/")

BROKER_URL = django_getenv("DJANGO_BPP_BROKER_URL",
                           "amqp://%s:%s@%s:%s/%s" % (CELERY_USER,
                                                      CELERY_PASSWORD,
                                                      CELERY_HOST,
                                                      CELERY_PORT,
                                                      CELERY_VHOST))
# BYłO: redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, REDIS_DB_BROKER)
# CELERY_RESULT_BACKEND = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, REDIS_DB_CELERY)

#
SESSION_REDIS_HOST = REDIS_HOST
SESSION_REDIS_PORT = REDIS_PORT
SESSION_REDIS_DB = REDIS_DB_SESSION
SESSION_REDIS_PREFIX = 'session'

ALLOWED_TAGS = ('b', 'em', 'i', 'strong', 'strike', 'u', 'sup', 'font', 'sub')

SESSION_SECURITY_PASSIVE_URLS = [
    '/messages/'
]

ADMINS = (
    ("Michal Pasternak", "michal.dtz@gmail.com"),
)
MANAGERS = ADMINS


def int_or_None(value):
    try:
        return int(value)
    except ValueError:
        return ""


DATABASES = {
    'default': {
        'ENGINE': django_getenv("DJANGO_BPP_DB_ENGINE", 'django.db.backends.postgresql_psycopg2'),
        'NAME': django_getenv("DJANGO_BPP_DB_NAME", "bpp"),
        'USER': django_getenv("DJANGO_BPP_DB_USER", "postgres"),
        'PASSWORD': django_getenv("DJANGO_BPP_DB_PASSWORD", "password"),
        'HOST': django_getenv("DJANGO_BPP_DB_HOST", "localhost"),
        'PORT': int_or_None(django_getenv("DJANGO_BPP_DB_PORT", "5432")),
    },
    # 'test': {
    #     'ENGINE': django_getenv("DJANGO_BPP_DB_ENGINE", 'django.db.backends.postgresql_psycopg2'),
    #     'NAME': "test_" + django_getenv("DJANGO_BPP_DB_NAME", "bpp"),
    #     'USER': django_getenv("DJANGO_BPP_DB_USER", "bpp"),
    #     'PASSWORD': django_getenv("DJANGO_BPP_DB_PASSWORD", "password"),
    #     'HOST': django_getenv("DJANGO_BPP_DB_HOST", "bpp-db"),
    #     'PORT': int_or_None(django_getenv("DJANGO_BPP_DB_PORT", "5432")),
    # },
}

SECRET_KEY = django_getenv("DJANGO_BPP_SECRET_KEY")

SENDFILE_URL = MEDIA_URL

# django-password-policies
# Zmiana hasla co 30 dni
PASSWORD_DURATION_SECONDS = (60 * 60 * 24) * 30
PASSWORD_USE_HISTORY = True
PASSWORD_HISTORY_COUNT = 12
# wymagane przez django-password-policies
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

MESSAGE_STORAGE = 'messages_extends.storages.FallbackStorage'

NOTIFICATIONS_PUB_PREFIX = 'django_bpp'

TEST_NON_SERIALIZED_APPS = ['django.contrib.contenttypes',
                            'django.contrib.auth']

TESTING = ('test' in sys.argv) or ('jenkins' in sys.argv) or \
          ('py.test' in sys.argv) or ('pytest' in sys.argv)

if TESTING:
    CELERY_ALWAYS_EAGER = True
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

CELERYD_HIJACK_ROOT_LOGGER = False

CELERYBEAT_SCHEDULE = {

    'cleanup-integrator2-files': {
        'task': 'integrator2.tasks.remove_old_integrator_files',
        'schedule': timedelta(days=1),
    },

    'cleanup-eksport_pbn-files': {
        'task': 'eksport_pbn.tasks.remove_old_eksport_pbn_files',
        'schedule': timedelta(days=1),
    },

    'cleanup-report-files': {
        'task': 'bpp.tasks.remove_old_report_files',
        'schedule': timedelta(days=1),
    }
}

CAN_LOGIN_AS = lambda request, target_user: request.user.username in ['admin', 'sysdba']

#

# host dla HTMLu oraz linii polecen, reszta dla linii polecen (bo HTML sie autokonfiguruje...)
NOTIFICATIONS_HOST = django_getenv("DJANGO_BPP_NOTIFICATIONS_HOST", '127.0.0.1')
NOTIFICATIONS_PORT = django_getenv("DJANGO_BPP_NOTIFICATIONS_PORT", 80)
NOTIFICATIONS_PROTOCOL = django_getenv("DJANGO_BPP_NOTIFICATIONS_PROTOCOL", 'http')

MEDIA_ROOT = django_getenv(
    "DJANGO_BPP_MEDIA_ROOT",
    os.getenv("HOME", "C:/django-bpp-media")
)

SENDFILE_ROOT = MEDIA_ROOT

GOOGLE_ANALYTICS_PROPERTY_ID = django_getenv("DJANGO_BPP_GOOGLE_ANALYTICS_PROPERTY_ID", "")

ROBOTS_SITEMAP_VIEW_NAME = 'sitemap'

WEBMASTER_VERIFICATION = {
    'google': django_getenv("DJANGO_BPP_GOOGLE_VERIFICATION_CODE", "1111111111111111"),
}

EXCLUDE_FROM_MINIFYING = [
    "^google.*html$"
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True