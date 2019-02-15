# coding=utf-8
import json

lt = [
    {'name': '王宝强', 'age': '30'},
    {'name': '贾乃亮', 'age': '36'},
    {'name': '马蓉蓉', 'age': '33'},
    {'name': '宋吉吉', 'age': '40'},
    {'name': '李小璐', 'age': '43'},
]

# 刘晓庆
# dumps,loads
# string = json.dumps(lt)
# # print(string)
# json_ltl = json.loads(string)
# print(json_ltl)

# dump,load
json.dump(lt, open('json.txt','w',encoding='utf8'))
obj = json.load(open('json.txt','r',encoding='utf8'))
print(type(obj))
print(obj)