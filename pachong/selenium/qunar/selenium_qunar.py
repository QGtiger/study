"""
author:lightfish
Time:2018.10.15
note:爬取去哪儿网的攻略 网址：http://travel.qunar.com/travelbook/list.htm
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib import request
from PIL import Image
import re
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import pandas as pd
import pymongo

broswer = webdriver.Chrome()
wait = WebDriverWait(broswer,10)

def index_page(page):
    """
    爬取索引页
    :param page: 页码
    :return:
    """
    print('loading ',str(page),'th...')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'li>.tit>a')))
    html = broswer.page_source
    soup = BeautifulSoup(html,'html.parser')
    for item in soup.find_all(attrs={'class':'list_item'}):
        programme = {
            'title': item.find(attrs={'class':'tit'}).get_text(),
            'date':item.find(attrs={'class':'date'}).get_text()[:-2],
            'days':item.find(attrs={'class':'days'}).get_text() if item.find(attrs={'class':'days'}) else 'none',
            '推荐':item.find(attrs={'class':'trip'}).get_text() if item.find(attrs={'class':'trip'}) else 'none',
            '途径':item.find(attrs={'class':'places'}).get_text()[3:] if item.find(attrs={'class':'places'}) else 'none',
            '行程':item.find(attrs={'class':'places'}).next_sibling.get_text()[3:] if item.find(attrs={'class':'places'}) else 'none'
        }
        print(programme['title'])
        save_to_mongodb(programme)

    page-=1
    if page==0:
        return
    else:
        next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a.next')))
        next.click()
        index_page(page)


def save_to_mongodb(data):
    client = pymongo.MongoClient('localhost')
    db = client['mydb']
    taobao = db['qunar']
    try:
        if taobao.insert_one(data):
            print('存储到MongoDB成功!')
    except Exception:
        print('存储失败!')


if __name__=='__main__':

    while 1:
        page = input('Please input how many pages you want to get...\n')
        try:
            page = int(page)
            break
        except:
            print('Please input a number!')
            pass
    broswer.get('http://travel.qunar.com/travelbook/list.htm')
    index_page(page)

