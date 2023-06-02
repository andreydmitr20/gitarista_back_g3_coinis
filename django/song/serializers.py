""" songs serializers"""
from rest_framework import serializers
from .models import Song, Accord, Author, SongGenre, SongLike, Genre


class GenreSerializer(serializers.ModelSerializer):
    """GenreSerializer"""
    class Meta:
        model = Genre
        fields = '__all__'


class GenreShortSerializer(serializers.ModelSerializer):
    """GenreShortSerializer"""
    class Meta:
        model = Genre
        fields = ['id', 'name']


class AccordSerializer(serializers.ModelSerializer):
    """AccordSerializer"""
    class Meta:
        model = Accord
        fields = '__all__'


class AccordShortSerializer(serializers.ModelSerializer):
    """AccordShortSerializer"""
    class Meta:
        model = Accord
        fields = ['id', 'short_name']


class AuthorSerializer(serializers.ModelSerializer):
    """AuthorSerializer"""
    class Meta:
        model = Author
        fields = '__all__'


class AuthorShortSerializer(serializers.ModelSerializer):
    """AuthorShortSerializer"""
    class Meta:
        model = Author
        fields = ['id', 'name']


class SongGenreSerializer(serializers.ModelSerializer):
    """SongGenreSerializer"""
    class Meta:
        model = SongGenre
        fields = ['song_id', 'genre_id']


class SongGenreListSerializer(serializers.ModelSerializer):
    """SongGenreListSerializer"""
    genre__name = serializers.CharField()

    class Meta:
        model = SongGenre
        fields = ['genre_id', 'genre__name']


class SongLikeSerializer(serializers.ModelSerializer):
    """SongLikeSerializer"""
    class Meta:
        model = SongLike
        fields = ['id', 'song', 'user']


class SongSerializer(serializers.ModelSerializer):
    """SongSerializer"""
    user_name = serializers.CharField(
        source='user.username', required=False)
    author_name = serializers.CharField(
        source='author.name', required=False)

    class Meta:
        model = Song
        fields = [
            'id',
            'user_id',
            'user_name',
            'author_id',
            'author_name',
            'title',
            'text_with_accords',
            'date_creation',
            'link'
        ]
