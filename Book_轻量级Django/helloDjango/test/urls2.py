from django.conf.urls import url
from helloDjango.hello import index

urlpatterns = (
    url('^$', index)
)
