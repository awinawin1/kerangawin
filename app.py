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

#REQUEST DATA teman
def cariteman(panggilan):
    URLpanggilan = "http://www.aditmasih.tk/api_awinawin/show.php?panggilan=" + panggilan
    r = requests.get(URLpanggilan)
    data = r.json()
    err = "data tidak ditemukan"
    
    flag = data['flag']
    if(flag == "1"):
        panggilan = data['teman'][0]['panggilan']
        no_hp = data['teman'][0]['no_hp']
        hobby = data['teman'][0]['hobby']
        jurusan = data['teman'][0]['jurusan']
        kampung = data['teman'][0]['kampung']

        # munculin semua, ga rapi, ada 'u' nya
        # all_data = data['teman'][0]
        data= "panggilan : "+panggilan+"\no_hp : "+no_hp+"\ hobby: "+hobby\jurusan: "+jurusan+"\kampung: "+kampung
        return data
        # return all_data

    elif(flag == "0"):
        return err

#INPUT DATA teman
def inputteman(panggilan, no_hp, hobby, jurusan, kampung):
    r = requests.post("http://www.aditmasih.tk/api_awinawin/insert.php", data={'panggilan': panggilan, 'no_hp': no_hp, 'hobby': hobby, 'jurusan': jurusan, 'kampung':kampung})
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        return 'Data '+panggilan+' berhasil dimasukkan\n'
    elif(flag == "0"):
        return 'Data gagal dimasukkan\n'


#DELETE DATA teman
def hapusteman(panggilan):
    r = requests.post("http://www.aditmasih.tk/api_awinawin/delete.php", data={'panggilan': panggilan})
    data = r.json()

    flag = data['flag']
   
    if(flag == "1"):
        return 'Data '+panggilan+' berhasil dihapus\n'
    elif(flag == "0"):
        return 'Data gagal dihapus\n'

def updateteman(panggilanJadul,panggilan,no_hp,hobby,jurusan,kampung):
    URLteman = "http://www.aditmasih.tk/api_awin/show.php?panggilan=" + panggilanJadul
    r = requests.get(URLteman)
    data = r.json()
    err = "data tidak ditemukan"
    teman_jadul=temanjadul
    flag = data['flag']
    if(flag == "1"):
        r = requests.post("http://www.aditmasih.tk/api_awinawin/update.php", data={'panggilan': panggilan, 'no_hp': no_hp, 'hobby': hobby, 'jurusan':jurusan, 'kampung':kampung 'panggilanJadul':panggilanJadul})
        data = r.json()
        flag = data['flag']

        if(flag == "1"):
            return 'Data '+panggilanJadul+'berhasil diupdate\n'
        elif(flag == "0"):
            return 'Data gagal diupdate\n'

    elif(flag == "0"):
        return err

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
    text = event.message.text #simplify for receive message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)

    data=text.split('-')
    if(data[0]=='lihat'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cariteman(data[1])))
    elif(data[0]=='tambah'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=inputteman(data[1],data[2],data[3],data[4]),data[5])))
    elif(data[0]=='hapus'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=hapusteman(data[1])))
    elif(data[0]=='ganti'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=updateteman(data[1],data[2],data[3],data[4],data[5],data[6])))
   
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
