from __future__ import unicode_literals

import json

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FbUser(BaseModel):
    fbid = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.CharField(max_length=100, blank=True, null=True)
    locale = models.CharField(max_length=100, blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    yt_access_token = models.CharField(max_length=1000, blank=True, null=True)
    yt_refresh_token = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.first_name+":"+self.last_name)

    def userstate(self):
        state = json.loads(self.state)['current_state']
        return state

    def setstate(self, state_code):
        state = self
        state_data = json.loads(state.state)
        state_data['current_state'] = state_code
        state.state = json.dumps(state_data)
        state.save()


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
