""" songs serializers"""
from rest_framework import serializers
from utils.views_functions import (representation_simple)

from .models import (
    Song,
    Accord,
    Author,
    SongGenre,
    SongLike,
    Genre
)


class GenreSerializer(serializers.ModelSerializer):
    """GenreSerializer"""
    class Meta:
        model = Genre
        fields = '__all__'


class GenreShortSerializer(serializers.ModelSerializer):
    """GenreShortSerializer"""
    class Meta:
        model = Genre
        fields = ['genre_id', 'name']


class AccordSerializer(serializers.ModelSerializer):
    """AccordSerializer"""
    class Meta:
        model = Accord
        fields = '__all__'


class AccordShortSerializer(serializers.ModelSerializer):
    """AccordShortSerializer"""
    class Meta:
        model = Accord
        fields = ['accord_id', 'short_name']


class AuthorSerializer(serializers.ModelSerializer):
    """AuthorSerializer"""
    class Meta:
        model = Author
        fields = '__all__'


class AuthorShortSerializer(serializers.ModelSerializer):
    """AuthorShortSerializer"""
    class Meta:
        model = Author
        fields = ['author_id', 'name']


class SongGenreSerializer(serializers.ModelSerializer):
    """SongGenreSerializer"""
    class Meta:
        model = SongGenre
        fields = '__all__'


class SongGenreListSerializer(serializers.ModelSerializer):
    """SongGenreListSerializer"""

    class Meta:
        model = SongGenre
        fields = ['song_id', 'genre_id', 'genre_name']

    def to_representation(self, instance):
        return representation_simple(self.Meta.fields, instance)


class SongLikeSerializer(serializers.ModelSerializer):
    """SongLikeSerializer"""

    class Meta:
        model = SongLike
        fields = '__all__'


class SongLikeListSerializer(serializers.ModelSerializer):
    """SongLikeListSerializer"""

    class Meta:
        model = SongLike
        fields = ['song_id', 'user_id', 'user_email']

    def to_representation(self, instance):
        return representation_simple(self.Meta.fields, instance)


class SongSerializer(serializers.ModelSerializer):
    """SongSerializer"""

    class Meta:
        model = Song
        fields = '__all__'


class SongListSerializer(serializers.ModelSerializer):
    """SongListSerializer"""

    class Meta:
        model = Song
        fields = [
            'song_id',
            'user_id',
            'user_email',
            'author_id',
            'author_name',
            'title',
            'text_with_accords',
            'date_creation',
            'link'
        ]

    def to_representation(self, instance):
        return representation_simple(self.Meta.fields, instance)


class SongShortSerializer(serializers.ModelSerializer):
    """SongShortSerializer"""

    class Meta:
        model = Song
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
