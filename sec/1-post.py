# coding=utf-8

import urllib.request
import urllib.parse

# 获取posturl地址
post_url = "https://fanyi.baidu.com/sug"
word = input('请输入您要查询的英文单词：')
# 构建post表单
from_data = {
    'kw': word,
}

# 发送请求的过程
# 自己要伪装的头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/70.0.3538.67 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url=post_url,headers=headers)
# 处理表单数据
from_data = urllib.parse.urlencode(from_data).encode()
# 发送请求
resonse = urllib.request.urlopen(request, data=from_data)
print(resonse.read().decode())
