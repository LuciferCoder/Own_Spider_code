# coding=utf-8

import requests

"""
若果碰到回话相关的问题，首先要创建一个对话
Sesssion:
会话；工作阶段；一段时间
    往下的所有操作都通过s进行访问：s.get   s.post
"""

s = requests.Session()

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019162357984 '
url = 'http://www.renren.com/969538686/profile'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.67 Safari/537.36',
}

# formdata={
# email	13261924736
# icode	业横如少
# origURL	http://www.renren.com/home
# domain	renren.com
# key_id	1
# captcha_type	web_login
# password	32af899f4a673b0f0e9c1a15ee5227c6b8513362bf55f729ad461a231fef6ed7
# rkey	c5c08b36d1daef7b10b7ae3c886850e6
# f	https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DYuGlMeaW6B7nowg9spc2boVVf1yvUPqACoAr6M9FhWa%26wd%3D%26eqid%3Dd5c35b4e0001e877000000025c682ec5
# }

r = s.post(url=post_url,headers=headers)
# r = requests.get(url=post_url,headers=headers, data=formdata)
r = s.get(url=url, headers=headers)
# 之后的访问通过s.get来访问就可以了
print(r.text)
