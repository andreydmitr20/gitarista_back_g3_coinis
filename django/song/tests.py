""" song part tests """
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from song.datafortests import DataForTests
from user.models import Users
from utils.functions_for_tests import Endpoints, ListEndpoints

API_URL = "/api/v2/songs/"


# class TestUsersEndpoints(Endpoints):
#     """ TestUsersEndpoints """
#     fill_test_data = fill_test_data
#     endpoint = '/api/register/'
#     model = Users
#     model_pk_field_name = 'user_id'
#     model_search_field_name = 'username'
#     temp_data = {
#         'username': 'user100',
#         'email': 'user100@email.com',
#     }


class TestSongGenresEndpoints(ListEndpoints):
    """ TestSongGenresEndpoints """

    data_class = DataForTests

    endpoint = API_URL+'genres/'
    model = Genres
    model_pk_field_name = 'genre_id'
    model_search_field_name = 'name'
    temp_data = {
        'name': 'Test genre',
        'description': 'Test genre description'
    }


class TestSongAuthorsEndpoints(ListEndpoints):
    """ TestSongAuthorsEndpoints """

    data_class = DataForTests

    endpoint = API_URL+'authors/'
    model = Authors
    model_pk_field_name = 'author_id'
    model_search_field_name = 'name'
    temp_data = {
        'name': 'Test author name',
        'link': 'http://test.link'
    }


class TestSongAccordsEndpoints(ListEndpoints):
    """ TestSongAccordsEndpoints """

    data_class = DataForTests

    endpoint = API_URL+'accords/'
    model = Accords
    model_pk_field_name = 'accord_id'
    model_search_field_name = 'name'
    model_short_field_name = 'short_name'
    temp_data = {
        'name': 'Test accord name',
        'link': 'http://test.link',
        "short_name": 'Sn'
    }


# class TestSongSongGenresEndpoints(CompositeEndpoints):
#     """ TestSongSongGenresEndpoints """
#     endpoint = API_URL+'/'
#     endpoint_suffix = 'genres/'
#     model = SongGenres
#     # model_pk_field_name = 'accord_id'
#     # model_search_field_name = 'name'
#     # model_short_field_name = 'short_name'
#     temp_data = {
#         'song_id': 1,
#         'genre_id': 3,
#     }

#     def fill_data(self):
#         Genres.fill_test_data()
#         Songs.fill_test_data()


# class TestSongSongLikesEndpoints(CompositeEndpoints):
#     """ TestSongSongGenresEndpoints """
#     endpoint = API_URL+'/'
#     endpoint_suffix = 'likes/'
#     model = SongLikes
#     # model_pk_field_name = 'accord_id'
#     # model_search_field_name = 'name'
#     # model_short_field_name = 'short_name'
#     temp_data = {
#         'song_id': 2,
#         'user_id': 1,
#     }

#     def fill_data(self):
#         Users.fill_test_data()
#         Songs.fill_test_data()
