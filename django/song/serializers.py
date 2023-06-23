""" songs serializers"""
from rest_framework import serializers
from utils.views_functions import (representation_simple)

from .models import (
    Songs,
    Accords,
    Authors,
    SongGenres,
    SongLikes,
    Genres
)


class GenresSerializer(serializers.ModelSerializer):
    """GenresSerializer"""
    class Meta:
        model = Genres
        fields = '__all__'


class GenresShortSerializer(serializers.ModelSerializer):
    """GenresShortSerializer"""
    class Meta:
        model = Genres
        fields = ['genre_id', 'name']


class AccordsSerializer(serializers.ModelSerializer):
    """AccordsSerializer"""
    class Meta:
        model = Accords
        fields = '__all__'


class AccordsShortSerializer(serializers.ModelSerializer):
    """AccordsShortSerializer"""
    class Meta:
        model = Accords
        fields = ['accord_id', 'short_name']


class AuthorsSerializer(serializers.ModelSerializer):
    """AuthorsSerializer"""
    class Meta:
        model = Authors
        fields = '__all__'


class AuthorsShortSerializer(serializers.ModelSerializer):
    """AuthorsShortSerializer"""
    class Meta:
        model = Authors
        fields = ['author_id', 'name']


class SongGenresSerializer(serializers.ModelSerializer):
    """SongGenresSerializer"""
    class Meta:
        model = SongGenres
        fields = '__all__'


class SongGenresListSerializer(serializers.ModelSerializer):
    """SongGenresListSerializer"""

    class Meta:
        model = SongGenres
        fields = ['song_id', 'genre_id', 'genre_name']

    def to_representation(self, instance):
        return representation_simple(self.Meta.fields, instance)


class SongLikesSerializer(serializers.ModelSerializer):
    """SongLikesSerializer"""

    class Meta:
        model = SongLikes
        fields = '__all__'


class SongLikesListSerializer(serializers.ModelSerializer):
    """SongLikesListSerializer"""

    class Meta:
        model = SongLikes
        fields = ['song_id', 'user_id', 'user_email']

    def to_representation(self, instance):
        return representation_simple(self.Meta.fields, instance)


class SongsSerializer(serializers.ModelSerializer):
    """SongsSerializer"""

    class Meta:
        model = Songs
        fields = '__all__'


class SongsListSerializer(serializers.ModelSerializer):
    """SongsListSerializer"""

    class Meta:
        model = Songs
        fields = [
            'song_id',
            'user_id',
            'user_email',
            'author_id',
            'author_name',
            'author_link',
            'title',
            'text_with_accords',
            'date_creation',
            'link'
        ]

    def to_representation(self, instance):
        return representation_simple(self.Meta.fields, instance)


class SongsShortSerializer(serializers.ModelSerializer):
    """SongsShortSerializer"""

    class Meta:
        model = Songs
        fields = [
            'song_id',
            'user_id',
            'author_id',
            'author_name',
            'title',
            'date_creation',
            'link'
        ]

    def to_representation(self, instance):
        return representation_simple(self.Meta.fields, instance)
