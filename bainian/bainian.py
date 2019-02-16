#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import urllib.request
import time
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"}

# 输出时间
print('现在开始运行程序，当前时间是：', time.asctime(time.localtime(time.time())))

# # 构建字段容器
names = []
file_addresses = []

#soup = BeautifulSoup.
# 文件：<a href="/data/cms/archive/201412(5)/848632/中英人寿优选缘福两全保险条款（变更）--加密版.pdf">查看 &gt;&gt;</a>
# 页码： <a id="next" href="/website/xxzx/gkxxpl/gsjbxx/grbxtk/rsbx/list-2.shtml"><span style="
# color:#6b6b6b; background:none">下一页</span></a>

root_url = r'http://www.aviva-cofco.com.cn/website/xxzx/gkxxpl/gsjbxx/grbxtk/rsbx/list-1.shtml'

r = urllib.request.urlopen(root_url)
urltext = r.read().decode('utf-8')
# print (urltext)

file_addresses = re.findall('<li class="li_content"><a href="(/data/cms/archive/.*\.[pP][dD][fF])">', urltext)
names = re.findall('<li class="li_content"><a href="/data/cms/archive/.*/(.*)\.pdf', urltext)
print(type(names))
print(len(names))
# soup = BeautifulSoup()
print("*" * 40)
print(file_addresses)
print(len(file_addresses))


def Make_url(address):
    url = 'http://www.aviva-cofco.com.cn' + address
    # url=url.decode('utf-8')
    return url


def getFile_downloader(url):
    file_name = url.split('/')[-1]
    # print(file_name) 中英人寿安鑫传家终身寿险条款.pdf
    response = urllib.request.urlopen(url)
    # block_sz = 8192
    with open(file_name, 'w') as f:
        buffer = response.read()
        f.write(buffer)
    f.close()

    print("Sucessful to download" + " " + file_name)


# 写入条款信息
file = open('bainian.txt', 'w')
file.write('|'.join(('地址', '条款名字')) + '\n')

for i in range(0, 5):
    # print(i)
    url = Make_url(addresses[i])
    getFile_downloader(url)

# 输出时间
print('程序运行结束，当前时间是：', time.asctime(time.localtime(time.time())))
