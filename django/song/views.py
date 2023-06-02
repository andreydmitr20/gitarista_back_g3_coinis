

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from utils.views_functions import (select_simple,
                                   insert_simple,
                                   update_simple,
                                   delete_simple,
                                   print_query,
                                   pagination_simple,
                                   search_simple,
                                   order_simple,
                                   API_TEXT_SEARCH)

from django.db.models import Q

from .models import Song, Accord, Author, SongGenre, SongLike, Genre
from .serializers import (SongSerializer,
                          AuthorSerializer, AuthorShortSerializer,
                          GenreSerializer, GenreShortSerializer,
                          SongLikeSerializer,
                          SongGenreSerializer, SongGenreListSerializer,
                          AccordSerializer, AccordShortSerializer)


PERMISSION_CLASSES = [AllowAny]
# PERMISSION_CLASSES=[IsAuthenticated]

PRINT_QUERY = True


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
            order_field='name',
            is_print_query=PRINT_QUERY)

    def post(self, request, format=None):
        return insert_simple(request, self.serializer_class)

    def put(self, request, id=None, format=None):
        return update_simple(self.model, request, id, self.serializer_class)

    def delete(self, request, id=None, format=None):
        return delete_simple(self.model, Q(pk=id))


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
            order_field='name',
            is_print_query=PRINT_QUERY)

    def post(self, request, format=None):
        return insert_simple(request, self.serializer_class)

    def put(self, request, id=None, format=None):
        return update_simple(self.model, request, id, self.serializer_class)

    def delete(self, request, id=None, format=None):
        return delete_simple(self.model, Q(pk=id))


class AccordView(APIView):
    """AccordView"""
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
            order_field='name',
            is_print_query=PRINT_QUERY)

    def post(self, request, format=None):
        return insert_simple(request, self.serializer_class)

    def put(self, request, id=None, format=None):
        return update_simple(self.model, request, id, self.serializer_class)

    def delete(self, request, id=None, format=None):
        return delete_simple(self.model, Q(pk=id))


class SongGenreView(APIView):
    """SongGenreView"""
    permission_classes = PERMISSION_CLASSES
    serializer_class = SongGenreSerializer
    model = SongGenre

    def get(self, request, song_id=None, format=None):
        serializer = SongGenreListSerializer
        fields = serializer.Meta.fields
        queryset = self.model.objects.select_related('genre').values(*fields)

        if not song_id is None:
            queryset = queryset.filter(song_id=song_id)

        if not request.query_params.get(API_TEXT_SEARCH) is None:
            queryset = search_simple(
                queryset,
                request.query_params.get(API_TEXT_SEARCH),
                'genre__name',
            )

        queryset = order_simple(queryset, 'genre__name')
        print_query(PRINT_QUERY, queryset)

        return pagination_simple(request, serializer, queryset)

    def post(self, request, song_id=None, format=None):
        # print(request.data)
        data = request.POST.copy()
        data['song_id'] = str(song_id)
        # print(data)

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            print('valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, song_id=None, format=None):
        return delete_simple(self.model, Q(song_id=song_id, genre_id=request.data['genre_id']))


class SongLikeView(APIView):
    permission_classes = PERMISSION_CLASSES
    serializer_class = SongLikeSerializer
    model = SongLike
