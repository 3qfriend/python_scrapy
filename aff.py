#coding:utf-8

from bs4 import BeautifulSoup
import urllib2
from openpyxl import Workbook


count = 2
wb = Workbook()
ws =wb.active
#打开源代码模式打一种方法
#url='http://www.asiafashionfair.jp/custom_exhibitor/%E5%8D%97%E9%80%9A%E5%87%B1%E6%AC%A7%E5%9B%BD%E9%9A%9B%E8%B2%BF%E6%98%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/'

for url in urls:
    thtext=[]
    tdtext=[]
    text=[]
    text1=[]
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    source=response.read()
    response.close()

    soup =BeautifulSoup(source)
    thtext = soup.find_all("th")
    tdtext = soup.find_all("td")

    length = len(thtext)

    for i in range(length):
        a = thtext[i].string
        text.append(a)

    for j in range(length):
        try:
            b = tdtext[j].string.lstrip()
        except AttributeError:
            b = tdtext[j].string

        text1.append(b)

    print text1[1]

    if count >1 :
        ws.append([text[i]for i in range(length)])
        count = count -1

    else:
        pass
    ws.append([text1[j]for j in range(length)])


wb.save('aff.xlsx')



