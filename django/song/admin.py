""" song admin """
from django.contrib import admin

from .models import Genre


class GenreAdmin(admin.ModelAdmin):
    """ genre admin"""
    list_display = ['name', 'description']
    # list_filter = ['name',]
    search_fields = ['name', 'description']


admin.site.register(Genre, GenreAdmin)
