from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^webhook/$', views.fbwebhook),
    url(r'^download_url/$', views.download_url),
]
