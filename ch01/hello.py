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

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
)

application = get_wsgi_application()

print(application)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

    # python hello.py runserver
