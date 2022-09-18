from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=500)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title