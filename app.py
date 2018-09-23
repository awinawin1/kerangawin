from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json

from random import randint
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
line_bot_api = LineBotApi('2SuilSaQz7z3veGQjioUZ/bqxYd7XQNxGNxqgXmsLXntv5w2r5YQVMjwNgP4TedFX+2Qn+AMdgdheLyIVSKDn/T14oxg0IDgs8IXD60kEMi0jnqViYpZRg5bq9pg29lR/S+JThQDSWHumiLeoMaHBQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6e7f36d0a3dd7c5e8b8ed88414a880c2')
#===========[ NOTE SAVER ]=======================
notes = {}

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
    a=(randint(0, 9))
    if a%2:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Iya'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Tidak'))
    # if text=="who?":
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text='ini awin'))
    # if text=="where?":
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text='RPL'))
    # if text=="why?":
    #     line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id='1', sticker_id='1'))


    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Halo '+profile.display_name+'\nKata Kunci Tidak Diketahui :) \nKetik "menu" untuk mengetahui menu yang tersedia'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)