# coding=utf-8

import urllib.request
import urllib.parse
import os

url = 'http://tieba.baidu.com/f?ie=utf-8&'
# pn = (page - 1) * 50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0

# 输入起始页码，输入结束页码，输入吧名，
# 然后在当前文件夹中创建一个以吧名为名字的文件夹，
# 里面是每一页的htnl内容，文件名是吧名_page.html

ba_name = input('请输入要爬取的吧名：')
start_page = int(input('请输入要爬取的起始页码：'))
end_page = int(input('请输入要爬取的结束页码：'))

# 创建文件夹
if not os.path.exists(ba_name):
    os.mkdir(ba_name)


# 搞个循环依次爬取每一页数据
for page in range(start_page, end_page + 1):
    # page就是当前页
    # 拼接url的过程
    data = {
        'kw': ba_name,
        'pn': (page - 1) * 50,
    }
    data = urllib.parse.urlencode(data)
    url_index = url + data
    # print(url_index)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/70.0.3538.67 Safari/537.36',
    }
    request = urllib.request.Request(url=url_index, headers=headers)
    print('第%d页开始下载...' % page)
    response = urllib.request.urlopen(request)

    #生成文件名
    filename = ba_name + "_" + str(page) + ".html"
    filepath = ba_name + '/' + filename

    # 写内容
    with open(filepath, 'wb') as fp:
        fp.write(response.read())
        print('第%s页下载完毕...' % page)
        #fp.close()
