"""
author:lightfish
Time:2018.11.19
note:爬取网易云音乐
"""
import urllib.request
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import re
import os

chrome_options = Options()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser,10)


def get_page(url):
    browser.get(url)
    browser.switch_to_frame('g_iframe')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-table')))
    #print(browser.page_source)
    get_music_url(browser.page_source)


def get_music_url(html):
    pattern=re.compile('<a.*?href="/song.*?id=(.*?)">.*?title="(.*?)".*?>',re.S)
    result = re.findall(pattern,html)
    print(result)
    download_music(result)

def download_music(urls):
    path = input('Please input where you want to save: ')
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    for i,j in urls:
        print('loading {}...'.format(j))
        url='http://music.163.com/song/media/outer/url?id={}.mp3'.format(i)
        urllib.request.urlretrieve(url,'{}.mp3'.format(j))



if __name__=='__main__':

    while True:
        id = input('Please input id: ')
        if id.isdigit():
            index_url = 'https://music.163.com/#/artist?id={}'.format(id)
            break
        else:
            print('Please input a number')

    print(index_url)
    get_page(index_url)