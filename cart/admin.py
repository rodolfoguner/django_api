from django.contrib import admin
from .models import Cart

class Carts(admin.ModelAdmin):
    list_display = ('id', 'owner', 'total',)
    list_display_links = ('id', 'owner',)
    searche_fields = ('id', 'owner')
    list_per_page = 10

admin.site.register(Cart, Carts)
