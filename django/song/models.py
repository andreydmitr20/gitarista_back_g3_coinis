""" song part """
from django.db import models

from django.contrib import admin

from user.models import Users


class Genres(models.Model):
    """ genres """

    genre_id = models.BigAutoField(
        primary_key=True,
        # default=0,
        db_column='genre_id'
    )
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=True,
    )

    description = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        default=''
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Genres"


class Authors(models.Model):
    """ authors """

    author_id = models.BigAutoField(
        primary_key=True,
        # default=0,
        db_column='author_id'
    )

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    link = models.URLField(
        max_length=400,
        null=True,
        blank=True,
        default=''
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Authors"


class Songs (models.Model):
    """ songs  """

    song_id = models.BigAutoField(
        primary_key=True,
        # default=0,
        db_column='song_id'
    )

    user_id = models.ForeignKey(
        Users,
        db_column='user_id',
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    author_id = models.ForeignKey(
        Authors,
        db_column='author_id',
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    date_creation = models.DateTimeField(
        null=False,
        blank=True,
        auto_now_add=True
    )

    link = models.URLField(
        max_length=400,
        null=True,
        blank=True,
        default=''
    )

    text_with_accords = models.TextField(
        max_length=10000,
        null=True,
        blank=True,
        default=''
    )

    @admin.display(ordering='song_author', description='Song author')
    def get_author(self):
        """ get_song_title"""
        return self.author_id.name

    @admin.display(ordering='user_username', description='User who created')
    def get_username(self):
        """get_username"""
        return self.user_id.username

    def __str__(self):
        return str(self.author_id.name)+(' - ')+str(self.title)

    class Meta:
        # verbose_name = "Song"
        verbose_name_plural = "Songs"


class SongGenres(models.Model):
    """ genres of certain song """

    song_id = models.ForeignKey(
        Songs,
        db_column='song_id',
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    genre_id = models.ForeignKey(
        Genres,
        db_column='genre_id',
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        unique_together = [['song_id', 'genre_id']]
        verbose_name_plural = "Song genres"

    @admin.display(ordering='song_title', description='Song title')
    def get_song_title(self):
        """ get_song_title"""
        return self.song_id.title

    @admin.display(ordering='song_genre', description='Song genre')
    def get_song_genre(self):
        """get_song_genre"""
        return self.genre_id.name

    def __str__(self):
        return str(self.genre_id.name)+' genre '+str(self.song_id.title)


class SongLikes(models.Model):
    """ likes from users """

    song_id = models.ForeignKey(
        Songs,
        db_column='song_id',
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    user_id = models.ForeignKey(
        Users,
        db_column='user_id',
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        unique_together = [['song_id', 'user_id']]
        verbose_name_plural = "Song likes"

    @admin.display(ordering='song_title', description='Song title')
    def get_song_title(self):
        """ get_song_title"""
        return self.song_id.title

    @admin.display(ordering='user_username', description='User who likes')
    def get_username(self):
        """get_username"""
        return self.user_id.username

    def __str__(self):
        return str(self.user_id.username)+' likes '+str(self.song_id.title)


class Accords(models.Model):
    """ accords """
    accord_id = models.BigAutoField(
        primary_key=True,
        db_column='accord_id',
        # default=0
    )
    name = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        unique=True,
    )

    link = models.URLField(
        max_length=400,
        null=True,
        blank=True,
        default=''
    )

    short_name = models.CharField(
        max_length=6,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return str(self.short_name)+'( '+str(self.name)+' )'

    class Meta:
        verbose_name_plural = "Accords"
