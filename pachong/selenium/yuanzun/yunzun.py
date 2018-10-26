"""
author:lightfish
Time:2018.10.24
note:做一个实时爬取《元尊》的最新章节，并第一时间发送微信
"""
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import weixin
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

#无头浏览器的设置（无界面）
chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser,10)

index_url = 'https://www.ddbiquge.com'
headers={'User-Agent':UserAgent(verify_ssl=False).random}

def download_txt(txt_name,url):
    with open(txt_name+'.txt','w')as f:
        browser.get(url)
        html = browser.page_source
        soup = BeautifulSoup(html,'lxml')
        #print(soup.find(attrs={'id':'content'}).get_text().replace(url,'').replace('天才一秒记住本站地址：www.ddbiquge.com。顶点笔趣阁手机版阅读网址：m.ddbiquge.com','').replace('\xa0','\n').replace('　　','\n\n'))
        f.write('\t\t'+txt_name.split('\\')[1]+'\n\n')
        f.write(soup.find(attrs={'id':'content'}).get_text().replace(url,'').replace('天才一秒记住本站地址：www.ddbiquge.com。顶点笔趣阁手机版阅读网址：m.ddbiquge.com','').replace('\xa0','\n').replace('　　','\n\n\t'))



def get_page(url,i,check):
    print('checking %dth' % i)
    i+=1
    html = requests.get(url, headers)
    html = html.text
    soup = BeautifulSoup(html,'html.parser')
    name = soup.find('dd').get_text()
    check1 = soup.find('dd').get_text().split(' ')[1]
    if check1 == check:
        print('暂无更新,最新章为',check1)
        with open('yuanzun.txt','a+') as f:
            x=time.localtime()
            f.write(str(datetime.datetime(x[0],x[1],x[2],x[3],x[4],x[5]))+ '\n暂无更新,最新章为 '+check1+'\n')
            f.write('='*80+'\n')
        #weixin.send_msg('暂无更新,最新章为'+check1)
    else:
        print('元尊更新(已下载):  '+check1)
        with open('yuanzun.txt','a+') as f:
            x = time.localtime()
            f.write(str(datetime.datetime(x[0],x[1],x[2],x[3],x[4],x[5]))+ '\n元尊更新:  '+check1+'\n')
            f.write('=' * 80+'\n')
        download_txt('元尊\\' +name, index_url+soup.find('dd').find('a').attrs['href'])
        weixin.send_msg('元尊更新(已下载):  '+check1)
    check = check1
    time.sleep(1200)
    get_page(url,i,check)


if __name__=='__main__':
    url = 'https://www.ddbiquge.com/'
    i = 1
    html = requests.get(url, headers)
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('dd').get_text()
    check = soup.find('dd').get_text().split(' ')[1]
    download_txt('元尊\\' +name, index_url+soup.find('dd').find('a').attrs['href'])

    get_page(url,i,check)

