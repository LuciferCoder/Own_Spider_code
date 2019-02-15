# coding=utf-8
from selenium import webdriver
import time
# phantomjs路径
path = r'F:\gitHubRepos\spiderLearn\selenium_test\cao_pantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

# 打开百度
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(2)
# 保存截图
browser.save_screenshot(r'.\phantomPic\baidu.png')

# 此方法不能直接使用而是在driver.save_screenshot(“screenshot_filename.png”)
# 内部就是调用get_screenshot_as_file实现的
# browser.get_screenshot_as_png('phantomPic\\baidu.png')

# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写文字
# 输入文字后悔在ajax作用下变换了界面
time.sleep(2)
my_input.send_keys('美女')
browser.save_screenshot(r'.\phantomPic\shuru.png')

# 搜索，使用browser.find_element_by_class_name()不可行，原因是class会变化，并且有多个class由空格分开
# 只填写最后一个既可以使用
# button = browser.find_element_by_id('su')
button = browser.find_element_by_class_name('s_btn')
button.click()
time.sleep(2)
# 保存截图
browser.save_screenshot(r'.\phantomPic\meinv.png')
# 找到图片点击
# image = browser.find_elements_by_class_name('op-img-address-link-imgs')[2]
# image.click()
# time.sleep(3)
# # 保存截图
# browser.save_screenshot(r'.\phantomPic\show.png')

browser.quit()
