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


class AuthorSerializer(serializers.ModelSerializer):
    """AuthorSerializer"""
    class Meta:
        model = Author
        fields = '__all__'


class SongGenreSerializer(serializers.ModelSerializer):
    """SongGenreSerializer"""
    class Meta:
        model = SongGenre
        fields = '__all__'


class SongLikeSerializer(serializers.ModelSerializer):
    """SongLikeSerializer"""
    class Meta:
        model = SongLike
        fields = '__all__'


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
