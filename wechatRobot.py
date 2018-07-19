# -*- coding=utf-8 -*-
import requests
import itchat
import pdb
import json


def get_response(msg):
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'

    data = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": msg
        },
        "inputImage": {
            "url": "imageUrl"
        },
    },
    "userInfo": {
        "apiKey": "yourapikey",
        "userId": "youruserid"
    }
}

    try:
        r = requests.post(url=apiUrl, json=data)
        body = json.loads(r.text)
        return body.get('results', {})[0].get('values', {}).get('text')
    except:
        return u'你好，我在忙，稍后回复'

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply


itchat.auto_login()
itchat.run()
