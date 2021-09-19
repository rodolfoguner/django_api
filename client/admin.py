from re import I
from django.contrib import admin
from django.urls.resolvers import CheckURLMixin
from .models import Client


admin.site.register(Client)
