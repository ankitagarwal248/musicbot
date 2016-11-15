import json
from django.conf import settings
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
import requests
from django.views.decorators.csrf import csrf_exempt
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests.packages.urllib3

from master.utils import bot_sample_calls
from master.utils import botcalls
from master.utils import credentials
from master.utils.bot_sample_calls import sendText
from master.models import *
from oauth2client import client


requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@csrf_exempt
def fbwebhook(request):
    print "fbwehook called"

    if request.method == 'GET':
        if request.GET['hub.verify_token'] == credentials.fb_hook_verify_token:
            return HttpResponse(request.GET['hub.challenge'], content_type='application/json')
        else:
            return HttpResponse('Error, wrong validation token', content_type='application/json')

    if request.method == 'POST':
        incoming_message = json.loads(request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            pageId = entry['id']
            timeOfEvent = entry['time']

            for message in entry['messaging']:
                fbid = message['sender']['id']
                timeOfmessage = message['timestamp']

                if 'message' in message:
                    botcalls.messageReceived(message)

                elif 'read' in message:
                    pass

                elif 'delivery' in message:
                    pass

                elif 'postback' in message:
                    botcalls.postbackReceived(message)

                elif 'optin' in message:
                    sendText(fbid, "optin")

                elif 'account_linking' in message:
                    sendText(fbid, "account linking")

                else:
                    print "Webhook received unknown messagingEvent: "
                    sendText(fbid, "unknown webhook")

        return HttpResponse('', content_type='application/json')


def home(request):

    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        numbooks = request.POST.get('numbooks')

        key = settings.MAILGUN_KEY
        recipient = [
            'ankitagarwal24.8@gmail.com',
            'tpurohit91@gmail.com'
        ]
        from_ = settings.SENDER_EMAIL_ID
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'city': city,
            'numbooks': numbooks
        }
        html = render_to_string("master/email.html", context)

        request_url = settings.REQUEST_URL
        requests.post(request_url, auth=('api', key), data={
            'from': from_,
            'to': recipient,
            'subject': 'Bookworm Registration',
            "html": html,
        })

    return render(request, 'master/home.html', {})


def download_url(request):
    vid = request.GET.get('vid')
    data = {
        'vid': vid
    }
    return render(request, 'master/home.html', data)


def googleoauth2callback(request):
    auth_code = request.GET.get('code')
    if auth_code:
        data = {'code': auth_code,
                'client_id': credentials.CLIENT_ID,
                'client_secret': credentials.CLIENT_SECRET,
                'redirect_uri': credentials.REDIRECT_URI,
                'grant_type': 'authorization_code',
                }
        r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data).json()

        access_token = r.get("access_token")
        refresh_token = r.get("refresh_token")
        fbid = request.GET.get('state').replace("fbid", "")

        fbuser = FbUser.objects.get(fbid=fbid)
        fbuser.yt_access_token = access_token
        fbuser.yt_refresh_token = refresh_token
        fbuser.save()
        botcalls.send_after_registration_messages(fbuser)

        # return HttpResponseRedirect("/google_auth_success")

        return HttpResponse("Thanks for the registration, you can now go back to the messanger. Thanks!")
    return HttpResponse("can't find oauth code!!")


def google_auth_success(request):
    return HttpResponseRedirect("https://m.me/musicfeedbot")
