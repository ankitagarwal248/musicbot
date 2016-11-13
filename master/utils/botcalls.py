import json
from master.utils import bot_sample_calls
from master.utils import botutils


def messageReceived(event):
    print "messageReceived called"
    message = event.get('message')
    senderId = event['sender']['id']
    recipientId = event['recipient']['id']
    isEcho = message.get('is_echo')
    # messageId = message['mid']
    # appId = message['app_id']
    # metadata = message['metadata']

    print message

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
        if page_response == 'r1':
            send_p2(fbuser)
        if page_response == 'r2':
            send_p3(fbuser)

        return True

    if userstate == 'p2':
        send_p4(fbuser, message)
        return True


def send_p4(fbuser, message):
    print "sendp4"
    message_text = message.get('text')
    bot_sample_calls.sendText(fbuser.fbid, "Search results")
    fbuser.setstate('p4')


def send_p2(fbuser):
    print "sendp2"
    bot_sample_calls.sendText(fbuser.fbid, "Type the name of the song you wanna download")
    fbuser.setstate('p2')


def send_p3(fbuser):
    print "sendp3"
    bot_sample_calls.sendText(fbuser.fbid, "sendp3")
    fbuser.setstate('p2')


def send_p1(fbuser):
    print "send p1"

    data = {
        'recipient': {
            'id': fbuser.fbid
        },
        'message': {
            'text': "What do you need?",
            'quick_replies': [
                {
                    "content_type": "text",
                    "title": "Search",
                    "payload": json.dumps({'response': 'r1'})
                },
                {
                    "content_type": "text",
                    "title": "Get Top Songs",
                    "payload": json.dumps({'response': 'r2'})
                }
            ]
        }
    }

    fbuser.setstate('p1')
    botutils.call_send_api(data)
    userstate = fbuser.userstate()
    print userstate


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