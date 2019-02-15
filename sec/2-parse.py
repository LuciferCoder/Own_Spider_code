# coding=utf-8
import urllib.parse

url = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1547628861&di' \
      '=22db59909e49700d9ae105171903d8e6&src=http://b-ssl.duitang.com/uploads/item/201303/20/20130320140508_hLhjV.jpeg'

# url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=7&tn=78040160_15_pg&bar=&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&oq=%E5%91%A8%E6%9D%B0%E4%BC%A6%E4%BD%A0&rsv_pq=9307755300067a6c&rsv_t=7e35vE1PhOWjKigHjJvkRewpkX7v9N31hiKw%2FryGNWqSHcgLIhuj44%2B00p4rg5gDVTxhjsI&rqlang=cn

# url只能由特定的字符组成，字母、数字、下划线
# 如果出现其他的，比如$ 空格 中文等，就要对其进行编码
# response = urllib.parse.quote()

url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&rsv_pq=8691cd250001b59d&rsv_t=bcb3rPKKtKM2QJvgbc88%2FiUnYCtpseDPhdLxHZ3UXgQlrO3WHkS9QDCVLVg&rqlang=cn&rsv_enter=1&rsv_sug3=11&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&inputT=1526&rsv_sug4=1526"

url = 'http://www.baidu.com/index.html?name=狗蛋&pwd=123456'
ret = urllib.parse.quote(url)
print(ret)
# http%3A//www.baidu.com/index.html%3Fname%3D%E7%8B%97%E8%9B%8B%26pwd%3D123456
# http://tool.chinaz.com/tools/urlencode.aspx
# url站长工具
rett = urllib.parse.unquote(ret)
print(rett)
