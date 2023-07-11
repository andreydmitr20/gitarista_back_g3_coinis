""" song part tests """
from math import exp
from random import randint
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from song.data_for_tests import DataForTests
from user.models import Users
from utils.functions_for_tests import (
    Endpoints,
    ListEndpoints,
    CompositeEndpoints
)

API_URL = "/api/v2/songs/"


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


class TestSongSongGenresEndpoints(CompositeEndpoints):
    """ TestSongSongGenresEndpoints """

    data_class = DataForTests
    endpoint = API_URL
    endpoint_suffix = 'genres/'
    model = SongGenres
    model_main_field_id_name = 'song_id'
    model_search_field_id_name = 'genre_id'
    model_search_field_name = 'name'
    model_second_field_name = 'genre_name'
    temp_data = {
        'song_id': 1,
        'genre_id': 4,
    }


class TestSongSongLikesEndpoints(CompositeEndpoints):
    """ TestSongSongLikesEndpoints """

    data_class = DataForTests
    endpoint = API_URL
    endpoint_suffix = 'likes/'
    model = SongLikes
    model_main_field_id_name = 'song_id'
    model_search_field_id_name = 'user_id'
    model_search_field_name = 'email'
    model_second_field_name = 'user_email'
    temp_data = {
        'song_id': 3,
        'user_id': 3,
    }


