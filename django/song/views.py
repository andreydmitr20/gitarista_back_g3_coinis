from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import serializers, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from utils.views_functions import (API_TEXT_SEARCH, API_TEXT_SHORT,
                                   delete_simple, filter_params_simple,
                                   filter_simple, get_int_request_param,
                                   insert_simple, order_simple,
                                   pagination_simple, print_query,
                                   search_simple, select_simple, to_int,
                                   update_simple)

from django.db.models import F, Q

from .models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from .serializers import (AccordsSerializer, AccordsShortSerializer,
                          AuthorsSerializer, AuthorsShortSerializer,
                          GenresSerializer, GenresShortSerializer,
                          SongGenresListSerializer, SongGenresSerializer,
                          SongLikesListSerializer, SongLikesSerializer,
                          SongsListSerializer, SongsSerializer,
                          SongsShortSerializer)


import requests
from bs4 import *
from django.shortcuts import render
from django.views import View

PERMISSION_CLASSES = [AllowAny]
# PERMISSION_CLASSES=[IsAuthenticated]

PRINT_QUERY = True


PARAM_SEARCH_DESCRIPTION = "char '+' means AND"
PARAM_PAGE_0_DESCRIPTION = 'page=0 retrieve records count'


def get_page(url: str) -> dict:
    try:
        respond = requests.get(url)

        soup = BeautifulSoup(respond.text, "html.parser")
        soup.prettify()
        return {
            "error": "ok",
            "title": soup.title.get_text(),
            "text": soup.get_text(),
        }
    except Exception as exception:
        error = f'Can not get page {url}. {exception}'
        print(error)
        return {
            "error": error,
        }


@extend_schema(tags=['scrape url'])
class ScrapeView(GenericAPIView):
    """ Scrape """
    @extend_schema(
        description='scrape url',
        parameters=[
            OpenApiParameter("url", description='url'),
        ],
    )
    def get(self, request, format=None):
        result = get_page(request.GET.get("url"))
        return Response([result], status=status.HTTP_200_OK)


class ScrapeHTMLView(View):
    def get(self, request, *args, **kwargs):
        # Your processing logic here

        # Rendering the HTML file
        return render(request, 'song/index.html', context={'variable': 'value'})


@extend_schema(tags=['song : list of genres'])
class GenresView(APIView):
    """ GenresView """
    permission_classes = PERMISSION_CLASSES
    serializer_class = GenresSerializer
    model = Genres

    @extend_schema(
        description='genre_id=0 retrieve all records before applying filters',
        parameters=[
            OpenApiParameter("search", description=PARAM_SEARCH_DESCRIPTION),
            OpenApiParameter(
                "page", description=PARAM_PAGE_0_DESCRIPTION),
            OpenApiParameter("page_size"),
            OpenApiParameter("short"),
        ],
    )
    def get(self, request, genre_id=0, format=None):
        """ get """
        return select_simple(
            self.model,
            request,
            genre_id,
            self.serializer_class,
            short_serializer_class=GenresShortSerializer,
            search_field='name',
            order_field='name',
            is_print_query=PRINT_QUERY)

    def post(self, request, genre_id=0, format=None):
        """ post """
        return insert_simple(self.serializer_class, request.data)

    def put(self, request, genre_id=0, format=None):
        """ put """
        return update_simple(self.model, request, genre_id, self.serializer_class)

    def delete(self, request, genre_id=0, format=None):
        """ delete """
        return delete_simple(self.model, Q(pk=genre_id))


