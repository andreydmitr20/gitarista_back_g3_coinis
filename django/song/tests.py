""" song part tests """
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from user.models import User
from utils.functions_for_tests import TestEndpoints


API_URL = "/api/v2/songs/"


class TestSongGenresEndpoints(TestEndpoints):
    """ TestSongGenresEndpoints """

    endpoint = API_URL+'genres/'

    def test_get_count0(self, client):

        expected_data = [
            {'count': 0}
        ]

        response = self.get(client, self.endpoint +
                            '0/?page=0')

        assert self.is_equal(
            response.data,
            expected_data
        )

    def test_get_count(self, client):

        self.fill_test_data(Genres)

        expected_data = [
            {'count': len(Genres.test_data)}
        ]

        response = self.get(client, self.endpoint +
                            '0/?page=0')

        assert self.is_equal(
            response.data,
            expected_data
        )

    def test_get_search(self, client):

        self.fill_test_data(Genres)

        expected_data = [
            {'genre_id': 1, **Genres.test_data[0]}
        ]

        response = self.get(client, self.endpoint +
                            '0/?page_size=1000&search=' +
                            Genres.test_data[0]['name']
                            )

        assert len(response.data) == 1
        assert self.is_equal(
            response.data,
            expected_data
        )

    def test_get_short(self, client):

        self.fill_test_data(Genres)

        genre_id = 2
        expected_data = [
            {'genre_id': genre_id,
             'name': Genres.test_data[genre_id-1]['name']}
        ]

        response = self.get(client, self.endpoint +
                            str(genre_id)+'/?page_size=1000&short=1'
                            )

        assert len(response.data) == 1
        assert self.is_equal(
            response.data,
            expected_data
        )

    def test_post(self, client):

        self.fill_test_data(Genres)

        temp_data = {'name': 'Test genre',
                     'description': 'Test genre description'}
        expected_data = {
            'genre_id': len(Genres.test_data)+1,
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

        # self.get_row_by_id
