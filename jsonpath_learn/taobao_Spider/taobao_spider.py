# coding=utf-8

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import http.cookiejar

# 登录界面
# https://login.taobao.com/member/login.jhtml

# 接口
# https://rate.taobao.com/feedRateList.htm?auctionNumId=584469469152&userNumId=741345010&currentPageNum=2&pageSize=20&rate
# Type=&orderType=sort_weight&attribute=&sku=&hasSku=true&folded=0&ua=115%231qE3j11O1TN2tVk%2BT5F21CsoDCsISJhD1MMIcoa7d
# hh6AzRCnO0U13UHEf68ME%2F8taInDsz4%2BIbJ6XUxVL8wY7jQORVPeKFthwAFVcpPcsFcrvAfAhM0yrrQOSfyet1CuWNQiQWJHUFCvFwxoYpXyzFp9s
# AyetQ4yluIg%2FJRhiU8OWNcZYpXyrPQOjfyeKT4yWwOi%2FWJhEP193dKKEHLa4Ifvs%2BW1C0po9NR7aAIlLHhGsEMPVra5VOSa10zU33Ru%2Fp4Jl
# cXDluv5JxjWAJOWQfRUScij0oa6IqYZx0T%2BW6pE%2F2FWYwnN3L9btvLBTpgW505eqo6vpJ8CFl6Dd52e1tLzPQVp6WOmcahro654RV8DGdv3y24IdP
# QyPj3Mlukrl3Hqf9LeDnlZ5vDtnXO8W5NpdK90R1x4ZowWXqUjLtjHBQadcZaX6o3OJM%2FEAyEoeHLuQtXQMc%2FWzIaAvHUQDZK84BahH1wuorWtj9x9
# 1%2FuGizm3I3IbP9Xs2Af2jeYDzlw%2F9yz5D8IDSkbMlt3eAP9cwiETKmNazPhzQLJUzlBKHNYiU1MNy2zR66whuVuSSjH%2FVJAPmrWyZ9LbGO0ExQx
# iI%2FLeYhcVzRkI1jsjgAZe0u%2FmJ%2Fx%2B1s%2F8YbJRsQWq8vR%2ForV1nm2zO3quw1jb%2FR4CFQkoOyKDa%2BobGjtvAht9%2BV2qThZtNfeyp
# HI2v95QzkKMNC8iw2a2lXeNhazg1Qb1MYhKl1glVcZKiRBAlpWZI1TZNjrBtqri6yCzsSrH8uKH0YVYPnJIP%2BgBHMBoq3QxF%2FwkfxgOYsss4thzQ
# SRuZDrR6vR5ePBMVyLT2DwKkSsc2N6ZA%2FIPpe5JZZJIVi77SW2TYPZAVn0E4DV20qZL8mlaCgY7peC3FKEex0BHOeNLHOQTd8QsGjL%2BhEz5F5x7U
# Ju2YPDy13u41XR64GSfYMr23TbxSPFCWTs8d9zZYuPkqXw7656O1l91mHD%2FjuT9jFB4QnrPJ8g2c1%2B3AoDSbV%3D&_ksTS=1549974318401_13
# 97&callback=jsonp_tbcrate_reviews_list

#  currentPageNum=2

# url
# https://rate.taobao.com/feedRateList.htm?auctionNumId=584469469152&userNumId=741345010&currentPageNum=2&pageSize=20
def main():
    cj = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cj)
    url = 'https://rate.taobao.com/feedRateList.htm?' \
          'auctionNumId=584469469152&userNumId=741345010&currentPageNum=2&pageSize=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 '
                      'Safari/537.36 Core/1.63.5914.400 SLBrowser/10.0.3098.400',

    }
    opener = urllib.request.build_opener(handler)


if __name__ == '__main__':
    main()
