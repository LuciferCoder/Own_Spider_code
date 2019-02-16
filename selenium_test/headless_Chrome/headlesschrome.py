# coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
"""
google headless model
phantomjs 一般会被识别为爬虫，使用phantomjs可以更改头部，但是直接使用chrome-headless更方便
"""

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 驱动路径
path = r'F:\gitHubRepos\spiderLearn\selenium_test\headless_Chrome\chromedriver.exe'

# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

# 开始上网
url = 'http://www.baidu.com/'

browser.get(url)
time.sleep(3)

browser.save_screenshot('baidu.png')

browser.quit()

