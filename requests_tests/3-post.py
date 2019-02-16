# coding=utf-8
import requests


"""
bing 翻译
"""

url = 'http://cn.bing.com/ttranslationlookup?&IG=B576007BF81E4003A650A81EC9FD80FD&IID=translator.5038.4'

formdata = {
    'from': 'en',
    'to': 'zh-CHS',
    'text': 'dog',
}
# (.*?): (.*?)\n?
# '\1': '\2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.67 Safari/537.36',
}

r = requests.post(url=url, headers=headers, data=formdata)
# 使用r.json() 将直接显示json格式数据
# r.json 显示的是对象
print(r.json())
