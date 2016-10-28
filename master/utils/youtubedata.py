import gspread
from oauth2client.service_account import ServiceAccountCredentials
from master.utils import youtubeutils
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def fill_data(vid):
    vid = str(vid)
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('musicfeed-ba115ff06741.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("youtubedata").sheet1

    vid_data = youtubeutils.get_video_data(vid)

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
    return True


def fill_mix_data(vid):
    mix_vid_ids = youtubeutils.get_related_videos_from_mix_playlist(vid)
    for vid in mix_vid_ids:
        try:
            fill_data(vid)
        except Exception as e:
            print str(e)
