"""
URL configuration for song app
"""
from django.urls import path, include
from .views import (AuthorView,
                    GenreView,
                    AccordView,
                    SongGenreView,
                    SongLikeView,
                    SongView,
                    )

urlpatterns = [

    path('genre/<int:genre_id>/', GenreView.as_view(), name='genres'),

    path('author/<int:author_id>/', AuthorView.as_view(), name='authors'),

    path('accord/<int:accord_id>/', AccordView.as_view(), name='accords'),

    path('<int:song_id>/genre/', SongGenreView.as_view(), name='song genres'),

    path('<int:song_id>/like/', SongLikeView.as_view(), name='song likes'),

    path('<int:song_id>/', SongView.as_view(), name='songs'),
]
