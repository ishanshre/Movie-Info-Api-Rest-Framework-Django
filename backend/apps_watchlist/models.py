from django.db import models

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    website = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class Watchlist(models.Model):

    class Type(models.TextChoices):
        TVSERIES = 'TV', 'TVSERIES'
        MOVIE = 'MV', 'MOVIE'
        PODCAST = 'PD', 'PODCAST'


    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=500)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.MOVIE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title