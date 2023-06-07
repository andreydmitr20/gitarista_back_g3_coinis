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

    path('genre/<int:id>/', GenreView.as_view(), name='genres'),

    path('author/<int:id>/', AuthorView.as_view(), name='authors'),

    path('accord/<int:id>/', AccordView.as_view(), name='accords'),

    path('<int:song_id>/', SongView.as_view(), name='songs'),

    path('<int:song_id>/genre/', SongGenreView.as_view(), name='song genres'),

    path('<int:song_id>/like/', SongLikeView.as_view(), name='song likes'),

]
