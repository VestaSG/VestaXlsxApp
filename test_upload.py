#!/usr/bin/env python3

import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

print("Content-type: text/html; charset=utf-8\n")

import requests
import os
import json

print("<br />")
fls = os.listdir('./')
# fname = fls[7]
fname = "t.pdf"
print()
print("<br />")
f = open('conf.json')
j = json.loads(f.read())
token = j["token"]
uid = 4756
heads = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Python3. VestaXlsxApp (test@huntflow.ru)', "X-File-Parse": "true"}
# heads['Content-Type'] = "multipart/form-data"
# post = {"file": open("Тестовое задание/Frontend-разработчик/Танский Михаил.pdf", 'rb')} #.encode('utf-8')
post = {"file": open(fname, 'rb')} #
# r = requests.post('/python/testhf/test_post.php', headers=heads, files=post) # https://api.huntflow.ru/account/4756/upload
r = requests.post('https://api.huntflow.ru/account/' + str(uid) + '/upload', headers=heads, files=post) # https://api.huntflow.ru/account/4756/upload
print(r.text + "<br />") # {"errors": [{"type": "upload", "value": "unable_to_upload"}]}
# print(json.loads(r.text))
# print(r.request.headers)
print("<br />")

# Вопрос 1: что не так к моменту выполнения строки 28 или в ней самой?
# Вопрос 2: Что читать по работе с файлами с не ascii путями как в строке 25?
