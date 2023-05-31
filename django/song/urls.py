"""
URL configuration for song app
"""
from django.urls import path, include
from .views import (AuthorView, AuthorDetailView,
                    GenreView, GenreDetailView,
                    AccordView, AccordDetailView)

urlpatterns = [

    path('genre/', GenreView.as_view(), name='song genres'),
    path('genre/<int:pk>', GenreDetailView.as_view(), name='genre'),

    path('author/', AuthorView.as_view(), name='song authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='song authors'),

    path('accord/', AccordView.as_view(), name='accords'),
    path('accord/<int:pk>', AccordDetailView.as_view(), name='accords'),
]
