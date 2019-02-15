# coding=utf-8

lt = [{'name': '宫本武藏\n小田纯一郎'}]

# with open('lala.txt', 'w', encoding='utf8') as fp:
#     fp.write(str(lt))

fp = open('lala.txt', 'r', encoding='utf8')
string = fp.read()
fp.close()

# 下面的这种强制转换是不可以的，每一个都会被分开来
lt = list(string)
print(lt)

# 使用下面的这个方法读取来，可以正常使用
lt1 = eval(string)
print(lt1)
print(lt1[0]['name'])