@extend_schema(tags=['song : list of authors'])
class AuthorsView(APIView):
    """ AuthorsView """
    permission_classes = PERMISSION_CLASSES
    serializer_class = AuthorsSerializer
    model = Authors

    # API_TEXT_ADD_SONGS = 'add_songs'

    @extend_schema(
        description='author_id=0 retrieve all records before applying filters',
        parameters=[
            OpenApiParameter("search", description=PARAM_SEARCH_DESCRIPTION),
            OpenApiParameter(
                "page", description=PARAM_PAGE_0_DESCRIPTION),
            OpenApiParameter("page_size"),
            OpenApiParameter("short"),
            # OpenApiParameter(API_TEXT_ADD_SONGS, description='add songs'),
        ]
    )
    def get(self, request, author_id=0, format=None):
        """ get """

        # add_songs = to_int(request.query_params.get(
        #     self.API_TEXT_ADD_SONGS, '0'), 0)
        # if add_songs != 0:
        #     add_songs = min(add_songs, 6)
        #     return Response([], status=status.HTTP_400_BAD_REQUEST)

        return select_simple(
            self.model,
            request,
            author_id,
            self.serializer_class,
            short_serializer_class=AuthorsShortSerializer,
            search_field='name',
            order_field='name',
            is_print_query=PRINT_QUERY)

    def post(self, request, author_id=0, format=None):
        """ post """
        return insert_simple(self.serializer_class, request.data)

    def put(self, request, author_id=0, format=None):
        """ put """
        return update_simple(self.model, request, author_id, self.serializer_class)

    def delete(self, request, author_id=0, format=None):
        """ delete """
        return delete_simple(self.model, Q(pk=author_id))


@extend_schema(tags=['song : list of accords'])
class AccordsView(APIView):
    """AccordsView"""
    permission_classes = PERMISSION_CLASSES
    serializer_class = AccordsSerializer
    model = Accords

    @extend_schema(
        description='accord_id=0 retrieve all records before applying filters',
        parameters=[
            OpenApiParameter("search", description=PARAM_SEARCH_DESCRIPTION),
            OpenApiParameter(
                "page", description=PARAM_PAGE_0_DESCRIPTION),
            OpenApiParameter("page_size"),
            OpenApiParameter("short"),
        ]
    )
    def get(self, request, accord_id=0, format=None):
        """ get """
        return select_simple(
            self.model,
            request,
            accord_id,
            self.serializer_class,
            short_serializer_class=AccordsShortSerializer,
            search_field='name',
            order_field='name',
            is_print_query=PRINT_QUERY)

    def post(self, request, accord_id=0, format=None):
        """ post """
        return insert_simple(self.serializer_class, request.data)

    def put(self, request, accord_id=0, format=None):
        """ put """
        return update_simple(self.model, request, accord_id, self.serializer_class)

    def delete(self, request, accord_id=0, format=None):
        """ delete """
        return delete_simple(self.model, Q(pk=accord_id))


@extend_schema(tags=['song : list of pairs (song, genre of this song)'])
class SongGenresView(APIView):
    """SongGenresView"""

    permission_classes = PERMISSION_CLASSES
    serializer_class = SongGenresSerializer
    model = SongGenres

    @extend_schema(
        description='song_id=0 retrieve all records before applying filters',
        parameters=[
            OpenApiParameter("search", description=PARAM_SEARCH_DESCRIPTION),
            OpenApiParameter(
                "page", description=PARAM_PAGE_0_DESCRIPTION),
            OpenApiParameter("page_size"),
        ],
    )
    def get(self, request, song_id=0, genre_id=0, format=None):
        """ get """
        serializer = SongGenresListSerializer
        fields = serializer.Meta.fields
        # print('fields:', fields)
        queryset = self.model.objects.select_related(
            'genre_id'
        ).annotate(
            genre_name=F('genre_id__name')
        ).values(
            *fields)

        queryset = filter_simple(queryset, 'song_id', song_id)
        queryset = filter_simple(queryset, 'genre_id', genre_id)
        # queryset = filter_params_simple(queryset, 'genre_id', request)

        if not request.query_params.get(API_TEXT_SEARCH) is None:
            queryset = search_simple(
                queryset,
                request.query_params.get(API_TEXT_SEARCH),
                'genre_name',
            )

        queryset = order_simple(queryset, 'genre_name')

        print_query(PRINT_QUERY, queryset)

        return pagination_simple(request, serializer, queryset)

    @extend_schema(
        request=None,
    )
    def post(self, request, song_id=0, genre_id=0, format=None):
        """ post """
        return insert_simple(self.serializer_class, {
            'song_id': song_id,
            'genre_id': genre_id
            # get_int_request_param(
            # request, 'genre_id', None )
        })

    def delete(self, request, song_id=0, genre_id=0, format=None):
        """ delete """
        return delete_simple(self.model,
                             Q(
                                 song_id=song_id,
                                 genre_id=genre_id
                                 #  get_int_request_param(
                                 #  request, 'genre_id', None
                             )
                             )


