

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
                                   get_int_request_param,
                                   API_TEXT_SEARCH,
                                   API_TEXT_SHORT)

from django.db.models import Q

from .models import Song, Accord, Author, SongGenre, SongLike, Genre
from .serializers import (SongSerializer, SongShortSerializer, SongListSerializer,
                          AuthorSerializer, AuthorShortSerializer,
                          GenreSerializer, GenreShortSerializer,
                          SongLikeSerializer, SongLikeListSerializer,
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
        return insert_simple(self.serializer_class, request.data)

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
        return insert_simple(self.serializer_class, request.data)

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
        return insert_simple(self.serializer_class, request.data)

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
        return insert_simple(self.serializer_class, {
            'song': song_id,
            'genre': get_int_request_param(request, 'genre')
        })

    def delete(self, request, song_id=None, format=None):
        return delete_simple(self.model, Q(song_id=song_id,
                                           genre_id=request.data['genre']))


class SongLikeView(APIView):
    permission_classes = PERMISSION_CLASSES
    serializer_class = SongLikeSerializer
    model = SongLike

    def get(self, request, song_id=None, format=None):
        serializer = SongLikeListSerializer
        fields = serializer.Meta.fields
        queryset = self.model.objects.select_related('user').values(*fields)

        if not song_id is None:
            queryset = queryset.filter(song_id=song_id)

        if not request.query_params.get(API_TEXT_SEARCH) is None:
            queryset = search_simple(
                queryset,
                request.query_params.get(API_TEXT_SEARCH),
                'user__username',
            )

        queryset = order_simple(queryset, 'user__username')
        print_query(PRINT_QUERY, queryset)

        return pagination_simple(request, serializer, queryset)

    def post(self, request, song_id=None, format=None):
        return insert_simple(self.serializer_class, {
            'song': song_id,
            'user': get_int_request_param(request, 'user')
        })

    def delete(self, request, song_id=None, format=None):
        return delete_simple(self.model, Q(song_id=song_id,
                                           user_id=request.data['user']))


class SongView(APIView):
    """SongView"""
    permission_classes = PERMISSION_CLASSES
    serializer_class = SongSerializer
    model = Song

    def get(self, request, song_id=None, format=None):
        serializer_class_local = (
            SongShortSerializer
            if request.query_params.get(API_TEXT_SHORT, '0') == '1'
            else SongListSerializer
        )

        fields = serializer_class_local.Meta.fields
        # print('fields', fields)
        # print(serializer_class_local)
        queryset = self.model.objects.select_related(
            'user').select_related('author').values(*fields)

        author = self.request.query_params.get('author', '')
        print('author', author)
        if author != '':
            queryset = queryset.filter(author=author)

        user = self.request.query_params.get('user', '')
        print('user', user)
        if user != '':
            queryset = queryset.filter(user=user)

        if not request.query_params.get(API_TEXT_SEARCH) is None:
            queryset = search_simple(
                queryset,
                request.query_params.get(API_TEXT_SEARCH),
                "title")

        queryset = order_simple(queryset, 'title')

        if not song_id is None:
            queryset = queryset.filter(pk=song_id)

        print_query(PRINT_QUERY, queryset)

        return pagination_simple(request, serializer_class_local, queryset)

    def post(self, request, format=None):
        # print('request', request.POST)
        return insert_simple(self.serializer_class,
                             request.data.dict() | {
                                 'author': get_int_request_param(request, 'author'),
                                 'user': get_int_request_param(request, 'user')
                             })

    def put(self, request, song_id=None, format=None):
        return update_simple(self.model, request, song_id, self.serializer_class)

    def delete(self, request, song_id=None, format=None):
        return delete_simple(self.model, Q(pk=song_id))
