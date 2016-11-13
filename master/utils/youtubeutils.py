from urlparse import parse_qs
from urlparse import urlparse

import bs4
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
google_api_key = "AIzaSyCi3xrwwx3kB1POO4AVJPeWJQ95Q1ACuM8"


def get_video_data(vids):

    vid = ""
    for i in vids:
        vid = vid + i + ","

    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "id": vid,
        "key": google_api_key,
        "part": "snippet,contentDetails,statistics,status",
    }

    video_info = requests.get(url, params=params).json()
    items = video_info['items']

    videos_data = []

    for item in items:
        snippet = item.get('snippet')
        video_id = item.get('id')
        content_details = item.get('contentDetails')
        statistics = item.get('statistics')
        viewCount = statistics.get('viewCount', '0')
        likeCount = statistics.get('likeCount', '0')
        dislikeCount = statistics.get('dislikeCount', '0')
        favoriteCount = statistics.get('favoriteCount', '0')
        commentCount = statistics.get('commentCount', '0')

        title = snippet['title']
        thumbnail = snippet['thumbnails']['medium']['url']
        channelTitle = snippet['channelTitle']
        video_url = 'https://www.youtube.com/watch?v='+video_id

        data = {
            'id': video_id,
            'title': title,
            'url': video_url,
            'thumbnail': thumbnail,
            'channeltitle': channelTitle,
            'viewcount': viewCount,
            'likecount': likeCount,
            'dislikecount': dislikeCount,
            'favcount': favoriteCount,
            'commentcount': commentCount,
        }
        videos_data.append(data)

    return videos_data


def get_mix_playlist(vid):

    response = requests.get("https://www.youtube.com/watch", params={"v": vid})
    bs = bs4.BeautifulSoup(response.content)
    items = bs.select("a.mix-playlist")
    if len(items) != 1:
        return None
    else:
        url = parse_qs(urlparse(items[0]['href']).query)
        return url['list'][0]


def playlist_items(pid):
    url = "https://www.googleapis.com/youtube/v3/playlistItems"

    params = {
        'part': 'snippet',
        'maxResults': "50",
        'playlistId': pid,
        'key': google_api_key,
    }

    playlist_items = requests.get(url, params=params).json()['items']
    video_ids = []
    video_names = []
    for item in playlist_items:
        vid = item['snippet']['resourceId']['videoId']
        title = item['snippet']['title']
        video_ids.append(vid)
        video_names.append(title)

    print video_ids
    for i in video_names:
        print i

    return video_ids


def search_youtube_video(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'videoCategoryId': '10',
        'maxResults': '1',
        'key': google_api_key,
    }

    video = requests.get(url, params=params).json()['items'][0]
    vid = video['id']['videoId']
    title = video['snippet']['title']
    thumbnail = video['snippet']['thumbnails']['medium']['url']

    data = {
        'vid': vid,
        'title': title,
        'thumbnail': thumbnail
    }
    return data


def get_related_videos(vid):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'maxResults': '50',
        'relatedToVideoId': vid,
        'type': 'video',
        'videoCategoryId': '10',
        'key': google_api_key,
    }

    related_videos = requests.get(url, params=params).json()
    items = related_videos['items']

    video_ids = []
    video_names = []
    for item in items:
        vid = item['id']['videoId']
        video_ids.append(vid)

        title = item['snippet']['title']+ " -- " +  item['snippet']['channelTitle']
        video_names.append(title)

    print video_ids
    for i in video_names:
        print i

    return video_ids


def get_related_videos_from_mix_playlist(vid):
    playlist_id = get_mix_playlist(vid)
    playlist_video_ids = playlist_items(playlist_id)
    return playlist_video_ids


def search_youtube_videos(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'videoCategoryId': '10',
        'maxResults': '5',
        'key': google_api_key,
    }

    data = []
    videos = requests.get(url, params=params).json()['items']
    for video in videos:
        vid = video['id']['videoId']
        title = video['snippet']['title']
        thumbnail = video['snippet']['thumbnails']['medium']['url']
        channeltitle = video['snippet']['channelTitle']

        vid_data = {
            'vid': vid,
            'title': title,
            'thumbnail': thumbnail,
            'channeltitle': channeltitle
        }
        data.append(vid_data)

    return data