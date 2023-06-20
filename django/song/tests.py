""" song part tests """
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from user.models import User
from utils.functions_for_tests import TestEndpoints


API_URL = "/api/v2/songs/"


class TestSongGenresEndpoints(TestEndpoints):
    """ TestSongGenresEndpoints """

    endpoint = API_URL+'genres/'

    def test_get_count0(self, client):
        """ test_get """
        expected_data = [{'count': 0}]

        response = client.get(self.endpoint+'0/?page=0')
        self.log(response.data)

        assert response.status_code == 200
        assert self.is_equal(
            response.data,
            expected_data
        )

    def test_get_count(self, client):
        """ test_get """
        expected_data = [{'count': len(Genres.test_data)}]

        self.fill_test_data(Genres)

        response = client.get(self.endpoint+'0/?page=0')
        self.log(response.data)

        assert response.status_code == 200
        assert self.is_equal(
            response.data,
            expected_data
        )


# @pytest.mark.django_db
# def test_genre_create():
#     genre = Genres.objects.create(name="genre1", description="description")
#     assert genre.name == "genre1"


# @pytest.mark.django_db
# def test_song_genres_get(client):
#     response = client.get(API_BASE_URL+API_VERSION+'songs/genres/0/')
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_song_genres_get_count(client):
#     Genres.objects.create(
#         name="genre1", description="description"
#     ).save()

#     response = client.get(API_BASE_URL+API_VERSION +
#                           'songs/genres/0/?page=0')
#     log(response.data)

#     assert response.status_code == 200
#     assert is_objects_deep_equal(
#         response.data,
#         [{'count': 0}]
#     )
