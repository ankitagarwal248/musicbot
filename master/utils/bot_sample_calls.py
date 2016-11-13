from master.utils import pafyutils
from master.utils.botutils import call_send_api


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
    messageData = {
      "recipient":{
        "id": fbid
      },
      "message": {
        "attachment": {
          "type": "audio",
          "payload": {
            "url": pafyutils.sample_audio_url
          }
        }
      }
    }

    call_send_api(messageData)


def sendVideoMessage(fbid):
    messageData = {
      "recipient": {
        "id": fbid
      },
      "message": {
        "attachment": {
          "type": "video",
          "payload": {
            "url": pafyutils.sample_video_url
          }
        }
      }
    }

    call_send_api(messageData)


def sendFileMessage(fbid):
    messageData = {
              "recipient": {
                "id": fbid
              },
              "message": {
                "attachment": {
                  "type": "file",
                  "payload": {
                    "url": pafyutils.sample_audio_url
                  }
                }
              }
            }

    call_send_api(messageData)

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

    call_send_api(messageData)


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
                        'buttons': [
                            {
                                'type': "web_url",
                                'url': pafyutils.sample_audio_url,
                                'title': "Open Video"
                            },
                            {
                                "type": "web_url",
                                "url": "https://faae45a0.ngrok.io/",
                                "title": "Select Criteria",
                                "webview_height_ratio": "compact"
                            },
                            {
                                'type': "web_url",
                                'url': "http://redirector.googlevideo.com/videoplayback?sparams=dur%2Cei%2Cgcr%2Chcs%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Cshardbypass%2Csource%2Cupn%2Cexpire&id=o-APqY1W353M0xFJNPwBqSy0IT1ZK13bz0Tvrwca8r9_WF&initcwndbps=3347500&ip=159.253.144.86&ei=EFInWP2yDMWxcqqLuXg&dur=261.851&shardbypass=yes&ms=au&mv=m&mt=1478971819&mn=sn-p5qlsnle&mm=31&source=youtube&upn=Gm9zTlWIGfc&lmt=1478830965451507&key=yt6&itag=22&mime=video%2Fmp4&ipbits=0&pl=24&gcr=us&hcs=yes&ratebypass=yes&nh=IgpwcjAzLmlhZDA3KgkxMjcuMC4wLjE&expire=1478993520&signature=6DF3816CD65A9A4A53A41C0DDD6CEA6298CBFA03.6DBA7753FD1DE3166DAA1F7A228A6616459DAEEF&title=The+Chainsmokers+-+Closer+%28Lyric%29+ft.+Halsey",
                                'title': "Download Audio"
                            },
                            # {
                            #     'type': "postback",
                            #     'title': "Call Postback",
                            #     'payload': "Payload for first bubble",
                            # }
                        ],
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
                        }
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


def sendText(fbid, message):
    messageData = {
        'recipient': {
            'id': fbid
        },
        'message': {
            'text': message
          }
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
        print "quick reply"
        # sendTextMessage(fbid, "Quick Reply Tapped")
        return True

    if messageText:
        messageText = messageText.lower()

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
            sendText(fbid, messageText)
    elif messageAttachment:
        sendText(fbid, "message with attachment received")

    return True

