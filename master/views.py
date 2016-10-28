import json
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import requests
from django.views.decorators.csrf import csrf_exempt
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
access_token = "EAARqIqseANoBAOjI9MeAmHXDgDrAy5PuVmCEizRZC38B3baTd8NW9JgZBvwxCaLwb9CBUB22XRvwffPia3wWUZBJ3M4nj2pXbQeh3J3JuZALgn3CsZCvwDUtAwuSSsYE0dYKJH3wOEk7HEz3ZCVW1hxsi3pVzpbTF4bhiyTCga2gZDZD"


@csrf_exempt
def fbwebhook(request):

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
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events

                fbid = message['sender']['id']
                timeOfmessage = message['timestamp']

                if 'message' in message:
                    messageReceived(message)

                elif 'read' in message:
                    pass
                    # print "read message"
                    # sendTextMessage(fbid, "read")
                elif 'delivery' in message:
                    pass
                    # print "delivery message"
                    # sendTextMessage(fbid, "delivery")
                elif 'postback' in message:
                    print "postback message"
                    sendTextMessage(fbid, "postback received")
                elif 'optin' in message:
                    print "optin message"
                    sendTextMessage(fbid, "optin")
                elif 'account_linking' in message:
                    print "account_linking message"
                    sendTextMessage(fbid, "account linking")
                else:
                    print "Webhook received unknown messagingEvent: "
                    print message
                    sendTextMessage(fbid, "unknown webhook")

        return HttpResponse('', content_type='application/json')


def call_send_api(message_data):
    print "send api called"
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+access_token
    message_data = json.dumps(message_data)
    # response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": recevied_message}})

    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=message_data)
    print status.json()


def sendImageMessage(fbid):
    print "send image message"
    messageData = {
        'recipient': {
            'id': fbid
        },
        'message': {
            'attachment': {
                'type': "image",
                'payload': {
                    'url': "http://messengerdemo.parseapp.com/img/rift.png"
                }
            }
        }
    }
    call_send_api(messageData)


def sendGifMessage(fbid):
    pass


def sendAudioMessage(fbid):
    pass


def sendVideoMessage(fbid):
    pass


def sendFileMessage(fbid):
    pass


def sendButtonMessage(fbid):

    messageData = {
        'recipient': {
            'id': fbid
        },
        'message': {
            'attachment': {
                'type': "template",
                'payload': {
                    'template_type': "button",
                    'text': "This is test text",
                    'buttons': [{
                        'type': "web_url",
                        'url': "https://www.oculus.com/en-us/rift/",
                        'title': "Open Web URL"
                    }, {
                        'type': "postback",
                        'title': "Trigger Postback",
                        'payload': "DEVELOPED_DEFINED_PAYLOAD"
                    }, {
                        'type': "phone_number",
                        'title': "Call Phone Number",
                        'payload': "+917022167044"
                    }]
                }
            }
        }
    }

    call_send_api(messageData);


