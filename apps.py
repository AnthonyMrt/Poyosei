from django.apps import AppConfig
from django.conf.urls import url
from django.contrib import admin


class PoyoseiConfig(AppConfig):
    name = 'poyosei'

admin.site.site = '/poyosei'