import json
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import requests
from django.views.decorators.csrf import csrf_exempt
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests.packages.urllib3
from master.utils import botcalls
from master.utils.bot_sample_calls import sendText

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@csrf_exempt
def fbwebhook(request):
    print "fbwehook called"

    if request.method == 'GET':
        if request.GET['hub.verify_token'] == '123456789':
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
                    sendText(fbid, "postback received")

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