def sendGenericMessage(fbid):
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
                        'title': "Bruno Mars - 24K Magic [Official Video]",
                        'subtitle': "Bruno Mars",
                        'item_url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                        'image_url': "https://i.ytimg.com/vi/UqyT8IEBkvY/mqdefault.jpg",
                        'buttons': [{
                            'type': "web_url",
                            'url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                            'title': "Open Video"
                        }, {
                            'type': "postback",
                            'title': "Call Postback",
                            'payload': "Payload for first bubble",
                        }],
                    },
                        {
                            'title': "Bruno Mars - 24K Magic [Official Video]",
                            'subtitle': "Bruno Mars",
                            'item_url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                            'image_url': "https://i.ytimg.com/vi/UqyT8IEBkvY/mqdefault.jpg",
                            'buttons': [{
                                'type': "web_url",
                                'url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                                'title': "Open Video"
                            }, {
                                'type': "postback",
                                'title': "Call Postback",
                                'payload': "Payload for first bubble",
                            }],
                        },
                        {
                        'title': "Bruno Mars - 24K Magic [Official Video]",
                        'subtitle': "Bruno Mars",
                        'item_url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                        'image_url': "https://i.ytimg.com/vi/UqyT8IEBkvY/mqdefault.jpg",
                        'buttons': [{
                            'type': "web_url",
                            'url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                            'title': "Open Video"
                        }, {
                            'type': "postback",
                            'title': "Call Postback",
                            'payload': "Payload for first bubble",
                        }],
                    },
                        {
                            'title': "Bruno Mars - 24K Magic [Official Video]",
                            'subtitle': "Bruno Mars",
                            'item_url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                            'image_url': "https://i.ytimg.com/vi/UqyT8IEBkvY/mqdefault.jpg",
                            'buttons': [{
                                'type': "web_url",
                                'url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                                'title': "Open Video"
                            }, {
                                'type': "postback",
                                'title': "Call Postback",
                                'payload': "Payload for first bubble",
                            }],
                        },
                        {
                            'title': "Bruno Mars - 24K Magic [Official Video]",
                            'subtitle': "Bruno Mars",
                            'item_url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                            'image_url': "https://i.ytimg.com/vi/UqyT8IEBkvY/mqdefault.jpg",
                            'buttons': [{
                                'type': "web_url",
                                'url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                                'title': "Open Video"
                            }, {
                                'type': "postback",
                                'title': "Call Postback",
                                'payload': "Payload for first bubble",
                            }],
                        },
                        {
                            'title': "Bruno Mars - 24K Magic [Official Video]",
                            'subtitle': "Bruno Mars",
                            'item_url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                            'image_url': "https://i.ytimg.com/vi/UqyT8IEBkvY/mqdefault.jpg",
                            'buttons': [{
                                'type': "web_url",
                                'url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                                'title': "Open Video"
                            }, {
                                'type': "postback",
                                'title': "Call Postback",
                                'payload': "Payload for first bubble",
                            }],
                        },
                        {
                            'title': "Bruno Mars - 24K Magic [Official Video]",
                            'subtitle': "Bruno Mars",
                            'item_url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                            'image_url': "https://i.ytimg.com/vi/UqyT8IEBkvY/mqdefault.jpg",
                            'buttons': [{
                                'type': "web_url",
                                'url': "https://www.youtube.com/watch?v=UqyT8IEBkvY",
                                'title': "Open Video"
                            }, {
                                'type': "postback",
                                'title': "Call Postback",
                                'payload': "Payload for first bubble",
                            }],
                        },
                    ]
                }
            }
        }
    }

    call_send_api(messageData)


def sendQuickReply(fbid):

    messageData = {
        'recipient': {
            'id': fbid
        },
        'message': {
            'text': "What's your favorite movie genre?",
            'quick_replies': [
                {
                    "content_type": "text",
                    "title": "Action",
                    "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_ACTION"
                },
                {
                    "content_type": "text",
                    "title": "Comedy",
                    "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_COMEDY"
                },
                {
                    "content_type": "text",
                    "title": "Drama",
                    "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_DRAMA"
                }
            ]
        }
    }

    call_send_api(messageData)


def sendReadReceipt(fbid):
    messageData = {
        'recipient': {
            'id': fbid
        },
        'sender_action': "mark_seen"
    }

    call_send_api(messageData)


def sendTypingOn(fbid):
    messageData = {
        'recipient': {
            'id': fbid
        },
        'sender_action': "typing_on"
    }

    call_send_api(messageData)


def messageReceived(event):
    message = event.get('message')
    senderId = event['sender']['id']
    recipientId = event['recipient']['id']
    isEcho = message.get('is_echo')
    # messageId = message['mid']
    # appId = message['app_id']
    # metadata = message['metadata']

    messageText = message.get('text')
    messageAttachment = message.get('attachment')
    quickReply = message.get('quick_reply')

    fbid = senderId

    if isEcho:
        print "echo"
        fbid = recipientId
        return True
    elif quickReply:
        sendTextMessage(fbid, "Quick Reply Tapped")
        return True

    get_fb_user_datails(fbid)

    if messageText:
        if 'image' in messageText:
            sendImageMessage(fbid)
        elif 'gif' in messageText:
            sendGifMessage(fbid)
        elif 'audio' in messageText:
            sendAudioMessage(fbid)
        elif 'video' in messageText:
            sendVideoMessage(fbid)
        elif 'file' in messageText:
            sendFileMessage(fbid)
        elif 'button' in messageText:
            sendButtonMessage(fbid)
        elif 'generic' in messageText:
            sendGenericMessage(fbid)
        elif 'quick reply' in messageText:
            sendQuickReply(fbid)
        elif 'read receipt' in messageText:
            sendReadReceipt(fbid)
        elif 'typing on' in messageText:
            sendTypingOn(fbid)
        else:
            sendTextMessage(fbid, messageText)
    elif messageAttachment:
        sendTextMessage(fbid, "message with attachment received")

    return True





def get_fb_user_datails(fbid):
    full_url = "https://graph.facebook.com/v2.6/%s?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=%s"%(fbid, access_token)

    user_details = requests.get(full_url).json()
    print "-----", fbid, user_details.get('first_name')


def sendTextMessage(fbid, recevied_message):
    print "pppppppppp"
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+access_token

    response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": recevied_message}})

    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    print status.json()




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
