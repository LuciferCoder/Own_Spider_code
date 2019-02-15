# coding=utf-8
import urllib.request
import urllib.parse
import os
import re


def handle_request(url, page):
    url = url + str(page) + '/?s=5162013'
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/70.0.3538.67 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def download_image(content):
    patern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', re.S)
    # print(image_url)
    lt = patern.findall(content)
    # 遍历列表，依次下载图片
    for image_src in lt:
        image_src = 'https:' + image_src
        # 发送请求，下载图片
        # 创建文件夹
        dirname = 'qiutu'
        filename = image_src.split("/")[-1]
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filepath = dirname + '/' + filename
        print('正在下载：' + filename + '...')
        if not os.path.exists(filepath):
            urllib.request.urlretrieve(image_src, filepath)
        print(filename + '下载完毕！')


def get_end_page(root_url):
    request = handle_request(root_url, 1)
    content = urllib.request.urlopen(request).read().decode()
    patern = re.compile(r'<span class="page-numbers">.*?</span>', re.S)
    lt = patern.findall(content)
    return re.compile(r'\d+').findall(lt[-1])[0]


def main():
    #?s=5162013
    root_url = 'https://www.qiushibaike.com/pic/'
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入其实页码：'))
    if start_page <= 0:
        print('起始页码有误：页码数字小鱼等于0！\n请重新运行程序输入合法的页数！')
        exit(-1)
    end_page = int(input('请输入结束页码：'))
    e_p = get_end_page(url)
    if end_page > int(e_p):
        print('结束页码有误：页码数字小鱼等于0！\n请重新运行程序输入合法的页数！')
        print('最大页数为：' + e_p)
        exit(-1)
    # print(int(get_end_page(url)))
    for page in range(start_page, end_page+1):
        # 生成请求对象
        request = handle_request(url, page)
        # 发送请求对象，获取相应内容
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容，提取所有的图片链接，下载图片
        download_image(content)
    

if __name__ == '__main__':
    main()
