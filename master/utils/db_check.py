import gspread
from oauth2client.service_account import ServiceAccountCredentials

from master.models import *
import json


def songs_no_likes():
    songs = Song.objects.all()

    for s in songs:
        details = json.loads(s.yt_details)
        likes = details['likecount']
        if likes == '0':
            print details['id'], details['title']


def song_fill_drive():

    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('musicfeed-ba115ff06741.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("youtubedata").worksheet('Sheet3')

    all_data = []

    songs = Song.objects.all()
    length_songs = songs.count()
    for index, s in enumerate(songs):
        bb_songs = BillBoard.objects.filter(song=s)
        s_count_in_bb = bb_songs.count()
        s_highest_rank = min(map(lambda x: x.rank, bb_songs))
        details = json.loads(s.yt_details)

        title = details['title']
        url = details['url']
        channeltitle = details['channeltitle']
        viewcount = int(details['viewcount'])
        likecount = int(details['likecount'])
        dislikecount = int(details['dislikecount'])
        commentcount = int(details['commentcount'])

        data = [title, url, channeltitle, s_count_in_bb, s_highest_rank, viewcount, likecount, dislikecount, commentcount]

        # wks.append_row(data)
        # print index, "/", length_songs

        all_data.append(data)

    all_data_flat = []
    for row_data in all_data:
        for cell_data in row_data:
            all_data_flat.append(cell_data)

    num_cols = len(all_data[0])
    char_num_col = chr(64 + num_cols)

    num_filled_rows = wks.row_count
    rows_to_add = len(all_data)
    wks.add_rows(rows_to_add)

    range_start = 'A' + str(num_filled_rows + 1)
    range_end = char_num_col + str(num_filled_rows + rows_to_add)
    new_range = range_start + ':' + range_end

    cell_list = wks.range(new_range)
    for index, cell in enumerate(cell_list):
        cell.value = all_data_flat[index]

    wks.update_cells(cell_list)

    return True
