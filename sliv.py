# -*- coding: utf-8 -*-

from setting.setting import VK_API_TOKEN
from setting.setting import VK_CHAT_ID
import requests
import datetime
import logging

logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    encoding='utf-8',
                    filename=u"log/log.log")

fSeptember = "01.09.2015"
fSeptemberDate = datetime.datetime.strptime(fSeptember, "%d.%m.%Y")

nowDate = datetime.datetime.now()

diffDate = nowDate - fSeptemberDate

pmProgress = str(round(2 + (diffDate.days / 365), 6)) + " ПМиИ"

payload = {"chat_id": VK_CHAT_ID, "title": pmProgress, "access_token": VK_API_TOKEN + "b"}
r = requests.get('https://api.vk.com/method/messages.editChat', params=payload, timeout=10)

logging.debug("VK API return: " + r.text)
