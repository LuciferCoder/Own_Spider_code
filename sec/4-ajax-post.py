# coding=utf-8

import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
city = input('请输入要查询的城市：')
keyword = input('请输入要查询的关键字：')
page = input('请输入要查询第几页：')
size = input('请输入要多少个：')

# 表单数据
formdata = {
    'cname': city,
    'pid': '',
    'keyword': keyword,
    'pageIndex': page,
    'pageSize': size,
}
# headers
headers = {
    'Accept': 'application/json,text/javascript,*/*;q=0.01',
    # 'Accept - Encoding': 'gzip, deflate',
    'Accept-Language': 'zh - CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '80',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie': 'WT_FPC=id=298975ca492ceed5c0a1548001061091:' \
              'lv=1548127611964:ss=1548127611963;' \
              'Hm_lvt_1039f1218e57655b6677f30913227148=1548001061,1548127612;' \
              'Hm_lpvt_1039f1218e57655b6677f30913227148=1548127612;' \
              'KLBRSID=a34b6eb1eda6f7a05724ede2e440cdc7|1548127794|1548127611',
    'Host': 'www.kfc.com.cn',
    'Origin': 'http://www.kfc.com.cn',
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

request = urllib.request.Request(url=post_url, headers=headers)
# 构建表单数据
formdata = urllib.parse.urlencode(formdata).encode()

response = urllib.request.urlopen(request, data=formdata)

#打印获取的数据
print(response.read().decode())
