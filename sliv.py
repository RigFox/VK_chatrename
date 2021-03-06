# -*- coding: utf-8 -*-

from setting.setting import VK_API_TOKEN
from setting.setting import VK_CHAT_ID
import requests
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('log/log.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fSeptember = "02.09.2016"
fSeptemberDate = datetime.datetime.strptime(fSeptember, "%d.%m.%Y")

nowDate = datetime.datetime.now()

diffDate = fSeptemberDate - nowDate

dayStr = "день"
if diffDate.days // 10 == 1:
  dayStr = "дней"
elif (diffDate.days % 10 == 0) or (diffDate.days % 10 >= 5):
  dayStr = "дней"
elif (diffDate.days % 10 in [2,3,4]):
  dayStr = "дня"

pmProgress = str(round(2 + ((92 - diffDate.days) / 92), 6)) + " ПМиИ. " + str(diffDate.days) + " " + dayStr + " до 1 сентября"

payload = {"chat_id": VK_CHAT_ID, "title": pmProgress, "access_token": VK_API_TOKEN}
r = requests.get('https://api.vk.com/method/messages.editChat', params=payload, timeout=10)

logger.debug("VK API return: " + r.text)
