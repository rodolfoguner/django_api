from django.contrib import admin
from .models import Product


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_display_links = ('id', 'name', 'price', 'category')
    search_fields = ('name', 'category',)
    list_per_page = 10

admin.site.register(Product, Products)
