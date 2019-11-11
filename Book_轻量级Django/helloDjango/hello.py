# -*- coding:utf-8 -*-
import sys
from django.conf import settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='thissithrer',
    ROOT_URLCONF='test.urls2',
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.http import HttpResponse
from django.conf.urls import url


def index(request):
    return HttpResponse('Hello Django')


urlpatterns = (
    url('^$', index)
)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

