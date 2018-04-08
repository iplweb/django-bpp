# -*- encoding: utf-8 -*-

from .base import *

DEBUG = False

SENDFILE_BACKEND = 'sendfile.backends.nginx'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

COMPRESS_ENABLED = not DEBUG
COMPRESS_OFFLINE = False

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders'])
]

HTML_MINIFY = True

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    # This is required for django-compressor 'compress --offline --force'
    # memcache bug
    'compressor': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'compressor'
    }
}

COMPRESS_CACHE_BACKEND = 'compressor'

CACHE_MIDDLEWARE_SECONDS = 3600 * 24

DATABASES['default']['CONN_MAX_AGE'] = None

NOTIFICATIONS_PORT = None