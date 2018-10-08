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
from urllib.parse import quote
from pyquery import PyQuery as pq
import pandas as pd

browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)

def login(dict):
    browser.get('https://www.douban.com')
    try:
        user=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#form_email')))
        passwd=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#form_password')))
        login_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.bn-submit')))
        user.clear()
        passwd.clear()
        user.send_keys('15990184749')
        passwd.send_keys('qwer123qg')
        captcha_link=browser.find_element_by_id('captcha_image').get_attribute('src')
        request.urlretrieve(captcha_link,'capycha.jpg')
        Image.open('capycha.jpg').show()
        captcha_code=input('请输入验证码：')
        browser.find_element_by_id('captcha_field').send_keys(captcha_code)
        login_btn.click()
        search_movie=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#inp-query')))
        search_movie.clear()
        search_movie.send_keys('蚁人2')
        search_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#db-nav-sns > div > div > div.nav-search > form > fieldset > div.inp-btn > input[type="submit"]')))
        search_btn.click()
        movie_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#content > div > div.article > div.search-result > div:nth-child(3) > div:nth-child(1) > div.content > div > h3 > a')))
        movie_btn.click()
        browser.switch_to_window(browser.window_handles[1])
        comments_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#comments-section h2 .pl')))
        comments_btn.click()
        get_info(dict)
    except TimeoutException:
        browser.refresh()
def get_info(dict):

    print('just loading one...')
    html=browser.page_source
    print(browser.current_url)
    #print(html)
    doc=pq(html)
    EC.presence_of_element_located((By.CSS_SELECTOR,'.comment-item'))
    items=doc('#comments .comment-item').items()
    for item in items:
        print(item('.comment-info>a').html())
        dict['comment-info'].append(item.find('.comment-info>a').text())
        print(item.find('.comment-info>a'))
        dict['comment-star'].append(str(item.find('.comment-info span.rating').attr('class'))[7:8])
        dict['comment-date'].append(item.find('.comment-info span.comment-time').text().strip())
        dict['comment-vote'].append(item.find('.comment-vote span.votes').text())
        dict['comments'].append(item.find('.comment p').text())
    try :
        next_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#paginator  a:last-child')))
        next_btn.click()
        #get_info(dict)
    except TimeoutException:
        print('爬取达到上限！')

if __name__=='__main__':
    dict={
        'comment-info':[],
        'comment-star':[],
        'comment-date':[],
        'comment-vote':[],
        'comments':[]
    }
    login(dict)
    df=pd.DataFrame(dict)
    table=pd.DataFrame(df)
    table.to_excel('蚁人2影评.xlsx')