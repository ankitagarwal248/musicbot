from django.conf import settings

ENV = settings.ENV
BASE_URL = ""

if ENV == 'local':

    BASE_URL = "https://81a21b6e.ngrok.io/"
    fb_access_token = "EAAYIkWuA6c0BABPgDwaRwnaJso5WzKY9AQxixjrjz8h0eKzRMpifBS072CtQ4p8uTkSKxQk2Bsuho1X5P8KODDlHXNsYB9iqYosYjxygw3qpIOIckHi5DtkNLBbZABWYjOd4ZCT6aFEMvd1lGZCnKr49BIcQ2H8Tl68ZCnUavAZDZD"

elif (ENV == 'staging') or (ENV == 'production'):

    BASE_URL = "https://bookwormindia.herokuapp.com/"
    fb_access_token = "EAARqIqseANoBAOjI9MeAmHXDgDrAy5PuVmCEizRZC38B3baTd8NW9JgZBvwxCaLwb9CBUB22XRvwffPia3wWUZBJ3M4nj2pXbQeh3J3JuZALgn3CsZCvwDUtAwuSSsYE0dYKJH3wOEk7HEz3ZCVW1hxsi3pVzpbTF4bhiyTCga2gZDZD"


# google credentials
CLIENT_ID = '507175992320-br2pubjd7u0q7q9js6s6tq2dteidnorj.apps.googleusercontent.com'
CLIENT_SECRET = 'HkVG1_P8i-xhkUrS02yaeaMP'
SCOPE = 'https://www.googleapis.com/auth/youtube'
REDIRECT_URI = BASE_URL + 'googleoauth2callback'

# fb credentials
fb_hook_verify_token = "123456789"
