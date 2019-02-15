# coding=utf-8

import urllib.request
import urllib.parse
import http.cookiejar

# 真实的模拟浏览器，当发送完post请求的时候，将cookie保存到代码中
# 创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
# 通过cookiekar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
# 根据handler创建一个opener
opener = urllib.request.build_opener(handler)

url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019041541394'

formdata = {
    'email': '13261924736',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '710c1a18e7aaf6a3f63c1c6f8f4d01f82d411c22209811020fef9d531705cac8',
    'rkey': 'd56fdd61c78ec2f9b2b0ceacf778e024',
    'f': 'http%3A%2F%2Fwww.renren.com%2F969538686',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/70.0.3538.67 Safari/537.36',
}

# 登录-发送请求表单
request = urllib.request.Request(url=url, headers=headers)

formdata = urllib.parse.urlencode(formdata).encode()

response = opener.open(request, data=formdata)
# cookie = response.cookies
# print(cookie)

# print(response.read().decode())

get_url = 'http://www.renren.com/969538686/profile'

request = urllib.request.Request(url=get_url, headers=headers)
response = opener.open(request)

print(response.read().decode())
