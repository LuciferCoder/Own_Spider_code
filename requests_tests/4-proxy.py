# coding=utf-8
import requests

url = 'https://www.baidu.com/s?wd=ip&ie=utf-8'
proxies = {
    'http': 'http://121.233.206.205:9999',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.67 Safari/537.36',
}

r = requests.get(url=url, headers=headers, proxies=proxies)
# print(r.text)
with open('proxy.html', 'wb') as fp:
    fp.write(r.content)
