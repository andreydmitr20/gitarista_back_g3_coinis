""" user admin """
from django.contrib import admin

from .models import Users


class UserAdmin(admin.ModelAdmin):

    list_display = ['user_id','username','email', 'is_staff','password', 'date_creation']
    # list_filter = ['name',]
    search_fields = ['username']


admin.site.register(Users, UserAdmin)
