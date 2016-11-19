import json
from master.utils import bot_sample_calls
from master.utils import botutils
from master.utils import credentials
from master.utils import youtubeutils


def messageReceived(event):
    print "messageReceived called"
    message = event.get('message')
    senderId = event['sender']['id']
    recipientId = event['recipient']['id']
    isEcho = message.get('is_echo')
    # messageId = message['mid']
    # appId = message['app_id']
    # metadata = message['metadata']

    message_text = message.get('text')
    messageAttachment = message.get('attachment')
    quickReply = message.get('quick_reply')
    fbid = senderId

    if isEcho:
        print "echo"
        fbid = recipientId
        return True

    if messageAttachment:
        bot_sample_calls.sendText(fbid, "message with attachment received")

    fbuser = botutils.create_find_fb_user(fbid)
    userstate = fbuser.userstate()
    print fbuser, userstate

    if message_text:
        message_text = message_text.lower()
        if 'reset' in message_text:
            fbuser.setstate('p0')
            print "reset", fbuser.userstate()

    userstate = fbuser.userstate()
    if userstate == 'p0':
        send_p1(fbuser)
        return True

    if userstate == 'p1':
        page_response = check_response(message)
        if page_response:
            if page_response == 'r1':
                send_p2(fbuser)
            if page_response == 'r2':
                send_p3(fbuser)
        else:
            send_p1(fbuser)

        return True

    if userstate == 'p2':
        send_p4(fbuser, message)
        return True


def send_p4(fbuser, message):
    print "sendp4"
    message_text = message.get('text')
    bot_sample_calls.sendText(fbuser.fbid, "Search results")
    bot_sample_calls.sendTypingOn(fbuser.fbid)
    search_results = youtubeutils.search_youtube_videos(message_text)
    botutils.send_video_search_results(fbuser, search_results)
    # send_reset_quick_reply(fbuser)
    fbuser.setstate('p4')


def send_p2(fbuser):
    print "sendp2"
    bot_sample_calls.sendText(fbuser.fbid, "Type a song's name..")
    fbuser.setstate('p2')


def send_auth_link_btn(fbid):
    auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
                '&client_id={}&redirect_uri={}&scope={}&state=fbid{}'
                '&access_type=offline&prompt=consent').format(credentials.CLIENT_ID, credentials.REDIRECT_URI, credentials.SCOPE, fbid)

    messageData = {
        'recipient': {
            'id': fbid
        },
        'message': {
            'attachment': {
                'type': "template",
                'payload': {
                    'template_type': "button",
                    'text': "Authorise YouTube?",
                    'buttons': [
                        {
                            'type': "web_url",
                            'url': auth_uri,
                            'title': "Yes",
                        },
                        {
                            "type": "postback",
                            "title": "No",
                            "payload": json.dumps({'response': 'r3'})
                        }
                    ]
                }
            }
        }
    }

    botutils.call_send_api(messageData)


def send_p3(fbuser):
    print "sendp3"

    access_token = fbuser.yt_access_token
    if access_token:
        send_liked_videos(fbuser)
    else:
        send_auth_link_btn(fbuser.fbid)

    fbuser.setstate('p3')


def send_p1(fbuser):
    print "send p1"

    data = {
        'recipient': {
            'id': fbuser.fbid
        },
        'message': {
            'text': "Get Started!!",
            'quick_replies': [
                {
                    "content_type": "text",
                    "title": "Search",
                    "payload": json.dumps({'response': 'r1'})
                },
                {
                    "content_type": "text",
                    "title": "Get Liked Songs",
                    "payload": json.dumps({'response': 'r2'})
                }
            ]
        }
    }

    fbuser.setstate('p1')
    botutils.call_send_api(data)


def send_reset_quick_reply(fbuser):
    print "send_reset_quick_reply"
    data = {
        'recipient': {
            'id': fbuser.fbid
        },
        'message': {
            'text': "Reset?",
            'quick_replies': [
                {
                    "content_type": "text",
                    "title": "Reset",
                    "payload": json.dumps({'response': 'r3'})
                }
            ]
        }
    }

    botutils.call_send_api(data)


def check_response(message):
    print "check_response"

    quick_reply = message.get('quick_reply')
    if quick_reply:
        payload = quick_reply.get('payload')
        if payload:
            payload = json.loads(payload)
            response = payload.get('response')
            if response:
                return response

    return None


def send_after_registration_messages(fbuser):
    bot_sample_calls.sendText(fbuser.fbid, "thanks for the registration")
    send_liked_videos(fbuser)


def send_liked_videos(fbuser):
    bot_sample_calls.sendText(fbuser.fbid, "Your last 10 liked music videos")
    bot_sample_calls.sendTypingOn(fbuser.fbid)
    refresh_token = fbuser.yt_refresh_token
    new_access_token = youtubeutils.get_new_access_token(refresh_token)
    liked_videos = youtubeutils.get_liked_videos(new_access_token)
    botutils.send_video_search_results(fbuser, liked_videos)
    # send_reset_quick_reply(fbuser)


def postbackReceived(event):
    print "postbackReceived called"

    s = {
        u'timestamp': 1479218513945,
        u'postback':
            {u'payload': u'{"response": "r3"}'
             },
        u'recipient': {u'id': u'157955300922253'},
        u'sender': {u'id': u'1150296141673799'}
    }


    postback_payload = event.get('postback').get('payload')
    postback_payload = json.loads(postback_payload)
    senderId = event['sender']['id']
    recipientId = event['recipient']['id']
    fbid = senderId
    fbuser = botutils.create_find_fb_user(fbid)
    userstate = fbuser.userstate()
    print fbuser, userstate

    postback_response = postback_payload.get('response')

    if postback_response == 'r3':
        send_p1(fbuser)
