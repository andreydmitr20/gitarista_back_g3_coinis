from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from utils.views_functions import select_simple, insert_simple, update_simple, delete_simple
from .models import Song, Accord, Author, SongGenre, SongLike, Genre
from .serializers import (SongSerializer,
                          AuthorSerializer, AuthorShortSerializer,
                          GenreSerializer, GenreShortSerializer,
                          SongLikeSerializer,
                          SongGenreSerializer,
                          AccordSerializer)


PERMISSION_CLASSES = [AllowAny]
# PERMISSION_CLASSES=[IsAuthenticated]


class GenreView(APIView):
    """ GenreView """
    permission_classes = PERMISSION_CLASSES
    serializer_class = GenreSerializer
    model = Genre

    def get(self, request, id=None, format=None):
        return select_simple(
            self.model,
            request,
            id,
            self.serializer_class,
            short_serializer_class=GenreShortSerializer,
            search_field='name',
            order_by='name')

    def post(self, request, format=None):
        return insert_simple(request, self.serializer_class)

    def put(self, request, id=None, format=None):
        return update_simple(self.model, request, id, self.serializer_class)

    def delete(self, request, id=None, format=None):
        return delete_simple(self.model, id)


class AuthorView(APIView):
    """ AuthorView """
    permission_classes = PERMISSION_CLASSES
    serializer_class = AuthorSerializer
    model = Author

    def get(self, request, id=None, format=None):
        return select_simple(
            self.model,
            request,
            id,
            self.serializer_class,
            short_serializer_class=AuthorShortSerializer,
            search_field='name',
            order_by='name')

    def post(self, request, format=None):
        return insert_simple(request, self.serializer_class)

    def put(self, request, id=None, format=None):
        return update_simple(self.model, request, id, self.serializer_class)

    def delete(self, request, id=None, format=None):
        return delete_simple(self.model, id)


class AccordView(APIView):
    permission_classes = PERMISSION_CLASSES
    serializer_class = AccordSerializer
    model = Accord

    def get(self, request, id=None, format=None):
        return select_simple(
            self.model,
            request,
            id,
            self.serializer_class,
            short_serializer_class=AccordShortSerializer,
            search_field='name',
            order_by='name')

    def post(self, request, format=None):
        return insert_simple(request, self.serializer_class)

    def put(self, request, id=None, format=None):
        return update_simple(self.model, request, id, self.serializer_class)

    def delete(self, request, id=None, format=None):
        return delete_simple(self.model, id)
