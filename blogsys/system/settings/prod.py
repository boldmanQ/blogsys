from .base_setting import * # noqa

#import cache_toolbar.panels.redis


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'blog',
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
DEBUG = False

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

STATIC_URL = '/static/'
STATIC_ROOT = 'static_files'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, THEME_TEMPLATE_DIR, 'static')
]
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': 'codesnippet,uploadimage,prism,widget,lineutils',
        'height': 300,
        'width': 1000,
        'tabSpaces': 4,
    },
}
MEDIA_URL = "/media/"
MEDIA_ROOT = "/data/www/blogsys/media"
CKEDITOR_UPLOAD_PATH = "images"
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 24
}
