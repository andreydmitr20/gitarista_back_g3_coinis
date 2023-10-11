"""
URL configuration for song app
"""
from django.urls import path, include
from .views import (AuthorsView,
                    GenresView,
                    AccordsView,
                    SongGenresView,
                    SongLikesView,
                    SongsView,
                    ScrapeView,
                    )

urlpatterns = [

    path('genres/<int:genre_id>/', GenresView.as_view(), name='genres'),
    path('scrape/', ScrapeView.as_view(), name='scrape'),

    path('authors/<int:author_id>/', AuthorsView.as_view(), name='authors'),

    path('accords/<int:accord_id>/', AccordsView.as_view(), name='accords'),

    path('<int:song_id>/genres/<int:genre_id>/',
         SongGenresView.as_view(), name='song genres'),

    path('<int:song_id>/likes/<int:user_id>/',
         SongLikesView.as_view(), name='song likes'),

    path('<int:song_id>/', SongsView.as_view(), name='songs'),
]
