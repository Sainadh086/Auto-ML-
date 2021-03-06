"""
WSGI config for excel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise


#from django.contrib.staticfiles.handlers import StaticFilesHandler
#application = StaticFilesHandler(get_wsgi_application())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "excel.settings")

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
#application = StaticFilesHandler(get_wsgi_application())
