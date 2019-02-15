# coding=utf-8
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json


# https://sou.zhaopin.com/?jl=530&kw=Python&kt=3
# https://sou.zhaopin.com/?p=2&jl=530&kw=Python&kt=3


class ZhilianSpider(object):
    # url中不变的内容，要拼接朱合成完成的url
    url = 'http://sou.zhaopin.com/?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/70.0.3538.67 Safari/537.36',
    }

    def __init__(self, jl, kw, start_page, end_page):
        # 将上面的参数都保存为自己的成员属性
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page

    # 根据page拼接指定的url，然后生成请求对象
    def handle_request(self, page):
        data = {
            'jl': self.jl,
            'kw': self.kw,
            'p': page,
            'kt': '3',
        }
        url_now = self.url + urllib.parse.urlencode(data)
        # print(urllib.parse.urlencode(data))
        # print(url_now)
        request = urllib.request.Request(url=url_now, headers=self.headers)
        return request

    # 爬取程序
    def run(self):
        # 搞个循环，循环爬取每一页的数据
        for page in range(self.start_page, self.end_page + 1):
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read().decode()
            self.parse_content(content)

        # 将列表数据保存到文件中
        string = json.dumps(self.items)
        with open('zhilian.txt', 'w', encoding='utf8') as fp:
            fp.write(string)

    # 解析内容
    def parse_content(self, content):
        # 生成对象
        soup = BeautifulSoup(content)


def main():
    jl = input('请输入工作地点： ')
    kw = input('请输入工作关键字： ')
    start_page = int(input('请输入其实页码： '))
    end_page = int(input('请输入结束页码： '))

    # 创建爱你对象，启动安排去程序
    spider = ZhilianSpider(jl, kw, start_page, end_page)
    spider.run()


if __name__ == '__main__':
    main()
