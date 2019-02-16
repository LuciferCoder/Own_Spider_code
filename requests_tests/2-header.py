# coding=utf-8
import requests

# url = 'http://www.baidu.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/70.0.3538.67 Safari/537.36',
# }
# r = requests.get(url, headers=headers)
# # print(r.encoding)
# # print(r.text)
# r.encoding = 'utf8'
# print(r.text)

# 带参数的额get
url = 'https://www.baidu.com/s'
# https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD&rsv_spt=1&rsv_iqid=0xb7da93a80002c563&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=10&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&inputT=1366&rsv_sug4=2852
data = {
    'ie': 'utf8',
    'wd': '中国',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.67 Safari/537.36',
}
r = requests.get(url=url, headers=headers, params=data)
# # 把结果写到文件中
# with open('baidu.html', 'wb') as fp:
#     fp.write(r.content)
print(r.status_code)
print(r.headers)
print(r.url)



