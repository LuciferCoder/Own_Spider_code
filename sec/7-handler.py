# coding=utf-8

import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/70.0.3538.67 Safari/537.36',
}

# 创建一个handler
handler = urllib.request.HTTPHandler()
# 通过handler创建一个opener
# opener就是一个对象，一会发送请求的时候，直接使用opener里面的方法即可
# ，不要使用urlopen()了
opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url, headers=headers)

# 发送请求
response = opener.open(request)

print(response.read().decode())
