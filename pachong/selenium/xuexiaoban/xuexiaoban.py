"""
author:lightfish
Time:2018.10.24
note:爬取b站的《工作细胞》的短评
"""
import requests
from fake_useragent import UserAgent
import json
import pandas as pd
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser,10)
headers = { 'User-Agent': UserAgent(verify_ssl=False).random,
            'Referer':'https//www.bilibili.com/bangumi/media/md102392/?from=search&seid=6645420277974835286'
            }
comment_api = 'https://bangumi.bilibili.com/review/web_api/short/list?media_id=102392&folded=0&page_size=20&sort=0'

# 发送get请求
#response_comment = requests.get(comment_api,headers = headers)
browser.get(comment_api)
json_comment = browser.page_source
#json_comment = response_comment.text
soup = BeautifulSoup(json_comment,'lxml')
json_comment = soup.find('pre').get_text()
print(json_comment)
json_comment = json.loads(json_comment)

total = json_comment['result']['total']

cols = ['author','score','disliked','likes','liked','ctime','score','content','last_ep_index','cursor']
dataall = pd.DataFrame(index = range(total),columns = cols)


j = 0
while j <total:
    n = len(json_comment['result']['list'])
    for i in range(n):
        dataall.loc[j,'author'] = json_comment['result']['list'][i]['author']['uname']
        dataall.loc[j,'score'] = json_comment['result']['list'][i]['user_rating']['score']
        dataall.loc[j,'disliked'] = json_comment['result']['list'][i]['disliked']
        dataall.loc[j,'likes'] = json_comment['result']['list'][i]['likes']
        dataall.loc[j,'liked'] = json_comment['result']['list'][i]['liked']
        x = json_comment['result']['list'][i]['mtime']
        t = time.gmtime(int(x))
        dataall.loc[j,'ctime'] = str(datetime.datetime(t[0],t[1],t[2],t[3],t[4],t[5]))
        dataall.loc[j,'content'] = json_comment['result']['list'][i]['content']
        dataall.loc[j,'cursor'] = json_comment['result']['list'][n-1]['cursor']
        j+= 1
    try:
        dataall.loc[j,'last_ep_index'] = json_comment['result']['list'][i]['user_season']['last_ep_index']
    except:
        pass

    comment_api1 = comment_api + '&cursor=' + dataall.loc[j-1,'cursor']
    print(comment_api1)
    #response_comment = requests.get(comment_api1,headers = headers)
    #json_comment = response_comment.text
    browser.get(comment_api1)
    json_comment = browser.page_source
    soup = BeautifulSoup(json_comment, 'lxml')
    json_comment = soup.find('pre').get_text()
    json_comment = json.loads(json_comment)

    if j % 50 ==0:
        print('已完成 {}% !'.format(round(j/total*100,2)))
    time.sleep(0.5)


dataall.to_csv('血小板.csv',index=False)
"""
dataall = dataall.fillna(0)

def getDate(x):
    x = time.gmtime(x)
    return(pd.Timestamp(datetime.datetime(x[0],x[1],x[2],x[3],x[4],x[5])))

dataall['date'] = dataall.ctime.apply(lambda x:getDate(x))
"""

