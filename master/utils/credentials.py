from django.conf import settings

ENV = settings.ENV
BASE_URL = ""

if ENV == 'local':

    BASE_URL = "https://0c6baaef.ngrok.io/"
    fb_access_token = "EAAYIkWuA6c0BAG1T1sdnU6QsCL4Sn3PIDasxNOPI7wdSTjTMZARucWiJEjt0Vv7VZBOY4PcainZC0xcIvpxcPc9Y88tSw33nkBoNuUWYJLu0eoYN3HTSfE71RpZBejZBiuiISr0g4sjZBXlBNVCJqjZBiZBZCF7blY4UqZCVexL10fSgZDZD"

elif (ENV == 'staging') or (ENV == 'production'):

    BASE_URL = "https://bookwormindia.herokuapp.com"
    fb_access_token = "EAARqIqseANoBAOjI9MeAmHXDgDrAy5PuVmCEizRZC38B3baTd8NW9JgZBvwxCaLwb9CBUB22XRvwffPia3wWUZBJ3M4nj2pXbQeh3J3JuZALgn3CsZCvwDUtAwuSSsYE0dYKJH3wOEk7HEz3ZCVW1hxsi3pVzpbTF4bhiyTCga2gZDZD"


# google credentials
CLIENT_ID = '507175992320-br2pubjd7u0q7q9js6s6tq2dteidnorj.apps.googleusercontent.com'
CLIENT_SECRET = 'HkVG1_P8i-xhkUrS02yaeaMP'
SCOPE = 'https://www.googleapis.com/auth/youtube'
REDIRECT_URI = BASE_URL + 'googleoauth2callback'

# fb credentials
fb_hook_verify_token = "123456789"
