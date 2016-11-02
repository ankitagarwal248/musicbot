import json

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from master.utils import youtubeutils
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests.packages.urllib3
from master.models import *

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def fill_data(videos_data):
    # vid = str(vid)
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('musicfeed-ba115ff06741.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("youtubedata").sheet1

    for vid_data in videos_data:
        title = vid_data['title']
        vid_url = vid_data['url']
        thumbnail = vid_data['thumbnail']
        channeltitle = vid_data['channeltitle']
        viewcount = int(vid_data['viewcount'])
        likecount = int(vid_data['likecount'])
        dislikecount = int(vid_data['dislikecount'])
        favcount = int(vid_data['favcount'])
        commentcount = int(vid_data['commentcount'])

        data = [title, vid_url, channeltitle, viewcount, likecount, dislikecount, favcount, commentcount]
        wks.append_row(data)
        print "--"
    return True


def fill_mix_data(vid):
    mix_vid_ids = youtubeutils.get_related_videos_from_mix_playlist(vid)
    for vid in mix_vid_ids:
        try:
            fill_data(vid)
        except Exception as e:
            print str(e)


def fill_yt_details_db_none():
    songs = Song.objects.filter(yt_details=None)
    while songs:
        songs = songs[:40]
        song_ids = map(lambda x: x.yt_id, songs)
        videos_data = youtubeutils.get_video_data(song_ids)
        print len(songs), len(videos_data)
        for v in videos_data:
            video_details = json.dumps(v)
            song_id = v['id']
            song = Song.objects.get(yt_id=song_id)
            song.yt_details = video_details
            song.save()
        songs = Song.objects.filter(yt_details=None)


def fill_yt_details_db_all():
    songs = Song.objects.all()
    while songs:
        songs = songs[:40]
        song_ids = map(lambda x: x.yt_id, songs)
        videos_data = youtubeutils.get_video_data(song_ids)
        print len(songs), len(videos_data)
        for v in videos_data:
            video_details = json.dumps(v)
            song_id = v['id']
            song = Song.objects.get(yt_id=song_id)
            song.yt_details = video_details
            song.save()
        songs = Song.objects.all()
