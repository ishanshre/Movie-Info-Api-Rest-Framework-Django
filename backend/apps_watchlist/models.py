from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True,blank=True, null=True)
    active = models.BooleanField(default=True,blank=True, null=True)
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
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist', blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.rating