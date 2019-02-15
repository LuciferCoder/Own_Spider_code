# coding=utf-8
import urllib.parse

url = 'http://www.baidu.com/index.html?namegoudan&age=18&sex=nv&height=180'

# 假如参数有 name age sex height
name = 'goudan'
age = '18'
sex = 'nv'
height = '180'

data = {
    "name": name,
    "sex": sex,
    "age": age,
    "height": height,
    "weight": 180,
}

query_string = urllib.parse.urlencode(data)
print(query_string)

# 遍历字典
# lt = []
# for k, v in data.items():
#     lt.append(k + "=" + str(v))
# query_string = "&".join()

url = url + "?" + query_string
#
print(url)
