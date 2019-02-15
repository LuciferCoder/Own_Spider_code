# coding=utf-8

import urllib.request
import urllib.parse
import re

url = 'http://www.yikexun.cn/lizhi/qianming/20190141227.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.67 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)
content = urllib.request.urlopen(request).read().decode()
# print(content)
pattern = re.compile(r'<li>(.*?)</li>', re.S)
string = pattern.findall(content)
print(string)
print(len(string))
# exit()
with open('lizhi_test.html', 'a', encoding='utf8') as fp:
    for i in range(0, 14):
        fp.write(string[i])
