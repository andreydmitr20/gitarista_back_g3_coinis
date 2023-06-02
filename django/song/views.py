from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render
import django_filters
from django_filters import CharFilter

from rest_framework import mixins
from rest_framework import generics


from .models import Song, Accord, Author, SongGenre, SongLike, Genre
from .serializers import (SongSerializer,
                          AuthorSerializer,
                          GenreSerializer,
                          SongLikeSerializer,
                          SongGenreSerializer,
                          AccordSerializer)

DEFAULT_PAGE_SIZE_FOR_PAGINATION = 4

PERMISSION_CLASSES = [AllowAny]
# PERMISSION_CLASSES=[IsAuthenticated]

# ERROR_NO_SEARCH_ALLOWED=[]

API_TEXT_SEARCH = 'search'
API_TEXT_PAGE = 'page'
API_TEXT_PAGE_SIZE = 'page_size'
API_TEXT_SHORT = 'short'
API_TEXT_ORDER = 'order_by'


"""
  create POST api-path/ body has data | return created object with id
  retrieve GET api-path/ url has data | all with pagination
            api-path/id | all data with id


"""


def parse_search_to_queryset(queryset,
                             search_text: str,
                             search_field):
    """ search by max 3 patterns space separated """

    search_text = search_text.strip()

    if search_text != '':
        search_text = search_text.split(' ')
    search_text_len = len(search_text)
    if search_text_len > 0:
        if search_text_len == 1:
            print(':', search_text[0].strip())
            queryset = queryset.filter(
                Q(**{'{}__icontains'.format(search_field)
                  : search_text[0].strip()})
            )
        elif search_text_len == 2:
            queryset = queryset.filter(
                Q(**{'{}__icontains'.format(search_field)
                  : search_text[0].strip()})
                | Q(**{'{}__icontains'.format(search_field): search_text[1].strip()})
            )
        else:
            queryset = queryset.filter(
                Q(**{'{}__icontains'.format(search_field)
                  : search_text[0].strip()})
                | Q(**{'{}__icontains'.format(search_field): search_text[1].strip()})
                | Q(**{'{}__icontains'.format(search_field): search_text[2].strip()})
            )

    return queryset


# genre

class GenreView(APIView):
    """ CRUD """
    permission_classes = PERMISSION_CLASSES
    serializer_class = GenreSerializer
    short_serializer_class = GenreSerializer
    model = Genre
    search_field = 'name'

    def get_object(self, id):
        """ get_object """
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        """ R - retrieve """

        serializer_class_local = (
            self.serializer_class
            if (self.request.query_params.get(API_TEXT_SHORT) != '1')
            else self.short_serializer_class)

        fields = serializer_class_local.Meta.fields
        queryset = (self.model.objects.all()
                    if isinstance(fields, str)
                    else self.model.objects
                    # inner join
                    # .select_related('user')
                    .values(*fields))

        # if (self.request.query_params.get('mine') == "1"):
        #     queryset = queryset.filter(user=self.request.user.id)

        if not self.request.query_params.get(API_TEXT_SEARCH) is None:
            if not hasattr(self, "search_field"):
                return Response([], status=status.HTTP_400_BAD_REQUEST)
            queryset = parse_search_to_queryset(
                queryset,
                self.request.query_params.get(API_TEXT_SEARCH),
                self.search_field)

        order_by = self.request.query_params.get(API_TEXT_ORDER, '-id')
        if not order_by is None:
            queryset = queryset.order_by(order_by)

        if not id is None:
            queryset = queryset.filter(pk=id)

        print(queryset.query)

        page = self.request.query_params.get(API_TEXT_PAGE, 1)
        if page == '0':
            # return count
            count = queryset.count()
            return Response([{'count': count}], status=status.HTTP_200_OK)

        page_size = self.request.query_params.get(API_TEXT_PAGE_SIZE,
                                                  DEFAULT_PAGE_SIZE_FOR_PAGINATION)
        try:
            paginator = Paginator(queryset, page_size)
            serializer = serializer_class_local(paginator.page(
                page), many=True, context={'request': self.request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EmptyPage:
            return Response([], status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        instance = self.get_object(id)
        # check if the same user
        # if ingredient.user_id != request.user.id:
        #     return Response(USER_IS_NOT_AUTHORIZED_TO_DELETE, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id=None, format=None):
    #     instance = self.get_object(id)
    #     # check if the same user
    #     # if ingredient.user_id != request.user.id:
    #     #     return Response(USER_IS_NOT_AUTHORIZED_TO_DELETE, status=status.HTTP_400_BAD_REQUEST)
    #     try:
    #         instance.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except:
    #         return Response(ERROR_WHILE_DELETING, status=status.HTTP_400_BAD_REQUEST)


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
