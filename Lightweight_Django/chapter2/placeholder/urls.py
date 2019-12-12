from django.conf.urls import url
from django.conf import urls
from placeholder import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('image/<int:width>x<int:height>/', views.placeholder, name='placeholder')
]
