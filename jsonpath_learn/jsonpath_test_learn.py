# coding=utf-8
# pip isntall jsonpath
import json
import jsonpath
# 将json格式字符串转化为Python对象
obj = json.load(open('book.json', 'r', encoding='utf8'))

# 商店里所有书的作者
# ret = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(type(ret))
# print(ret)

# 	所有作者
# ret = jsonpath.jsonpath(obj, '$..author')
# print(type(ret))
# print(ret)

# 所有的东西都在商店里，有一些书和一辆红色自行车。
# ret = jsonpath.jsonpath(obj, '$.store.*')
# print(ret)

# 	商店里所有东西的价格。  $.store..price
# 所有的东西都在商店里，有一些书和一辆红色自行车。
# ret = jsonpath.jsonpath(obj, '$.store..price')
# print(ret)

# 最后一本书
ret = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# $..book[-1:]  最后一本书
print(ret)

# 前两本书
# $..book[0,1]
# $..book[:2]

# 过滤所有ISBN编号的书籍
# $..book[?(@.isbn)]

# 过滤所有低于10的书籍
# $..book[?(@.price<10)]

# XML文档中的所有元素。所有JSON结构的成员。
# $..*