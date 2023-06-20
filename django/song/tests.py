""" song part tests """
from song.models import Accords, Authors, Genres, SongGenres, SongLikes, Songs
from user.models import Users
from utils.functions_for_tests import (
    ListEndpoints
)


API_URL = "/api/v2/songs/"


class TestSongGenresEndpoints(ListEndpoints):
    """ TestSongGenresEndpoints """
    endpoint = API_URL+'genres/'
    model = Genres
    model_pk_field_name = 'genre_id'
    model_search_field_name = 'name'
    temp_data = {
        'name': 'Test genre',
        'description': 'Test genre description'
    }
    test_data = [
        {'name': 'Rock', 'description': 'This genre encompasses various subgenres such as classic rock, hard rock, alternative rock, punk rock, and progressive rock. Guitar-driven bands and iconic guitar solos are a defining characteristic of rock music'},
        {'name': 'Blues', 'description': 'Originating from African-American communities in the United States, blues music heavily relies on the guitar. It often features soulful playing, bending of notes, and expressive solos'},
        {'name': 'Jazz', 'description': 'Jazz music incorporates improvisation and complex harmonies. The guitar plays a significant role in jazz, both as a rhythm instrument and for soloing. Subgenres like gypsy jazz and smooth jazz also have distinct guitar styles'},
        {'name': 'Country', 'description': 'Country music often features acoustic and electric guitars, including fingerpicking and twangy guitar sounds. It encompasses subgenres like traditional country, country rock, and outlaw country'},
        {'name': 'Metal', 'description': 'Known for its heavy sound, aggressive riffs, and fast guitar playing, metal music is characterized by distorted guitars and intricate solos. Subgenres like thrash metal, heavy metal, and power metal are all guitar-driven'},
    ]


class TestSongAuthorsEndpoints(ListEndpoints):
    """ TestSongAuthorsEndpoints """
    endpoint = API_URL+'authors/'
    model = Authors
    model_pk_field_name = 'author_id'
    model_search_field_name = 'name'
    temp_data = {
        'name': 'Test author name',
        'link': 'http://test.link'
    }
    test_data = [
        {'name': 'Johnny Cash', 'link': 'https://en.wikipedia.org/wiki/Johnny_Cash'},
        {'name': 'The Beatles', 'link': 'https://sh.wikipedia.org/wiki/The_Beatles'},
        {'name': 'Чёрный Обелиск',
            'link': 'https://ru.wikipedia.org/wiki/%D0%A7%D1%91%D1%80%D0%BD%D1%8B%D0%B9_%D0%9E%D0%B1%D0%B5%D0%BB%D0%B8%D1%81%D0%BA_(%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B0)'},
    ]


class TestSongAccordsEndpoints(ListEndpoints):
    """ TestSongAccordsEndpoints """
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
    test_data = [
        {'name': 'A major', 'short_name': 'A',
            'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/A-Major-Chord-Open-Finger-Numbers.jpg.webp'},
        {'name': 'E9', 'short_name': 'E9',
            'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/E-9-Chord-7th-Fret-5th-String-Root-1.jpg.webp'},
        {'name': 'E minor', 'short_name': 'Em',
            'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/E-Minor-Chord-Open-Finger-Numbers.jpg.webp'},
        {'name': 'G major', 'short_name': 'G',
            'link': 'https://www.audiolisted.com/wp-content/uploads/2018/04/G-Major-Chord-Open-Finger-Numbers.jpg.webp'},
    ]
