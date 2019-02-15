# coding=utf-8

import urllib.request
import urllib.parse
import re


def handle_request(url, page=None):
    # 拼接出来指定的url
    if page is not None:
        url = url + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/70.0.3538.67 Safari/537.36',
    }
    # print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_text(a_href):
    # 调用函数构建请求对象
    request = handle_request(a_href)
    # 发送请求，获取响应
    content = urllib.request.urlopen(request).read().decode()
    pattern = re.compile(r'<li>(.*?)</li>', re.S)
    lt = pattern.findall(content)
    # print(type(lt))
    # 写个正则，将内容里面所有的图片全部去掉
    pat = re.compile(r'<img .*?>')
    text = pat.sub('', str(lt))
    # print(lt)
    # exit()
    # print(type(text))
    # print(text)
    return text


def parse_content(content):
    """
    <h3><a href="/lizhi/qianming/20190241231.html">
    <b>当你感到累的时候，其实你是在走上坡路——加油励志经典语录</b></a></h3>
    :param content:
    :return:
    """
    pattern = re.compile(r'<h3><a href="(/lizhi/qianming/\d+\.html)"><b>(.*?)</b></a></h3>')
    lt = pattern.findall(content)
    # 返回的lt是一个列表，列表中的元素都是元组，元组中第一个元素就是正则中第一个小括号匹配到的内容，元组中第二个元素就是正则中第二个小括号匹配到的内容

    # 遍历列表
    for href_title in lt:
        # 获取连接内容
        a_href = 'http://www.yikexun.cn' + href_title[0]
        # print(a_href)
        # 获取标题
        title = href_title[-1]
        # 向a_href发送请求，获取响应内容
        text = get_text(a_href)
        # 写到html文件中
        new_text = str(text).strip().replace('[\'', '').replace(']\'', '').replace('\'', '').split('\r\n')[0].strip().split('</div>')[0].replace('<p>\\r\\n\\t\\t\\t\\t', '').split('<a')[0].replace(',', '')
        # print(new_text)
        # print(new_text.__len__())
        # exit()

        string = '<h1>%s</h1>%s' % (title, new_text)
        with open("lizhi.html", 'a', encoding='utf-8') as fp:
            fp.write(string)


def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input('请输入其实页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page+1):
        request = handle_request(url, page=page)
        # return request
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        

if __name__ == '__main__':
    main()
