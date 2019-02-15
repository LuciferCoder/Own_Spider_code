# coding=utf-8

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?' \
      'type=5&interval_id=100%3A90&action=&'

# start limit
# 'https://movie.douban.com/j/chart/top_list?' \
#       'type=5&interval_id=100%3A90&action=&start=0&limit=20'

# 'https://movie.douban.com/j/chart/top_list?' \
#       'type=5&interval_id=100%3A90&action=&start=20&limit=20'

page = int(input('请输入想要第几页的数据：'))
number = 20
# 构建数据
data = {
    'start': (page-1) * number,
    'limit': number,
}

# 将字典转化为query_string
query_string = urllib.parse.urlencode(data)
# 修改url
url += query_string

# 发送请求的过程
# 自己要伪装的头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/70.0.3538.67 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())
