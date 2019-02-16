# coding=utf-8
import urllib.request
import urllib.parse
import json

"""
1、之前的简单网站登录过程：直接抓包到post地址，发送过去即可完成登录成功
2、现在登良路过程：直接抓包发送post不行，因为表单中有一些数据需要从网页中获取到，比之前的formhash。
    现在的登录过程就变成了，先发送get请求到登录页面，然后通过xpath、bs等获取需要的表单，然后再发送到post请求
    开始登陆。
"""
url = 'http://account.chinaunix.net/login/login'
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

response = urllib.request.urlopen(request, data=formdatas)
# print(response.read().decode())
"""
{"code":200,"msg":"成功","data":{"url":"/login/sso?url=%2Fucenter%2Fuser%2Findex"}}
"""
json_data = response.read().decode()
# print(json_data)
data_1 = json.loads(json_data)
# {'url': '/login/sso?url=%2Fucenter%2Fuser%2Findex'}
# print(data_1['data']['url'])
url1 = data_1['data']['url']

# print(response.read().decode())
url_t1 = urllib.parse.urljoin(url, url1)
response = urllib.request.urlopen(url_t1)
print(response.read().decode())
# print(json_data[2]['url'])