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
line_bot_api = LineBotApi('7hjz3UmWTaV8DyImwyZsXOJ++tTd7PDNTE6QqGaHpwURfSfxQhOin6rpLT09EAEBX+2Qn+AMdgdheLyIVSKDn/T14oxg0IDgs8IXD60kEMjKQ2UzrxeeQkDuv0bSNA2JYI8BS0kNcQdfkP4CdO5jAQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d5c43898787d24fc5cd20b1fc6782b7d')
#===========[ NOTE SAVER ]=======================
notes = {}

def carijadwal(kota):
    URLteman = "https://time.siswadi.com/timezone/" + kota
    r = requests.get(URLteman)
    data = r.json()
    # print(data)
    status = data['time']['timezone']
    letak = data['location']['address']
    jam = data['time']['time']
    # print("Daerah : " + status + "\n"+"kota : " + letak + "\n"+ "Jam sholat : " + jam)
    a = "Daerah : " + status + "\n"+"kota : " + letak + "\n"+ "Jam sholat : " + jam
    return a


# Post Request
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
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)
    
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=carijadwal(text)))
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

