from recent import recent_down, recent_up
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from recent import *
from new import *
from event import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('tegZ5yxcpKtlWbAJTjLEMPumOTnjh9CuyMs65DkbPIAHaREkt/ZACsmg9stoz8uLxJ9hh+lQPV8kyAlZdq4wKT1rZfZye7bmNh83MBFNld1ZShT88zeoc8FpKEMFj66iZooG7NwDJcv5pVD0fgrCRgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('df76d2aff2f56f7ce5597d45eb29931c')

# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '近期活動上' in msg:
        message = recent_up()
        line_bot_api.reply_message(event.reply_token, message)
    elif '近期活動下' in msg:
        message = recent_down()
        line_bot_api.reply_message(event.reply_token, message)
    elif '學系之夜' in msg: 
        message = department()
        line_bot_api.reply_message(event.reply_token, message)
    elif '新生包' in msg: 
    #    message = pack()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '地區迎新' in msg: # 選課系統
    #    message = area()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '行事曆' in msg: 
    #    message = schedule()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '迎新茶會' in msg:
    #    message = tea()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '制服日' in msg:
    #   message = uniform()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '系烤' in msg:
    #   message = bbq()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '萬聖節晚會' in msg:
    #   message = halloween()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '耶誕晚會' in msg:
    #   message = xmas()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '湯圓晚會' in msg:
    #   message = lantern()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '宿營' in msg:
    #   message = camp()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '資工週' in msg:
    #   message = csie_week()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '系卡' in msg:
    #   message = karaoke()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)
    elif '資工營' in msg:
    #   message = csie_summer_camp()
        message = not_yet()
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
