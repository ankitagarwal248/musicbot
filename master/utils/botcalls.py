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
        bot_sample_calls.sendText(fbid, "Quick Reply Tapped")
        return True

    fbuser = botutils.create_find_fb_user(fbid)
    print fbuser

    if messageText:
        messageText = messageText.lower()

        if 'image' in messageText:
            bot_sample_calls.sendImageMessage(fbid)
        elif 'gif' in messageText:
            bot_sample_calls.sendGifMessage(fbid)
        elif 'audio' in messageText:
            bot_sample_calls.sendAudioMessage(fbid)
        elif 'video' in messageText:
            bot_sample_calls.sendVideoMessage(fbid)
        elif 'file' in messageText:
            bot_sample_calls.sendFileMessage(fbid)
        elif 'button' in messageText:
            bot_sample_calls.sendButtonMessage(fbid)
        elif 'generic' in messageText:
            bot_sample_calls.sendGenericMessage(fbid)
        elif 'quick reply' in messageText:
            bot_sample_calls.sendQuickReply(fbid)
        elif 'read receipt' in messageText:
            bot_sample_calls.sendReadReceipt(fbid)
        elif 'typing on' in messageText:
            bot_sample_calls.sendTypingOn(fbid)
        else:
            bot_sample_calls.sendText(fbid, messageText)
    elif messageAttachment:
        bot_sample_calls.sendText(fbid, "message with attachment received")

    return True