@extend_schema(tags=['song : list of pairs (song, user who likes this song)'])
class SongLikesView(APIView):
    permission_classes = PERMISSION_CLASSES
    serializer_class = SongLikesSerializer
    model = SongLikes

    @extend_schema(
        description='song_id=0 retrieve all records before applying filters',
        parameters=[
            OpenApiParameter("search", description=PARAM_SEARCH_DESCRIPTION),
            OpenApiParameter(
                "page", description=PARAM_PAGE_0_DESCRIPTION),            OpenApiParameter("page_size"),
        ],
    )
    def get(self, request, song_id=0, user_id=0, format=None):
        """ get """
        serializer = SongLikesListSerializer
        fields = serializer.Meta.fields
        queryset = self.model.objects.select_related(
            'user_id'
        ).annotate(
            user_email=F('user_id__email')
        ).values(
            *fields)

        queryset = filter_simple(queryset, 'song_id', song_id)
        queryset = filter_simple(queryset, 'user_id', user_id)
        # queryset = filter_params_simple(queryset, 'user_id', request)

        if not request.query_params.get(API_TEXT_SEARCH) is None:
            queryset = search_simple(
                queryset,
                request.query_params.get(API_TEXT_SEARCH),
                'user_email',
            )

        queryset = order_simple(queryset, 'user_name')
        print_query(PRINT_QUERY, queryset)

        return pagination_simple(request, serializer, queryset)

    @extend_schema(
        request=None,
    )
    def post(self, request, song_id=0, user_id=0, format=None):
        """ post """
        return insert_simple(self.serializer_class, {
            'song_id': song_id,
            'user_id': user_id
            # get_int_request_param(
            #     request, 'user_id', None
            # )
        })

    def delete(self, request, song_id=0, user_id=0, format=None):
        """ delete """
        return delete_simple(self.model,
                             Q(
                                 song_id=song_id,
                                 user_id=user_id
                                 #  get_int_request_param(
                                 #      request, 'user_id', None
                                 #  )
                             ))


@extend_schema(tags=['song : list of songs'])
class SongsView(APIView):
    """SongsView"""
    permission_classes = PERMISSION_CLASSES
    serializer_class = SongsSerializer
    model = Songs

    @extend_schema(
        description='song_id=0 retrieve all records before applying filters',
        parameters=[
            OpenApiParameter("user_id"),
            OpenApiParameter("author_id"),

            OpenApiParameter("search", description=PARAM_SEARCH_DESCRIPTION),
            OpenApiParameter(
                "page", description=PARAM_PAGE_0_DESCRIPTION),
            OpenApiParameter("page_size"),
            OpenApiParameter("short"),
        ],
    )
    def get(self, request, song_id=0, format=None):
        """ get """
        serializer_class_local = (
            SongsShortSerializer
            if request.query_params.get(API_TEXT_SHORT, '0') == '1'
            else SongsListSerializer
        )

        fields = serializer_class_local.Meta.fields
        queryset = self.model.objects.select_related(
            'user_id'
        ).annotate(
            user_email=F('user_id__email')
        ).select_related(
            'author_id'
        ).annotate(
            author_name=F('author_id__name')
        ).annotate(
            author_link=F('author_id__link')
        ).values(
            *fields)

        queryset = filter_simple(queryset, 'song_id', song_id)
        queryset = filter_params_simple(queryset, 'author_id', request)
        queryset = filter_params_simple(queryset, 'user_id', request)

        if not request.query_params.get(API_TEXT_SEARCH) is None:
            queryset = search_simple(
                queryset,
                request.query_params.get(API_TEXT_SEARCH),
                "title")

        queryset = order_simple(queryset, 'title')

        print_query(PRINT_QUERY, queryset)

        return pagination_simple(request, serializer_class_local, queryset)

    def post(self, request, song_id=0, format=None):
        """ post """
        try:
            params = request.data
        except (AttributeError):
            params = {}

        return insert_simple(self.serializer_class,
                             params |
                             {
                                 'author_id': get_int_request_param(
                                     request, 'author_id', None
                                 ),
                                 'user_id': get_int_request_param(
                                     request, 'user_id', None
                                 )
                             })

    def put(self, request, song_id=0, format=None):
        """ put """
        return update_simple(self.model, request, song_id, self.serializer_class)

    def delete(self, request, song_id=0, format=None):
        """ delete """
        return delete_simple(self.model, Q(pk=song_id))
