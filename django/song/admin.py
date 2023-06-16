""" song admin """
from django.contrib import admin

from .models import Genre, Accord, Author, SongGenre, SongLike, Song


class GenreAdmin(admin.ModelAdmin):
    """ genre admin"""
    list_display = ['name', 'description']
    # list_filter = ['name',]
    search_fields = ['name', 'description']


admin.site.register(Genre, GenreAdmin)


class AuthorAdmin(admin.ModelAdmin):
    """ author admin"""
    list_display = ['name', 'link']
    # list_filter = ['name',]
    search_fields = ['name', 'link']


admin.site.register(Author, AuthorAdmin)


class AccordAdmin(admin.ModelAdmin):
    """ accord admin"""
    list_display = ['name', 'short_name', 'link']
    # list_filter = ['name',]
    search_fields = ['name', 'short_name', 'link']


admin.site.register(Accord, AccordAdmin)


class SongGenreAdmin(admin.ModelAdmin):
    """ song genre admin"""
    list_display = ['get_song_title', 'get_song_genre']
    list_filter = ['song_id', 'genre_id']
    search_fields = ['get_song_title', 'get_song__genre']


admin.site.register(SongGenre, SongGenreAdmin)


class SongLikeAdmin(admin.ModelAdmin):
    """ song like admin"""
    list_display = ['get_song_title'
                    # , 'get_user_email'
                    ]
    list_filter = ['song_id', 'user_id']
    search_fields = ['get_song_title'
                     #  , 'get_user_email'
                     ]


admin.site.register(SongLike, SongLikeAdmin)


class SongAdmin(admin.ModelAdmin):
    """ genre admin"""
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


admin.site.register(Song, SongAdmin)
