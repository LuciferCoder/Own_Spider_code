# coding=utf-8

import re

# string = '<p><div><span>猪八戒</span></div></p>'
# pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')

# string = '<div>如来富足</div><div></div>'


string = '''hate is a beautiful feel
love you very much
love she
love ger'''

string1 = """<div>沁园春-雪
北国风光
千里冰封
万里雪飘
望长城内外
惟余莽莽
大河上下
顿失滔滔
山舞银蛇
原驰蜡象
欲与天公试比高
</div></div>"""
# r'<(\w+)><(\w+)>\w+</\2></\1>' d 的 r
# pattern = re.compile(r'<div>.*</div>')

# pattern = re.compile(r'^love', re.M)

pattern = re.compile(r'<div>(.*?)</div>', re.S)
# ret = pattern.search(string)
ret = pattern.findall(string1)


# print(ret)

def fn(a):
    ret = int(a.group())
    # print(a)
    return str(ret - 10)


# string = 'i love you, you love me, ye'
# pattern = re.compile(r'love')
string = '我喜欢身高为170的女孩'

pattern = re.compile(r'\d+')
print(pattern.sub(fn, string))

# ret = pattern.sub('hate', string)
# ret = re.sub(pattern, 'hate', string)
# ret = re.sub(fn, string)
# print(ret)
