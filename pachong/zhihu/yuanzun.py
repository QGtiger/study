import requests
import re
from bs4 import BeautifulSoup
import time

def parse_one_page(html):
    pattern = re.compile('<dd>.*?a.*?href="(.*?)".*?>(.*?)</a>.*?</dd>',re.S)
    links = re.findall(pattern,html)
    return links

r=requests.get('https://www.xxbiquge.com/78_78513/')
r.encoding='UTF-8'
#print(soup.find_all('dd'))
links=parse_one_page(r.text)
print(links)
url='https://www.xxbiquge.com'
for x in range(437,len(links)):
    f=open(r'E:\python_project\元尊\元尊\\'+links[x][1]+'.txt','w',encoding='utf-8')
    t=requests.get(url+links[x][0])
    t.encoding='utf-8'
    soup=BeautifulSoup(t.text,'html.parser')
    f.write(soup.find(id='content').get_text())
    f.close()
    time.sleep(2)
    #print(soup.find(id='content').get_text())

