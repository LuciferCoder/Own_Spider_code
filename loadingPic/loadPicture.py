# coding=utf-8
# Spider5 about Spiderlearning by using xpath
import time
from lxml import etree
import urllib.request
import urllib.parse
import os


# root_url :
# first page : http://sc.chinaz.com/tupian/index.html
# url = "sc.chinaz.com/tupian"
# http://sc.chinaz.com/tupian/xingganmeinvtupian.html
# 1 : http://sc.chinaz.com/tupian/xingganmeinvtupian.html
# 2 : http://sc.chinaz.com/tupian/xingganmeinvtupian_2.html
# 3 : http://sc.chinaz.com/tupian/xingganmeinvtupian_3.html

def handle_request(url, page):
    # 由于第一页和后面页码的规律不一样，所以要进行判断
    if page == 1:
        url = url.format('')
        url.format
    else:
        url = url.format('_' + str(page))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/70.0.3538.67 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def download_img(image_src):
    # 下载有两种方式：
    # 此处使用发送请求写入文件的方式：
    dirpath = 'xinggam'
    # 创建一个文件夹
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)

    # filename
    filename = os.path.basename(image_src)
    # filepath
    filenpath = dirpath + "/" + filename
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/70.0.3538.67 Safari/537.36',
    }
    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filenpath, 'wb') as fp:
        fp.write(response.read())


def parse_content(content):
    tree = etree.HTML(content)
    """
    //div[@id="container"]/div/div/a/img/@src  无法使用
    一般xpath的使用会用到两个问题：
        这里是懒加载，懒加载是前端的技术
        懒加载的意思是用到的时候再加载！
        浏览器的可视区域有限，当你下滑浏览器的时候，图片再加载；
        可以通过查看源代码来查看实际的代码，因为请求发送之后，获得的都是实际源代码
    图片的加载是要单独加载请求的，js，css都是单独请求的，单独这个网页就有40个图片的连接，
    如果网络环境的不友好，加载所有的图片需要很久，影响到了网站用户体验；
    """
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    for image_src in image_list:
        download_img(image_src)


def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian{}.html'
    start_page = int(input('请输入其实页码： '))
    end_page = int(input('请输入结束页码： '))
    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        time.sleep(2)


if __name__ == '__main__':
    main()
