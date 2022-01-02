from flask import Flask, request, abort
#from __future__ import unicode_literals
from flask import jsonify
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import getHomework

import configparser

app = Flask(__name__)
# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('/home/peng/Team9/config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="作業提醒":
        #text,t1 = getHomework.gethw('C108118129','5515')
        #print(text,t1)
        result =""
        test = ['遠距教學缺席報告', '桌球期末報告', '面試App測試', 'ppt上傳繳交區服創早34', '程式作業:資料結構遞迴程式應用-小畫家封閉區域塗色功能', '【第六次小組作業】軟體專案管理期末報告(Final Oral)', '110-1_NKUST_MIS- Android App-期末報告']
        time = ['從 2021-06-10 00:00 到 2021-06-23 23:59', '從 2021-06-05 00:00 到 2021-06-23 23:59', '從 2019-11-26 00:00 到 2019-11-26 23:59', '從 即日起 到 無限期', '從 即日起 到 無限期', '從 2021-12-22 00:00 到 2022-01-16 00:00', '從 2021-12-28 11:00 到 2022-01-14 23:30']
        for i in range(len(test)):
            result = result + test[i] + " : " + time[i] + "\n"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = result))
    elif event.message.text=="資料搜尋":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "此功能上在開發當中！敬請期待"))
    elif event.message.text=="課堂資訊":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "此功能上在開發當中！敬請期待"))
    elif event.message.text=="考試提醒":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "此功能上在開發當中！敬請期待"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "感謝您的訊息！請重新輸入正確的指令\n1. 作業提醒\n2. 資料搜尋\n3. 課堂資訊\n4. 考試提醒"))




if __name__ == '__main__':
    app.run(port=5000)



