from __future__ import unicode_literals
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Song(BaseModel):
    yt_id = models.CharField(max_length=100, unique=True)
    yt_title = models.CharField(max_length=100, blank=True, null=True)
    yt_thumbnail = models.CharField(max_length=100, blank=True, null=True)
    yt_details = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.yt_title)

    def yt_url(self):
        return "https://www.youtube.com/watch?v="+self.yt_id


class BillBoard(BaseModel):
    song = models.ForeignKey(Song, blank=True, null=True, on_delete=models.SET_NULL)
    week = models.CharField(max_length=100)
    rank = models.IntegerField()
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.artist + " - " + self.name)
