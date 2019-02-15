# coding=utf-8
from bs4 import BeautifulSoup

# 生成对象
soup = BeautifulSoup(open('soup_test.html', encoding='utf8'), 'lxml')

# print(soup)
# print(soup.a)
# print(soup.div)
# print(soup.a['href'])
# print(soup.a['title'])
# print(soup.a['target'])
# print(soup.a.attrs)
# print(soup.a.attrs['href'])
# print('*****' * 10)
# print(soup.a.html)
# print('*****' * 10)
# print(soup.a.text)
# print('*****' * 10)
# print(soup.a.string)
# print('*****' * 10)
# print(soup.a.get_text())
# print('*****' * 10)
# print('*****' * 10)
#
#
# print(soup.div.text)
# print('*****' * 10)
# print(soup.div.string)
# print('*****' * 10)
# print(soup.div.get_text())
#
# print('*****' * 10)
# print('*****' * 10)

# print(soup.find('a'))
# print(soup.find('a', title='qin'))
# print(soup.find('a', alt='qi'))
# print(soup.find('a', class_="du"))
# print(soup.find('a', id="feng"))

# print(soup.find('a', class_="du"))

# div = soup.find('div', class_="tang")
# # print(type(div))
# print(div.find('a', class_="du"))
# lt = soup.find_all('a')
# print(type(lt))
# print(lt)
# print(len(lt))

div = soup.find('div', class_="tang")
# print(div.find_all('a'))
# print(div.find_all(['a', 'b']))
# print(div.find_all('a', limit=2))
# print(soup.select('.tang > ul > li > a')[2])
# print(soup.select("#feng")[0].text)
# print(soup.select("#feng")[0]['href'])
print(div.select('.du'))