import os
from .base_setting import * # noqa


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # noqa
    }
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
DEBUG = True

#INSTALLED_APPS += [ # noqa
#    'debug_toolbar',
#]
#MIDDLEWARE += [ # noqa
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#    'silk.middleware.SilkyMiddleware',
#]
#INTERNAL_IPS = ['*.*.*.*']

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
MEDIA_ROOT = os.path.join(BASE_DIR, "upload/media")
CKEDITOR_UPLOAD_PATH = "images"
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 24
}
