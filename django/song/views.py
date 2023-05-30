from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render


from rest_framework import mixins
from rest_framework import generics


from .models import Song, Accord, Author, SongGenre, SongLike, Genre
from .serializers import (SongSerializer,
                          AuthorSerializer,
                          GenreSerializer,
                          SongLikeSerializer,
                          SongGenreSerializer,
                          AccordSerializer)

PERMISSION_CLASSES = [AllowAny]
# PERMISSION_CLASSES=[IsAuthenticated]

# genre


class GenreView(
    generics.ListCreateAPIView,
):
    permission_classes = PERMISSION_CLASSES
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreDetailView(
    generics.RetrieveUpdateAPIView,
):
    permission_classes = PERMISSION_CLASSES
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


# author


class AuthorView(
    generics.ListCreateAPIView,
):
    permission_classes = PERMISSION_CLASSES
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDetailView(
    generics.RetrieveUpdateAPIView,
):
    permission_classes = PERMISSION_CLASSES
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


# accord


class AccordView(
    generics.ListCreateAPIView,
):
    permission_classes = PERMISSION_CLASSES
    serializer_class = AccordSerializer
    queryset = Accord.objects.all()


class AccordDetailView(
    generics.RetrieveUpdateAPIView,
):
    permission_classes = PERMISSION_CLASSES
    serializer_class = AccordSerializer
    queryset = Accord.objects.all()
