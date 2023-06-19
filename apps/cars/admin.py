from django.contrib import admin
from .models import CarModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'price', 'year', 'updated_at', 'auto_park']
    list_display_links = ['brand', 'price', 'year', 'updated_at', 'auto_park']
    search_fields = ['brand', 'price', 'year', 'updated_at', 'auto_park']
    list_filter = ['brand', 'price', 'year', 'updated_at', 'auto_park']
    list_per_page = 25
