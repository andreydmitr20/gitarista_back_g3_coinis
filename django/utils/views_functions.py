from rest_framework import status, viewsets
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpResponse
from rest_framework.response import Response

API_TEXT_SEARCH = 'search'
API_TEXT_PAGE = 'page'
API_TEXT_PAGE_SIZE = 'page_size'
API_TEXT_SHORT = 'short'

DEFAULT_PAGE_SIZE_FOR_PAGINATION = 4


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
                Q(**{'{}__icontains'.format(search_field): search_text[0].strip()})
            )
        elif search_text_len == 2:
            queryset = queryset.filter(
                Q(**{'{}__icontains'.format(search_field): search_text[0].strip()})
                | Q(**{'{}__icontains'.format(search_field): search_text[1].strip()})
            )
        else:
            queryset = queryset.filter(
                Q(**{'{}__icontains'.format(search_field): search_text[0].strip()})
                | Q(**{'{}__icontains'.format(search_field): search_text[1].strip()})
                | Q(**{'{}__icontains'.format(search_field): search_text[2].strip()})
            )

    return queryset


def select_simple(
    model,
    request,
    id,
    serializer_class,
    short_serializer_class=None,
    search_field=None,
    order_by=None,
    print_query=False
):
    serializer_class_local = (
        short_serializer_class
        if not short_serializer_class is None and
        request.query_params.get(API_TEXT_SHORT, '0') == '1'
        else serializer_class
    )

    fields = serializer_class_local.Meta.fields
    queryset = (model.objects.all()
                if isinstance(fields, str)
                else model.objects
                # inner join
                # .select_related('user')
                .values(*fields))

    # if (self.request.query_params.get('mine') == "1"):
    #     queryset = queryset.filter(user=self.request.user.id)

    if not request.query_params.get(API_TEXT_SEARCH) is None:
        if not search_field is None:
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        queryset = parse_search_to_queryset(
            queryset,
            request.query_params.get(API_TEXT_SEARCH),
            search_field)

    if not order_by is None:
        order_by = '-id'
    queryset = queryset.order_by(order_by)

    if not id is None:
        queryset = queryset.filter(pk=id)

    if print_query:
        print(queryset.query)

    page = request.query_params.get(API_TEXT_PAGE, 1)
    if page == '0':
        # return count
        count = queryset.count()
        return Response([{'count': count}], status=status.HTTP_200_OK)

    page_size = request.query_params.get(API_TEXT_PAGE_SIZE,
                                         DEFAULT_PAGE_SIZE_FOR_PAGINATION)
    try:
        paginator = Paginator(queryset, page_size)
        serializer = serializer_class_local(paginator.page(
            page), many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except EmptyPage:
        return Response([], status=status.HTTP_200_OK)


def insert_simple(
        request,
        serializer_class
):
    """ create """
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_simple(
        model,
        request,
        id,
        serializer_class
):
    """ update """
    try:
        instance = model.objects.get(pk=id)
    except model.DoesNotExist:
        raise Http404
    # check if the same user
    # if model.user_id != request.user.id:
    #     return Response(USER_IS_NOT_AUTHORIZED_TO_DELETE, status=status.HTTP_400_BAD_REQUEST)
    serializer = serializer_class(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


ERROR_WHEN_DELETING = 'Error when deleting'


def delete_simple(
        model,
        id,
):
    try:
        instance = model.objects.get(pk=id)
    except model.DoesNotExist:
        raise Http404
    # check if the same user
    # if ingredient.user_id != request.user.id:
    #     return Response(USER_IS_NOT_AUTHORIZED_TO_DELETE, status=status.HTTP_400_BAD_REQUEST)
    try:
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(ERROR_WHEN_DELETING + ' id=' + str(id),
                        status=status.HTTP_400_BAD_REQUEST)
