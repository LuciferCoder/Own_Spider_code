# coding=utf-8

import urllib.request
import urllib.parse
import ssl

# url后面不加“/”，则不是正确的url格式，浏览器会自动给添加“/”
url = 'http://www.baidu.com/'

# response = urllib.request.urlopen(url)
# read = response.read()
# print(read.decode())
# print(response.headers)

# 自己要伪装的头部
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/70.0.3538.67 Safari/537.36',
}

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求信息
response = urllib.request.urlopen(request)

readings = response.read()
print(readings.decode())




