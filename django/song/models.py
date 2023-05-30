""" song part """
from django.db import models

from django.contrib import admin

from user.models import User


class Genre(models.Model):
    """ genre """

    choices = {
        0: ['Rock',
            'This genre encompasses various subgenres such as classic rock, hard rock, alternative rock, punk rock, and progressive rock. Guitar-driven bands and iconic guitar solos are a defining characteristic of rock music'],
        1: ['Blues',
            'Originating from African-American communities in the United States, blues music heavily relies on the guitar. It often features soulful playing, bending of notes, and expressive solos'],
        2: ['Jazz',
            'Jazz music incorporates improvisation and complex harmonies. The guitar plays a significant role in jazz, both as a rhythm instrument and for soloing. Subgenres like gypsy jazz and smooth jazz also have distinct guitar styles'],
        3: ['Country',
            'Country music often features acoustic and electric guitars, including fingerpicking and twangy guitar sounds. It encompasses subgenres like traditional country, country rock, and outlaw country'],
        4: ['Metal',
            'Known for its heavy sound, aggressive riffs, and fast guitar playing, metal music is characterized by distorted guitars and intricate solos. Subgenres like thrash metal, heavy metal, and power metal are all guitar-driven'],
        5: ['Folk',
            'Folk music utilizes acoustic guitars and often features storytelling through lyrics. Fingerpicking and strumming patterns are common techniques. Subgenres like contemporary folk and folk rock incorporate electric guitars as well'],
        6: ['Flamenco',
            'Originating in Spain, flamenco is a highly expressive and passionate genre that heavily relies on guitar playing. It combines intricate fingerpicking techniques with percussive elements'],
        7: ['Classical',
            'Classical music showcases the guitar as a solo instrument, featuring compositions by renowned composers like Fernando Sor and Johann Sebastian Bach. It requires fingerstyle playing and classical guitar techniques'],
        8: ['Funk',
            'Funk music is known for its tight rhythm sections and infectious grooves. The guitar typically plays a rhythmic role, providing syncopated chords and funky strumming patterns'],
        9: ['R&B/Soul',
            'Rhythm and blues and soul music often incorporate guitar as a foundational instrument, providing melodic and rhythmic elements. It can range from smooth and mellow to energetic and groovy'],
    }

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

    def fill(self):
        """ fill model with choices"""

        for key, value in self.choices.items():
            genre = Genre(
                id=key,
                name=value[0],
                description=value[1])
            genre.save()


class Author(models.Model):
    """ author """

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


class Song (models.Model):
    """ songs  """

    list_display = ('get_author', 'get_username')

    @admin.display(ordering='song__author', description='Song author')
    def get_author(self, obj):
        """ get_song_title"""
        return obj.author.name

    @admin.display(ordering='user__username', description='User who created')
    def get_username(self, obj):
        """get_username"""
        return obj.user.username

    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    author = models.ForeignKey(
        Author,
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

    def __str__(self):
        return str(self.user.username)+' added song '+str(self.title)+(' of author ')+str(self.author.name)


class SongGenre(models.Model):
    """ genres of certain song """

    list_display = ('get_song_title', 'get_song_genre')

    @admin.display(ordering='song__title', description='Song title')
    def get_song_title(self, obj):
        """ get_song_title"""
        return obj.song.title

    @admin.display(ordering='song__genre', description='Song genre')
    def get_song_genre(self, obj):
        """get_song_genre"""
        return obj.genre.name

    song = models.ForeignKey(
        Song,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    genre = models.ForeignKey(
        Genre,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return str(self.genre.name)+' genre '+str(self.song.title)


class SongLike(models.Model):
    """ likes from users """

    list_display = ('get_song_title', 'get_username')

    @admin.display(ordering='song__title', description='Song title')
    def get_song_title(self, obj):
        """ get_song_title"""
        return obj.song.title

    @admin.display(ordering='user__username', description='User likes song')
    def get_username(self, obj):
        """get_username"""
        return obj.user.username

    song = models.ForeignKey(
        Song,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return str(self.user.username)+' likes '+str(self.song.title)


class Accord(models.Model):
    """ accords """

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
