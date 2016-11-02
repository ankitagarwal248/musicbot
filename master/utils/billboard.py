import bs4
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests.packages.urllib3
from datetime import datetime, timedelta
from master.models import *

from master.utils import bb
from master.utils import youtubedata
from master.utils import youtubeutils

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_billboard_music():
    base_url = "http://www.billboard.com"
    path_url = "/charts/hot-100/"

    full_url = base_url+path_url
    response = requests.get(full_url)
    soup = bs4.BeautifulSoup(response.text)

    chart_week = soup.find('time')
    week = chart_week['datetime']

    divs = soup.find_all('div', class_="chart-row__primary")
    songs_data = []
    for div in divs:
        if div:
            div_rank = div.find('span', class_="chart-row__current-week")
            if div_rank:
                div = div.find('div', class_="chart-row__title")
                if div:
                    name = div.find('h2')
                    if name:
                        artist = div.find('a')
                        if artist:
                            rank = int(div_rank.text.strip())
                            name = name.text.strip()
                            artist = artist.text.strip()
                            song_data = {'rank': rank, 'name': name, 'artist': artist}

                            songs_data.append(song_data)

    print len(songs_data)
    for t in songs_data:
        print t['rank'], t['name']

    bb_data = {
        'week': week,
        'songs_data': songs_data
    }

    return bb_data


def youtube_ids(bb_songs_data):

    titles = []
    for song in bb_songs_data:
        title = song['artist'] + " - " + song['name']
        titles.append(title)

    vids = []
    for title in titles:
        video_data = youtubeutils.search_youtube_video(title)
        vid = video_data['vid']
        vids.append(vid)
        print len(vids), len(titles)

    return vids


def get_bb_youtube_data():
    bb = get_billboard_music()['song_data']
    # bb = remove_duplicate_bb_songs_already_in_db()
    bb_vids = youtube_ids(bb)

    print bb_vids

    # bb_40 = bb.bb_40
    # videos_data = youtubeutils.get_video_data(bb_40)
    # for v in videos_data:
    #     print v['title']
    #
    # print youtubedata.fill_data(videos_data)


def fill_bb_db():
    bb = get_billboard_music()
    week = bb['week']
    week = datetime.strptime(week, '%Y-%m-%d').date()
    songs_data = bb['songs_data']

    for song in songs_data:
        rank = song['rank']
        name = song['name']
        artist = song['artist']

        db_song = BillBoard.objects.filter(week=week, name=name, artist=artist)
        if not db_song:
            BillBoard(week=week, rank=rank, name=name, artist=artist).save()

        print rank, name, artist


def yt_ids_db_from_bb_db():
    bb_songs = BillBoard.objects.filter(song=None)
    for bb_song in bb_songs:
        bb_title = bb_song.artist + " - " + bb_song.name
        video_data = youtubeutils.search_youtube_video(bb_title)
        vid = video_data['vid']
        yt_title = video_data['title']
        yt_thumbnail = video_data['thumbnail']

        s = Song(yt_id=vid, yt_title=yt_title, yt_thumbnail=yt_thumbnail)
        s.save()
        bb_song.song = s
        bb_song.save()
        print s


def get_bb_week_dates():
    week_latest = get_billboard_music()['week']
    week_latest = datetime.strptime(week_latest, '%Y-%m-%d').date()
    last_50_weeks = []
    for r in range(50):
        previous_week = week_latest - timedelta(weeks=r)
        last_50_weeks.append(str(previous_week))

    for r in last_50_weeks:
        print r


