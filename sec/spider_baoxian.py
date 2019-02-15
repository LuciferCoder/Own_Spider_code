# encoding:utf-8

from bs4 import BeautifulSoup
import urllib.request
import re
import urllib.parse
import os


class HtmlParder_pdf(object):
    # 1
    def __init__(self):
        self.url_list = set()
        self.filenames = set()

    # 2
    def parser(self, url):
        response = urllib.request.urlopen(url)
        html_cont = response.read()
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        return soup

    # 4
    def find_file_in_one_page(self, soup):
        pdf_url_in_One = soup.find_all('a', href=re.compile(r"/data/cms/."))
        return pdf_url_in_One

    # 7
    def get_next_page(self, soup):
        next_page_url = soup.find('a', id="next", href=re.compile(r'/website/xxzx/gkxxpl/gsjbxx/grbxtk/rsbx/.'))
        next_page_link = urllib.urlparse.urljoin(root_url, next_page_url['href'])
        return next_page_link

    def add_filenames(self, pdf_url_in_One):
        filename_list = self.filenames
        for link in pdf_url_in_One:
            pdf_url_in_One_link = urllib.parse.urljoin(root_url, link['href'])
            filename = pdf_url_in_One_link.split("/")[-1]
            filename_list.add(filename)

    # 5
    def add_url_list(self, url):
        for link in url:
            pdf_url_in_One_link = urllib.parse.urljoin(root_url, link['href'])
            self.url_list.add(pdf_url_in_One_link)

    # 6##########xxxxxxxxxxxxxxxxxx
    def download(self):
        # donwload 1 pdf and pop that url
        url = self.url_list.pop().encode("utf-8")
        urllib.request.urlretrieve(url=url, filename="1.pdf")

    # 3
    def hasnext_page(self, url):
        if url != None or len(url) != 0:
            return
        return False


if __name__ == '__main__':
    root_url = "http://www.aviva-cofco.com.cn/website/xxzx/gkxxpl/gsjbxx/grbxtk/rsbx/list-1.shtml"
    obj = HtmlParder_pdf()
    soup = obj.parser(root_url)
    # print soup
    count = 1

    file_list = obj.find_file_in_one_page(soup)
    # print file_list
    obj.add_url_list(file_list)
    obj.add_filenames(file_list)
    # obj.url_list
    # for i in range(0, list(obj.url_list).__len__()-2):
    obj.download()
    os.renames("1.pdf", "天地玄黄.pdf")

    next_url = obj.get_next_page(soup)
    print(next_url)
    root_url = next_url
    count = count + 1
    print(count)
