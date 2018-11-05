"""
author:lightfish
Time:2018.10.30
note:爬取顶点笔趣阁小说《元尊》
"""
import requests
import pymysql
import re
from bs4 import BeautifulSoup

index_url='https://read.douban.com'



from fake_useragent import UserAgent
headers = {
    'User-Agent': UserAgent(verify_ssl=False).random
}

def get_page(url):
    url = index_url+url
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    try:
        text = soup.find(attrs={'class':'abstract-full'}).get_text()[:2000]
    except:
        text = soup.find(attrs={'class': 'info'}).get_text()[:2000]
    return text


def down_page(html,bk_type,bk_type_type,index):
    soup = BeautifulSoup(html,'lxml')
    items = soup.find_all(attrs={'class':'store-item'})
    for item in items:
        bk_name = item.find(attrs={'class':'title'}).find('a').get_text()
        bk_type = bk_type
        bk_type_type = bk_type_type
        bk_img = item.find(attrs={'class':'shadow-cover'}).find('img').attrs['src']
        bk_author = item.find(attrs={'class':'title'}).next_sibling.get_text()[:50]
        try:
            bk_score = item.find(attrs={'class':'rating-average'}).get_text()
        except:
            bk_score = 'none'
        bk_content = get_page(item.find(attrs={'class':'title'}).find('a').attrs['href'])

        book_list = (index,bk_type,bk_type_type,bk_name,bk_img,bk_author,bk_score,bk_content,False,'none','none','none',False,'none')
        sava_to_mysql(book_list,index)
        index +=1

def sava_to_mysql(list,con):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='library'
    )
    cursor = conn.cursor()
    sqli = 'insert into booktest_book_list values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    print('loading {}th {}...'.format(str(con),list[3]))
    cursor.execute(sqli,list)
    cursor.close()
    conn.commit()
    conn.close()

def main():
    for i in range(0,200,20):
        t = requests.get('https://read.douban.com/kind/117?start={}'.format(i), headers=headers)
        t.encoding = 'utf-8'
        print(t.text)
        index = i+1+200
        down_page(t.text, '小说', '言情', index)


