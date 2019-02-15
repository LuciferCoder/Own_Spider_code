# coding=utf-8
import urllib.request
"""
    Python3将urllib和urllib2整合为一个urllib
    Python2的urllib对应Python3的urllib.request
    Python2的urllib2对应Python3的urllib.parse
"""
#url = 'http://www.baidu.com'
# 完整的url
# http://www.baidu.com:80/index.html?name=guodan&password=123#lala
#response = urllib.request.urlopen(url=url)
#with open('baidu.html', 'wb') as fp:
    #fp.write(response.read())

# 下载图片
# 图片只能写入到本地二进制格式
imageurl = 'https://img.zcool.cn/community/01c39159690c4da8012193a32b37b4.jpg@1280w_1l_2o_100sh.jpg'
#response = urllib.request.urlopen(imageurl)
#with open('qing.jpg', 'wb') as fp:
#    fp.write(response.read())
#   fp.close()
url = "http://www.aviva-cofco.com.cn/data/cms/archive/201812(4)/%E4%B8%AD%E8%8B%B1%E4%BA%BA%E5%AF%BF%E5%AE%89%E9%91%AB%E4%BC%A0%E5%AE%B6%E7%BB%88%E8%BA%AB%E5%AF%BF%E9%99%A9%E6%9D%A1%E6%AC%BE.pdf"
url1 = "http://www.aviva-cofco.com.cn/data/cms/archive/201811(3)/中英人寿乐相伴两全保险.pdf"
print(type(url1))
urllib.request.urlretrieve(url, "中英人寿乐相伴两全保险1.pdf")

