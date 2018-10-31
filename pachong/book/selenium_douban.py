"""
author:lightfish
Time:2018.10.8
note:对豆瓣蚁人2的评论爬取，爬取其评论人、星级、评价日期、有用个数、评价正文
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib import request
from PIL import Image
import re
import time
from bs4 import BeautifulSoup
import pandas as pd
import Mysql_yuanzun


browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)

def login():
    browser.get('https://www.douban.com')
    try:
        user=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#form_email')))
        passwd=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#form_password')))
        login_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.bn-submit')))
        user.clear()
        passwd.clear()
        time.sleep(2)
        user.send_keys('15990184749')
        time.sleep(4)
        passwd.send_keys('qwer123qg')
        try:
            captcha_link=browser.find_element_by_id('captcha_image').get_attribute('src')
            request.urlretrieve(captcha_link,'capycha.jpg')
            Image.open('capycha.jpg').show()
            captcha_code=input('请输入验证码：')
            time.sleep(1)
            browser.find_element_by_id('captcha_field').send_keys(captcha_code)
        except:
            print('不需要输入验证码！')
            pass

    except TimeoutException:
        browser.refresh()
def get_info(dict):

    print('just loading one...')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.comment-item')))
    html=browser.page_source
    print(browser.current_url)
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all(attrs={'class':'comment-item'})
    print(items)
    print(type(items))
    for item in items:
        print(type(item))
        #print(item)
        dict['comment-info'].append(item.find(attrs={'class':'comment-info'}).find('a').get_text())
        star=re.findall('<span .*?allstar(.*?)0.*?</span>',str(item))
        dict['comment-star'].append(star[0] if len(star) else '')
        dict['comment-date'].append(item.find(attrs={'class':'comment-time'}).get_text().strip())
        dict['comment-vote'].append(item.find(attrs={'class':'votes'}).get_text())
        dict['comments'].append(item.find('p').get_text())
    try :
        next_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#paginator  a:last-child')))
        next_btn.click()
        get_info(dict)
    except TimeoutException:
        print('爬取达到上限！')

if __name__=='__main__':
    login()
    for i in range(0,200,20):
        browser.get('https://read.douban.com/kind/117?start={}'.format(i))
        html = browser.page_source
        index = 200+i+1
        Mysql_yuanzun.down_page(html, '小说', '言情', index)