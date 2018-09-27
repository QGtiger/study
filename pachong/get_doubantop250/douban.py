"""
time:2018.9.27
author:lightfish
爬取豆瓣top250书籍
"""
from lxml import etree
import requests
import csv

fp=open('doubanbook.csv','w',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))

urls=['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

for url in urls:
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//tr[@class="item"]')
    for info in infos:
        name=info.xpath('td/div/a/@title')[0]
        url=info.xpath('td/div/a/@href')[0]
        author_r=info.xpath('td/p/text()')[0]
        author=author_r.split('/')[0]
        publisher=author_r.split('/')[-3]
        date=author_r.split('/')[-2]
        price=author_r.split('/')[-1]
        rate=info.xpath('td[2]/div[2]/span[2]/text()')[0]
        comments=info.xpath('td/p/span/text()')
        comment=comments[0] if len(comments)!=0 else 'empty!'
        writer.writerow((name,url,author,publisher,date,price,rate,comment))

fp.close()