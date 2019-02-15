# coding=utf-8

from selenium import webdriver
import time

# 模拟创建一个浏览器对象，然后通过对象去操作浏览器
path = r'F:\gitHubRepos\spiderLearn\jsonpath_learn\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)

url = 'http://www.baidu.com/'
# 打开连接
browser.get(url)

# print(browser)
time.sleep(2)

# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写文字
# 输入文字后悔在ajax作用下变换了界面
my_input.send_keys('美女')
time.sleep(2)

# 搜索，使用browser.find_element_by_class_name()不可行，原因是class会变化，并且有多个class由空格分开
# 只填写最后一个既可以使用
# button = browser.find_element_by_id('su')
button = browser.find_element_by_class_name('s_btn')
button.click()
time.sleep(2)
# 找到图片点击
image = browser.find_elements_by_class_name('op-img-address-link-imgs')[2]
image.click()
time.sleep(3)

# 退出浏览器
browser.quit()

