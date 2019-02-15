# coding=utf-8

import urllib.request
import urllib.parse

# 创建handler
handler = urllib.request.ProxyHandler({'http': '171.80.175.190:9999'})

opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/70.0.3538.67 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = opener.open(request)

with open('ip.html', 'wb') as fp:
    fp.write(response.read())
