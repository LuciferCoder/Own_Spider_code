# coding=utf-8
# use xpath
from lxml import etree

#生成对象
tree = etree.parse("xpath.html")
# ret = tree.xpath('//div[@class="tang"]/ul/li[@class="love" and @name="yang"]')
# ret = tree.xpath('//div[@class="tang"]/ul/li[contains(@class, "l")]')
# ret = tree.xpath('//li[contains(text(),"爱")]/text()')
# ret = tree.xpath('//li[starts-with(@class,"b")]')
ret = tree.xpath('//div[@class="song"]')
string = ret[0].xpath('string(.)')
print(string.replace('\n', '').replace(' ', ''))
print(type(string))
