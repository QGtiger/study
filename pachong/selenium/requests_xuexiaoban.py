"""
author:lightfish
Time:2018.10.23
note:爬取b站的《工作细胞》的短评
"""
import requests
import time
import pandas as pd
import json
from fake_useragent import UserAgent
import datetime

headers={'User-Agent':UserAgent(verify_ssl=False).random}
def get_page(url,data,i):
    print('loading %dth page...' % i)
    if i == 300:
        return
    try:
        html = requests.get(url,headers)
    except:
        return
    html = html.text
    json_data = json.loads(html)
    for item in json_data['result']['list']:
        data['user'].append(item['author']['uname'])
        data['score'].append(item['user_rating']['score'])
        x=item['mtime']
        t=time.gmtime(int(x))
        data['time'].append(str(datetime.datetime(t[0],t[1],t[2],t[3],t[4],t[5])))
        data['content'].append(item['content'])
        data['avatar'].append(item['author']['avatar'])
    if json_data['result']['list'][19].get('cursor','p') == 'p':
        return
    url = 'https://bangumi.bilibili.com/review/web_api/short/list?media_id=102392&folded=0&page_size=20&sort=0&cursor='+json_data['result']['list'][19]['cursor']

    i+=1
    get_page(url,data,i)


if __name__=='__main__':
    url = 'https://bangumi.bilibili.com/review/web_api/short/list?media_id=102392&folded=0&page_size=20&sort=0'
    data={
        'user':[],
        'score':[],
        'time':[],
        'content':[],
        'avatar':[]
    }
    i = 1
    get_page(url,data,i)
    df = pd.DataFrame(data)
    table = pd.DataFrame(df)
    table.to_excel('工作细胞.xlsx')


