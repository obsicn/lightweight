import sys

from django.conf.urls import url
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
from django.core.wsgi import get_wsgi_application


def index(request):
    message = 'Hello world ' + datetime.now().isoformat()
    print(message)
    return HttpResponse(message)


urlpatterns = (
    url(r'^$', index),
)

import os

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

print(ALLOWED_HOSTS)
settings.configure(
    DEBUG = DEBUG,
    ROOT_URLCONF = __name__,
    ALLOWED_HOSTS = ALLOWED_HOSTS,
)

application = get_wsgi_application()

print(application)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

    # python hello.py runserver
