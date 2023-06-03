""" user part"""
from django.db import models


class User (models.Model):
    """ user """

    user_id = models.BigAutoField(
        primary_key=True,
        db_column='user_id',
    )

    username = models.CharField(
        max_length=40,
        unique=True,
    )

    password = models.CharField(
        max_length=40,
    )

    public_info = models.CharField(
        max_length=1000,
        blank=True,
        default=''
    )

    date_creation = models.DateTimeField(
        null=False,
        blank=True,
        auto_now_add=True
    )

    def __str__(self):
        return str(self.username)
