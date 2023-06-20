""" song part tests """
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from user.models import User
from utils.functions_for_tests import TestEndpoints


API_URL = "/api/v2/songs/"


class TestSongGenresEndpoints(TestEndpoints):
    """ TestSongGenresEndpoints """

    endpoint = API_URL+'genres/'
    model = Genres

    def test_get_count0(self, client):

        self.get_assert(
            client,
            self.endpoint +
            '0/?page=0',

            expected_data={'count': 0})

    def test_get_count(self, client):

        self.fill_model(self.model)

        self.get_assert(
            client,

            self.endpoint +
            '0/?page=0',

            expected_data={'count': len(self.model.test_data)})

    def test_get_search(self, client):

        self.fill_model(self.model)

        response = self.get_assert(
            client,

            self.endpoint +
            '0/?page_size=1000&search=' +
            self.model.test_data[0]['name'],

            expected_data={
                'genre_id': 1,
                **self.model.test_data[0]
            }
        )

        assert len(response.data) == 1

    def test_get_short(self, client):

        self.fill_model(self.model)

        genre_id = 2

        response = self.get_assert(
            client,

            self.endpoint +
            str(genre_id) +
            '/?page_size=1000&short=1',

            expected_data={
                'genre_id': genre_id,
                'name': self.model.test_data[genre_id-1]['name']
            }
        )

        assert len(response.data) == 1

    def test_post(self, client):

        self.fill_model(self.model)

        temp_data = {'name': 'Test genre',
                     'description': 'Test genre description'}
        expected_data = {
            'genre_id': len(self.model.test_data)+1,
            **temp_data
        }

        response = self.post(client, self.endpoint +
                             '0/',
                             temp_data
                             )

        assert self.is_equal(
            response.data,
            expected_data
        )

        response = self.get_assert(
            client,

            self.endpoint +
            str(expected_data['genre_id'])+'/',

            expected_data
        )

    def test_put(self, client):

        self.fill_model(self.model)

        genre_id = 2
        api_endpoint = self.endpoint + str(genre_id)+'/'
        expected_data = {
            'genre_id': genre_id,
            ** self.model.test_data[genre_id-1]
        }

        self.get_assert(client, api_endpoint, expected_data)

        temp_data = {
            'name': 'Test genre',
            'description': 'Test genre description'
        }

        response = self.put(client, api_endpoint, temp_data)

        expected_data = {
            **expected_data,
            **temp_data
        }

        assert self.is_equal(
            response.data,
            expected_data
        )

        self.get_assert(client, api_endpoint, expected_data)

    def test_delete(self, client):

        self.fill_model(self.model)

        genre_id = 2
        api_endpoint = self.endpoint + str(genre_id)+'/'
        expected_data = {
            'genre_id': genre_id,
            ** self.model.test_data[genre_id-1]
        }

        self.get_assert(client, api_endpoint, expected_data)
        self.delete(client, api_endpoint)
        self.get_assert(client, api_endpoint, None)
