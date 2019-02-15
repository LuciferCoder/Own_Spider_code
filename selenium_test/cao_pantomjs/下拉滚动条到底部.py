# coding=utf-8
from selenium import webdriver
import time

path = r'F:\gitHubRepos\spiderLearn\selenium_test\cao_pantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://movie.douban.com/subject_search?search_text=%E5%8A%A8%E4%BD%9C&cat=1002'
browser.get(url)
time.sleep(3)

# browser.save_screenshot(r'.\phantomPic\douban1.png')
# 让滚动条执行简单的js代码滚动到底部
js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(1)
# browser.save_screenshot(r'.\phantomPic\douban2.png')

# 获取网页代码
html = browser.page_source
with open(r'.\phantomjs\douban.html', 'w', encoding='utf8') as fp:
    fp.write(html)

browser.quit()
