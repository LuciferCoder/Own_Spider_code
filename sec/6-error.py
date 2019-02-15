# coding=utf-8

import urllib.request
import urllib.parse
import urllib.error

# url = 'http://www.maodan.com/'
# https://blog.csdn.net/m0_37622530/article/details/81257015
url = 'https://blog.csdn.net/m0_37622530/article/details/8125701'
# NameError
# print(a)

# 捕获异常
try:
    response = urllib.request.urlopen(url)
    print(response)
#except Exception as e:
# except urllib.error.NameError as e:
except urllib.error.HTTPError as e:
    print(e)
    print(e.code)
except urllib.error.URLError as e:
    print(e)
