# coding=utf-8
import requests

url = 'http://www.baidu.com/'
r = requests.get(url)
# print(r.encoding)
# print(r.text)
r.encoding ='utf8'
print(r.text)