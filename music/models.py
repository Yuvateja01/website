from django.db import models
from django.urls import reverse


# Create your models here.
class Album(models.Model):
    albumname = models.CharField(max_length=1000)
    artist = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    albumlogo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse("music:details", kwargs={'pk', self.pk})

    def __str__(self):
        return self.albumname + "-" + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    songtitle = models.CharField(max_length=1000)
    filetype = models.CharField(max_length=1000)
    isfavourite = models.BooleanField(default=False)

    def __str__(self):
        return self.songtitle
