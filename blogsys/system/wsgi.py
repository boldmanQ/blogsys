"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.setdefault('DJANGO_ENVIRON_FILE', 'prod')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings.%s" % profile)

application = get_wsgi_application()
