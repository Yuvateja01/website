from django.db import models

# Create your models here.
class Album(models.Model):
    albumname=models.CharField(max_length=1000)
    artist=models.CharField(max_length=1000)
    genre=models.CharField(max_length=1000)
    albumlogo=models.CharField(max_length=1000)

    def __str__(self):
        return self.albumname+"-"+self.artist


class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    songtitle=models.CharField(max_length=1000)
    filetype=models.CharField(max_length=1000)
    isfavourite=models.BooleanField(default="false")
    def __str__(self):
        return self.songtitle