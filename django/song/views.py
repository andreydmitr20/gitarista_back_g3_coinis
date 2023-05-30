from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
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


class GenreView(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class AuthorView(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AccordView(
    generics.ListCreateAPIView,
    generics.RetrieveUpdateAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = AccordSerializer
    queryset = Accord.objects.all()
