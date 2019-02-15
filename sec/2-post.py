# coding=utf-8

import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'
# word = input('请输入您要搜索的单词：')
# 'sign': '275695.55262',
# 'token': '7f0ccf4952ab4548d8862aa40b5e37d9',
# 以上两个参数需要读懂代码进行破解
formdata = {
    'sign': '275695.55262',
    'simple_means_flag': '3',
    'token': '7f0ccf4952ab4548d8862aa40b5e37d9',
    'from': 'en',
    'transtype': 'realtime',
    'query': 'wolf',
    'to': 'zh',
}

headers = {
    'Host': 'fanyi.baidu.com',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '120',
    # 'Accept': '*/*',
    'Origin': 'https://fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.67 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://fanyi.baidu.com/?aldtype=85',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BAIDUID=E65A26ACA8F1B594CF1A012F889863E1:FG=1; '
              'BIDUPSID=E65A26ACA8F1B594CF1A012F889863E1; '
              'PSTM=1546947993; '
              'locale=zh;'
              ' to_lang_often=%5B%7B%22value%22%3A%22'
              'en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D;'
              ' REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1;'
              ' from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%'
              '22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D;'
              ' BDORZ=FFFB88E999055A3F8A630C64834BD6D0; '
              'BDRCVFR[mkUqnUt8juD]=aeXf-1x8UdYcs; '
              'delPer=0; H_PS_PSSID=1431_27210_21105_28329_28132_28267;'
              ' PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1547920390,1547996722; '
              'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1547996722',
}

request = urllib.request.Request(url=post_url, headers=headers)
formdata = urllib.parse.urlencode(formdata).encode()
response = urllib.request.urlopen(request, formdata)
print(response.read().decode())
