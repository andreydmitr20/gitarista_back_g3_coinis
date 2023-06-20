import json
import logging

import pytest
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from user.models import User

from utils.functions_for_tests import (
    is_objects_deep_equal
)


@pytest.mark.django_db
def test_genre_create():
    genre = Genres.objects.create(name="genre1", description="description")
    assert genre.name == "genre1"


LOGGER = logging.getLogger(__name__)


def log(a):
    LOGGER.info(a)


API_BASE_URL = "/api/"
API_VERSION = "v2/"


@pytest.mark.django_db
def test_song_genres_get(client):
    response = client.get(API_BASE_URL+API_VERSION+'songs/genres/0/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_song_genres_get_count(client):
    Genres.objects.create(
        name="genre1", description="description"
    ).save()

    response = client.get(API_BASE_URL+API_VERSION +
                          'songs/genres/0/?page=0')
    log(response.data)

    assert response.status_code == 200
    assert is_objects_deep_equal(
        response.data,
        [{'count': 0}]
    )
