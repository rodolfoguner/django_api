from django.contrib import admin
from django.urls.resolvers import CheckURLMixin
from .models import Client


class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'cpf',)
    list_per_page = 10


admin.site.register(Client, Clients)
