#!/usr/bin/env python3

import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

print("Content-type: text/html; charset=utf-8\n")

import requests
import os
import json

fls = os.listdir('./')
# fname = fls[7]
fname = "t.pdf"
fname = "Тестовое задание/Frontend-разработчик/Танский Михаил.pdf".encode('utf-8')
print()
print("<br />")
f = open('conf.json')
j = json.loads(f.read())
token = j["token"]
uid = 4756
heads = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Python3. VestaXlsxApp (test@huntflow.ru)', "X-File-Parse": "true"}
# heads['Content-Type'] = "multipart/form-data"
f1 = open(fname, 'rb')
fcontent = f1.read()
print()
print("<br />")

# post = {"file": f1} #
# TODO: брать расширение из имени файла
post = {'file': ('rt.pdf', fcontent)}
# r = requests.post('/python/testhf/test_post.php', headers=heads, files=post) # https://api.huntflow.ru/account/4756/upload
r = requests.post('https://api.huntflow.ru/account/' + str(uid) + '/upload', headers=heads, files=post) # https://api.huntflow.ru/account/4756/upload
print(r.text + "<br />") # {"errors": [{"type": "upload", "value": "unable_to_upload"}]}
# print(json.loads(r.text))
# print(r.request.headers)
print("<br />")

print(sys.getfilesystemencoding())

# Вопрос 1: что не так к моменту выполнения строки 34 или в ней самой? Почему ответ {"errors": [{"type": "upload", "value": "unable_to_upload"}]} ?
