""" song admin """
from django.contrib import admin

from .models import (Genres,
                     Accords,
                     Authors,
                     SongGenres,
                     SongLikes,
                     Songs)


class GenresAdmin(admin.ModelAdmin):
    """ genres admin"""
    list_display = ['name', 'description']
    # list_filter = ['name',]
    search_fields = ['name', 'description']


admin.site.register(Genres, GenresAdmin)


class AuthorsAdmin(admin.ModelAdmin):
    """ authors admin"""
    list_display = ['name', 'link']
    # list_filter = ['name',]
    search_fields = ['name', 'link']


admin.site.register(Authors, AuthorsAdmin)


class AccordsAdmin(admin.ModelAdmin):
    """ accords admin"""
    list_display = ['name', 'short_name', 'link']
    # list_filter = ['name',]
    search_fields = ['name', 'short_name', 'link']


admin.site.register(Accords, AccordsAdmin)


class SongGenresAdmin(admin.ModelAdmin):
    """ song genres admin"""
    list_display = ['get_song_title', 'get_song_genre']
    list_filter = ['song_id', 'genre_id']
    search_fields = ['get_song_title', 'get_song__genre']


admin.site.register(SongGenres, SongGenresAdmin)


class SongLikesAdmin(admin.ModelAdmin):
    """ song likes admin"""
    list_display = ['get_song_title'
                    # , 'get_user_email'
                    ]
    list_filter = ['song_id', 'user_id']
    search_fields = ['get_song_title'
                     #  , 'get_user_email'
                     ]


admin.site.register(SongLikes, SongLikesAdmin)


class SongsAdmin(admin.ModelAdmin):
    """ songs admin"""
    list_display = ['get_author',
                    'title',
                    # 'get_user_email',
                    'text_with_accords',
                    'link',
                    'date_creation']
    list_filter = ['author_id',
                   'user_id',
                   'date_creation']
    search_fields = ['get_author',
                     'title',
                     #  'get_user_email',
                     'text_with_accords',
                     'link',
                     'date_creation']


admin.site.register(Songs, SongsAdmin)
