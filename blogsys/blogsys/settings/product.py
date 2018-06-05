from .base_setting import * # noqa

#import cache_toolbar.panels.redis


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8'}
    },
}
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',
        'TIMEOUT': 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        }
    }
}
DEBUG = True

#INSTALLED_APPS += [ # noqa
#    'debug_toolbar',
#    'cache_toolbar',
#]
#MIDDLEWARE += [ # noqa
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#    'silk.middleware.SilkyMiddleware',
#]
#INTERNAL_IPS = ['117.136.88.36']
#DEBUG_TOOLBAR_PANELSOOLBAR_PANELS = (
#)
