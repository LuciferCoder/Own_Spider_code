# coding=utf-8
"""
执行js代码
"""

from   selenium import webdriver
import time

path = r'F:\gitHubRepos\spiderLearn\selenium_test\cao_pantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe'
url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv.html'

browser = webdriver.PhantomJS(path)
browser.get(url)
time.sleep(3)
with open(r'.\phantomjs\tupian1.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)

js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)
with open(r'.\phantomjs\tupian2.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)

browser.quit()



