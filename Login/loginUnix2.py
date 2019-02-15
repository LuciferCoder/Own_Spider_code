# coding=utf-8
import urllib.request
import urllib.parse
import json
import http.cookiejar
import re

first_page_url = 'http://www.chinaunix.net/'
url = 'http://account.chinaunix.net/login/login'
cj = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor()
openner = urllib.request.build_opener(handler)
# url = 'http%3A%2F%2Fbbs.chinaunix.net%2Fforum.php%3Ftid%3D84707881'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.67 Safari/537.36',
}
# 'referer': 'http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2Fforum.php%3Ftid%3D84707881',
# formhsh  表单令牌
data = {
    'username': 'your_acount',
    'password': 'your_passwd',
    '_token': '9M61IFWQCK1uPo0v9sfeifkIF9kH9vfITlE8yfbF',
    '_t': '1550122001753',
}

formdatas = urllib.parse.urlencode(data).encode()
request = urllib.request.Request(url=url, headers=headers)
"""
此网站是明文登陆，通过抓包可以发现，经过了两次跳转
{"code":200,"msg":"成功","data":{"url":"/login/sso?url=%2Fucenter%2Fuser%2Findex"}}
"""
response = openner.open(request, formdatas)
# print(response.read().decode())
json_data1 = response.read().decode()
json_data1 = json.loads(json_data1)
tz1 = json_data1['data']['url']
# print(tz1)
# 第一次跳转
tz1_url = urllib.parse.urljoin(url, tz1)
response2 = openner.open(tz1_url)
# print(response2.read().decode())
html_tz2 = response2.read().decode()
# print(html_tz2)
rec = re.compile("var url = '(.*)';")
# print(rec.findall(html_tz2))
tz2 = rec.findall(html_tz2)[0]
# print(type(tz2))
tz2_url = urllib.parse.urljoin(url, tz2)
# print(tz2_url)
# response3 = openner.open(tz2_url)
# print(response3.read().decode())

# 抓取页面成功
first_page_response = openner.open(first_page_url)
with open('unix.html', 'w', encoding='utf8') as fp:
    fp.write(first_page_response.read().decode())
print("spide over!")
