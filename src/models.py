from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from user.models import *

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_year = models.PositiveIntegerField()

    authors = models.ManyToManyField(
        Author,
        related_name='books'
    )

    genres = models.ManyToManyField(
        Genre,
        related_name='books'
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} → {self.book.title}"