class TestSongsEndpoints(Endpoints):
    """ tests for table with pk_id """
    data_class = DataForTests
    endpoint = API_URL
    model = Songs
    model_pk_field_name = 'song_id'
    model_search_field_name = 'title'
    fields_to_skip = ['date_creation',
                      'author_name',
                      'author_link',
                      'user_email']
    temp_data = {
        'user_id': 3,
        'author_id': 3,
        'title': 'Где цветы',
        'link': 'https://amdm.ru/akkordi/megapolis/11464/gde_cveti/',
                'text_with_accords':
        """G           Em
        Где цветы, дай мне ответ,
        C           D
        где они остались?
        G           Em
        Где цветы, дай мне ответ,
        C           D
        где они растут?
        G           Em
        Где цветы, дай мне ответ -
        C           D
        девушки сорвали, и вот их нет.

        Припев:
        C         G   
        Когда же все это поймут?
        С         D   G
        Когда же все поймут? 

        G           Em
        А девушки где, дай ответ,
        C           D
        где они остались?
        G           Em
        Девушки где, дай ответ,
        C           D
        где они живут?
        G           Em
        Девушки где, дай ответ -
        C           D
        вышли замуж, и вот их нет.
        G           Em
        Когда же все это поймут?
        C           D
        Когда же все поймут? 

        Припев:
        C         G   
        Когда же все это поймут?
        С         D   G
        Когда же все поймут? 

        G           Em
        А где мужья их, дай ответ,
        C           D
        где они остались?
        G           Em
        Где мужья их, дай ответ,
        C           D
        где теперь живут?
        G           Em
        Где мужья их, дай ответ -
        C           D
        ушли в солдаты, и вот их нет.
        G           Em
        Когда же все это поймут?
        C           D
        Когда же все поймут? 

        Припев:
        C         G   
        Когда же все это поймут?
        С         D   G
        Когда же все поймут? 

        G           Em
        А где солдаты, дай ответ,
        C           D
        где они остались?
        G           Em
        Где солдаты, дай ответ,
        C           D
        ведь их так ждут!
        G           Em
        Где солдаты, дай ответ -
        C           D
        легли в могилы, и вот их нет.
        G           Em
        Когда же все это поймут?
        C           D
        Когда же все поймут? 

        Припев:
        C         G   
        Когда же все это поймут?
        С         D   G
        Когда же все поймут? 

        G           Em
        Где могилы, дай ответ,
        C           D
        где они остались?
        G           Em
        Где могилы, дай ответ,
        C           D
        где слезы льют?
        G           Em
        Где могилы, дай ответ -
        C           D
        цветами стали, и вот их нет.
        G           Em
        Когда же все это поймут?
        C           D
        Когда же все поймут? 

        Припев:
        C         G   
        Когда же все это поймут?
        С         D   G
        Когда же все поймут?"""
    }

    # --------------------

    def test_get_count_bad(self, client):

        test_data = self.fill(self.data_class,
                              [],
                              self.model)
        self.get_assert(
            client,

            self.endpoint +
            '0/',

            expected_data={'count': len(test_data)},
            negative_expected_data_test=True)

        self.get_assert(
            client,

            self.endpoint +
            '100000/',
            expected_data=None,
            status_code=400,
            negative_status_code_test=True)

    # ++++++++++++++++++++

    def test_get_count0(self, client):

        self.get_assert(
            client,
            self.endpoint +
            '0/?page=0',

            expected_data={'count': 0})

    def test_get_count(self, client):

        test_data = self.fill(self.data_class,
                              [],
                              self.model)
        self.get_assert(
            client,

            self.endpoint +
            '0/?page=0',

            expected_data={'count': len(test_data)})

    def test_get_search(self, client):

        test_data = self.fill(self.data_class,
                              [],
                              self.model)

        pk_id = randint(1, len(test_data))

        search_text = (
            test_data[pk_id-1][self.model_search_field_name]
            .replace(' ', '%20')
        )

        expected_data = {
            self.model_pk_field_name: pk_id,
            **test_data[pk_id-1],
            'author_name': self.get_fk_field_value(self.model,
                                                   pk_id,
                                                   'author_id',
                                                   'name'),
            'author_link': self.get_fk_field_value(self.model,
                                                   pk_id,
                                                   'author_id',
                                                   'link'),
            'user_email': self.get_fk_field_value(self.model,
                                                  pk_id,
                                                  'user_id',
                                                  'email'),
        }

        self.get_assert(
            client,

            self.endpoint +
            '0/?page_size=1000&search=' +
            search_text,

            expected_data=expected_data,
            fields_to_skip=['date_creation']
        )

    def test_get_short(self, client):

        test_data = self.fill(self.data_class,
                              [],
                              self.model)
        pk_id = randint(1, len(test_data))

        expected_data = {
            self.model_pk_field_name: pk_id,
            **test_data[pk_id - 1],
            'author_name': self.get_fk_field_value(self.model,
                                                   pk_id,
                                                   'author_id',
                                                   'name'),
        }
        del expected_data['text_with_accords']

        self.get_assert(
            client,

            self.endpoint +
            str(pk_id) +
            '/?page_size=1000&short=1',

            expected_data=expected_data,
            fields_to_skip=self.fields_to_skip
        )

    def test_post(self, client):

        test_data = self.fill(self.data_class,
                              [],
                              self.model)
        expected_data = {
            self.model_pk_field_name: len(test_data)+1,
            **self.temp_data
        }

        response = self.post(
            client,
            self.endpoint +
            '0/',
            self.temp_data
        )

        self.log(f'resp: {response.data}\n exp: {expected_data}\n')
        assert self.is_equal(response.data,
                             expected_data,
                             fields_to_skip=self.fields_to_skip
                             )

        self.get_assert(
            client,

            self.endpoint +
            str(expected_data[self.model_pk_field_name])+'/',

            expected_data,
            fields_to_skip=self.fields_to_skip
        )

    def test_put(self, client):

        test_data = self.fill(self.data_class,
                              [],
                              self.model)

        pk_id = randint(1, len(test_data))
        api_endpoint = self.endpoint + str(pk_id)+'/'
        expected_data = {
            self.model_pk_field_name: pk_id,
            ** test_data[pk_id-1]
        }

        self.get_assert(client,
                        api_endpoint,
                        expected_data,
                        fields_to_skip=self.fields_to_skip
                        )

        response = self.put(client, api_endpoint, self.temp_data)

        expected_data = {
            **expected_data,
            **self.temp_data
        }

        assert self.is_equal(
            response.data,
            expected_data,
            fields_to_skip=self.fields_to_skip
        )

        self.get_assert(client,
                        api_endpoint,
                        expected_data,
                        fields_to_skip=self.fields_to_skip
                        )

    def test_delete(self, client):

        test_data = self.fill(self.data_class,
                              [],
                              self.model)

        pk_id = randint(1, len(test_data))
        api_endpoint = self.endpoint + str(pk_id)+'/'
        expected_data = {
            self.model_pk_field_name: pk_id,
            **test_data[pk_id-1]
        }

        self.get_assert(client,
                        api_endpoint,
                        expected_data,
                        fields_to_skip=self.fields_to_skip
                        )
        self.delete(client, api_endpoint)
        self.get_assert(client, api_endpoint, None)


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
