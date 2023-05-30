"""
URL configuration for song app
"""
from django.urls import path, include
from .views import AuthorView, GenreView, AccordView

urlpatterns = [

    path('author/', AuthorView.as_view(), name='song authors'),
    path('genre/', GenreView.as_view(), name='song genres'),
    path('accord/', AccordView.as_view(), name='accords'),
]
