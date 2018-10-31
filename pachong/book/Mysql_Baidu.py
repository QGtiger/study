"""
author:lightfish
Time:2018.10.31
note:爬取百度阅读中的言情小说
"""
import requests
import pymysql
import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

index_url='https://yuedu.baidu.com'
chrome_options = Options()
chrome_options.add_argument('--headless')
broswer = webdriver.Chrome(chrome_options=chrome_options)
wait =WebDriverWait(broswer,10)


from fake_useragent import UserAgent
headers = {
    'User-Agent': UserAgent(verify_ssl=False).random
}

def get_page(url):
    url = index_url+url
    broswer.get(url)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.book-intro-block')))
    except:
        pass
    r = broswer.page_source
    soup = BeautifulSoup(r,'lxml')
    try:
        bk_score = soup.find(attrs={'class':'doc-info-score-value'}).get_text()[:10]
    except:
        bk_score='none'


    try:
        bk_content = soup.find(attrs={'class':'book-intro-block'}).get_text()[:2000].replace('\n','')
    except:
        bk_content = '暂无，尽请期待(难讷)...'
    return (bk_score,bk_content)


def down_page(html,bk_type,bk_type_type,index):
    soup = BeautifulSoup(html,'lxml')
    items = soup.find_all(attrs={'class':'book'})
    for item in items:
        #time.sleep(0.5)
        _url = item.find('a').attrs['href']
        #print(_url)

        bk_name = item.find(attrs={'class': 'title'}).get_text()
        bk_img = item.find('img').attrs['data-src']
        #print(bk_img)
        bk_author = '作者 ' + item.find(attrs={'class':'author'}).get_text()[:48]

        book_list = (index,bk_type,bk_type_type,bk_name,bk_img,bk_author)+get_page(_url)+(False,'none','none','none',False,'none')

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
    a={'1001':'企业管理','1010':'经济金融','1003':'投资理财','1004':'市场营销','1015':'财会统计'}
    for y,x in enumerate(list(a.keys())):
        for i in range(0,100,20):

            t = requests.get('https://yuedu.baidu.com/book/list/{}?od=0&show=0&pn={}'.format(str(x),i), headers=headers)
            t.encoding='gbk'
            #soup = BeautifulSoup(t.text,'html.parser')
            #print(soup.find_all(attrs={'class':'title'}))
            index = i+1840+y*100
            down_page(t.text, '经济管理', a[str(x)], index)

if __name__=='__main__':
    #get_page('https://yuedu.baidu.com/ebook/475784e8de80d4d8d15a4ff4?fr=booklist')
    main()
