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
        #"apiKey": "af74c4f300d74314b2a904c9274dcf48",
        "apiKey" : "1ffce46bd830420090d940cead41356e",
        "userId": "285633"
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
    print('%s: %s' % (msg['FromUserName'], msg['Text']))
    import pdb
    reply = get_response(msg['Text'])
    print('reply: %s' % reply)
    pdb.set_trace()
    return reply or defaultReply


itchat.auto_login()
itchat.run()
