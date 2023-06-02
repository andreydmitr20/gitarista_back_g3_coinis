"""
URL configuration for song app
"""
from django.urls import path, include
from .views import (AuthorView,
                    GenreView,
                    AccordView,
                    )

urlpatterns = [

    path('genre/', GenreView.as_view(), name='song genres'),
    path('genre/<int:id>/', GenreView.as_view(), name='song genres'),

    path('author/', AuthorView.as_view(), name='song authors'),
    path('author/<int:id>/', AuthorView.as_view(), name='song authors'),

    path('accord/', AccordView.as_view(), name='accords'),
    path('accord/<int:id>/', AccordView.as_view(), name='accords'),
]
