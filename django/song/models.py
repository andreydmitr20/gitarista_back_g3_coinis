""" song part """
from django.db import models

from django.contrib import admin

from user.models import User


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

    def fill(self):
        """ fill model with choices"""

        for key, value in self.choices.items():
            genre = Genres(
                genre_id=key,
                name=value[0],
                description=value[1])
            genre.save()

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
        User,
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
        User,
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
