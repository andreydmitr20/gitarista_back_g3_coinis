""" user admin """
from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """ genre admin"""
    list_display = ['first_name','last_name','email', 'password', 'date_creation']
    # list_filter = ['name',]
    search_fields = ['username', 'public_info']


admin.site.register(User, UserAdmin)
