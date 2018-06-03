from .base_setting import * # noqa


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    },
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}
DEBUG = False

#INSTALLED_APPS += [ # noqa
#    'debug_toolbar',
#]
#MIDDLEWARE += [ # noqa
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#    'silk.middleware.SilkyMiddleware',
#]
#INTERNAL_IPS = ['*.*.*.*']
