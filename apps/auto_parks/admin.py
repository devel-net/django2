from django.contrib import admin
from .models import AutoParkModel


@admin.register(AutoParkModel)
class AutoParkAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 25
