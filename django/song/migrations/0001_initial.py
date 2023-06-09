# Generated by Django 4.2.1 on 2023-07-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accords",
            fields=[
                (
                    "accord_id",
                    models.BigAutoField(
                        db_column="accord_id", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=40, unique=True)),
                (
                    "link",
                    models.URLField(blank=True, default="", max_length=400, null=True),
                ),
                ("short_name", models.CharField(max_length=6, unique=True)),
            ],
            options={
                "verbose_name_plural": "Accords",
            },
        ),
        migrations.CreateModel(
            name="Authors",
            fields=[
                (
                    "author_id",
                    models.BigAutoField(
                        db_column="author_id", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "link",
                    models.URLField(blank=True, default="", max_length=400, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "Authors",
            },
        ),
        migrations.CreateModel(
            name="Genres",
            fields=[
                (
                    "genre_id",
                    models.BigAutoField(
                        db_column="genre_id", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=20, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=300, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "Genres",
            },
        ),
        migrations.CreateModel(
            name="SongGenres",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Song genres",
            },
        ),
        migrations.CreateModel(
            name="SongLikes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Song likes",
            },
        ),
        migrations.CreateModel(
            name="Songs",
            fields=[
                (
                    "song_id",
                    models.BigAutoField(
                        db_column="song_id", primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "link",
                    models.URLField(blank=True, default="", max_length=400, null=True),
                ),
                (
                    "text_with_accords",
                    models.TextField(
                        blank=True, default="", max_length=10000, null=True
                    ),
                ),
                (
                    "author_id",
                    models.ForeignKey(
                        db_column="author_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="song.authors",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Songs",
            },
        ),
    ]
