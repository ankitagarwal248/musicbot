from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^webhook/$', views.fbwebhook),
    url(r'^download_url/$', views.download_url),
    url(r'^googleoauth2callback/$', views.googleoauth2callback),
    url(r'^google_auth_success/$', views.google_auth_success),
]
