from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests
import re
import requests, json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Yd9bSGIfnnSbIQMIktXnmylAcM7xOWpFVgX1qb0wOPdsUCHmQJESpvMh2RJSNLjeX+2Qn+AMdgdheLyIVSKDn/T14oxg0IDgs8IXD60kEMiPCUtK1P4j4g6ty5qMKogrQm4qH7e6tnmFqScoeEVT2AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('827a3082a52880e667b25a02b982c2f2')
#===========[ NOTE SAVER ]=======================
notes = {}

#input mencari
def cariteman(kota):
    URLteman = "https://time.siswadi.com/timezone/" + kota
    r = requests.get(URLteman)
    data = r.json()
    # print(data)
    status = data['time']['timezone']
    jam = data['time']['time']
    waktu="Daerah : " + status + "\n" + "Jam sholat : " + jam

return (waktu)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receive message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)

    data=text.split('-')
    if(data[0]=='cek'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cariteman(data[1])))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Bukan menupakan kota di Indonesia pakai cek-(nama kota)"))
    
   
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=porta
