import json
from master.models import *
import pafy
import requests


access_token = "EAARqIqseANoBAOjI9MeAmHXDgDrAy5PuVmCEizRZC38B3baTd8NW9JgZBvwxCaLwb9CBUB22XRvwffPia3wWUZBJ3M4nj2pXbQeh3J3JuZALgn3CsZCvwDUtAwuSSsYE0dYKJH3wOEk7HEz3ZCVW1hxsi3pVzpbTF4bhiyTCga2gZDZD"


def send_generic_download_message(fbid, data):

    yt_title = data['title']
    yt_subtitle = data['subtitle']
    yt_url = data['yt_url']
    image_url = data['image_url']
    download_url = data['download_url']

    messageData = {
        'recipient': {
            'id': fbid
        },
        'message': {
            'attachment': {
                'type': "template",
                'payload': {
                    'template_type': "generic",
                    'elements': [
                        {
                        'title': yt_title,
                        'subtitle': yt_subtitle,
                        'item_url': yt_url,
                        'image_url': image_url,
                        'buttons': [
                            {
                                'type': "web_url",
                                'url': yt_url,
                                'title': "Open Video"
                            },
                            {
                                "type": "web_url",
                                "url": download_url,
                                "title": "Download MP3",
                                "webview_height_ratio": "compact"
                            },
                        ],
                    },
                    ]
                }
            }
        }
    }

    call_send_api(messageData)


def send_youtube_download_link(fbid):
    vid = "PT2_F-1esPk"
    download_url = "https://faae45a0.ngrok.io/download_url/?vid="+vid
    yt_url = "https://www.youtube.com/watch?v="+vid
    video = pafy.new(yt_url)

    data = {}
    data['title'] = video.title
    data['subtitle'] = video.author
    data['yt_url'] = yt_url
    data['image_url'] = video.bigthumb
    data['download_url'] = download_url
    send_generic_download_message(fbid, data)


def call_send_api(message_data):
    print "send api called"
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+access_token
    message_data = json.dumps(message_data)

    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=message_data)


def get_fb_user_details(fbid):
    print "get_fb_user_details called"
    full_url = "https://graph.facebook.com/v2.6/%s?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=%s"%(fbid, access_token)

    user_details = requests.get(full_url).json()
    data = {}
    data['first_name'] = user_details.get('first_name')
    data['last_name'] = user_details.get('last_name')
    data['profile_pic'] = user_details.get('profile_pic')
    data['locale'] = user_details.get('locale')
    data['timezone'] = user_details.get('timezone')
    data['gender'] = user_details.get('gender')
    return data


def create_find_fb_user(fbid):
    print "create_find_fb_user called"
    fbuser = FbUser.objects.filter(fbid=fbid)
    if fbuser:
        fbuser = fbuser[0]
    else:
        data = get_fb_user_details(fbid)
        fbuser = FbUser(fbid=fbid,
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        profile_pic=data['profile_pic'],
                        locale=data['locale'],
                        timezone=data['timezone'],
                        gender=data['gender']
                        )
        fbuser.save()

    return fbuser