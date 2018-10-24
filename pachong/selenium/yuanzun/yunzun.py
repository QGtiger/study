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
headers={'User-Agent':UserAgent(verify_ssl=False).random}


def get_page(url,i,check):
    print('checking %dth' % i)
    i+=1
    html = requests.get(url, headers)
    html = html.text
    soup = BeautifulSoup(html,'html.parser')
    check1 = soup.find('dd').get_text().split(' ')[1]
    if check1 == check:
        print('暂无更新,最新章为',check1)
        with open('yuanzun.txt','a+') as f:
            x=time.localtime()
            f.write(str(datetime.datetime(x[0],x[1],x[2],x[3],x[4],x[5]))+ '\n暂无更新,最新章为 '+check1+'\n')
            f.write('='*80)
        #weixin.send_msg('暂无更新,最新章为'+check1)
    else:
        print('元尊更新:  '+check1)
        with open('yuanzun.txt','a+') as f:
            x = time.localtime()
            f.write(str(datetime.datetime(x[0],x[1],x[2],x[3],x[4],x[5]))+ '\n元尊更新:  '+check1+'\n')
            f.write('=' * 80)
        weixin.send_msg('元尊更新:  '+check1)
    check = check1
    time.sleep(1200)
    get_page(url,i,check)


if __name__=='__main__':
    url = 'https://www.ddbiquge.com/'
    i = 1
    html = requests.get(url, headers)
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')

    check = soup.find('dd').get_text().split(' ')[1]


    get_page(url,i,check)

