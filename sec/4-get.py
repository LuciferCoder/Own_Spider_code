# coding=utf-8

import urllib.parse
import urllib.request

word = input("请输入您想搜索的内容：")
url = 'http://www.baidu.com/s?'

# 参数写成一个字典
data = {
    "ie": "utf-8",
    "wd": word,
}

qurey_string = urllib.parse.urlencode(data)
url = url + qurey_string

# 发送请求
response = urllib.request.urlopen(url)
read = response.read()
filename = word + ".html"

# urllib.request.urlretrieve(url,filename)
with open(filename, 'wb') as fp:
    fp.write(read)
    fp.close()

response.close()
