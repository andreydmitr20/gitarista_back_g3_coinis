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
        fields = '__all__'


class SongGenreListSerializer(serializers.ModelSerializer):
    """SongGenreListSerializer"""
    genre__name = serializers.ReadOnlyField()

    class Meta:
        model = SongGenre
        fields = ['genre_id', 'genre__name']


class SongLikeSerializer(serializers.ModelSerializer):
    """SongLikeSerializer"""
    class Meta:
        model = SongLike
        fields = '__all__'


class SongLikeListSerializer(serializers.ModelSerializer):
    """SongLikeListSerializer"""
    user__username = serializers.ReadOnlyField()

    class Meta:
        model = SongLike
        fields = ['user_id', 'user__username']


class SongSerializer(serializers.ModelSerializer):
    """SongSerializer"""

    class Meta:
        model = Song
        fields = '__all__'


class SongListSerializer(serializers.ModelSerializer):
    """SongListSerializer"""
    # user = serializers.SerializerMethodField('id')

    user__username = serializers.ReadOnlyField()
    author__name = serializers.ReadOnlyField()

    class Meta:
        model = Song
        fields = [
            'id',
            'user_id',
            'user__username',
            'author_id',
            'author__name',
            'title',
            'text_with_accords',
            'date_creation',
            'link'
        ]


class SongShortSerializer(serializers.ModelSerializer):
    """SongShortSerializer"""
    author__name = serializers.ReadOnlyField()

    class Meta:
        model = Song
        fields = [
            'id',
            'user_id',
            'author_id',
            'author__name',
            'title',
            'date_creation',
            'link'
        ]
        read_only_fields = ('author_id', 'author__name')
