"""
author:lightfish
Time:2018.10.17
note:爬取猫眼电影中的《悲伤逆流成河》，用直接登录网址 http://maoyan.com/films/1217236只能爬取十条
短评。切换成手机模式就能爬取更多短评
"""
import requests
import os
import json
import csv
import pandas as pd
header={
    'Host':'m.maoyan.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47'

}
def get_page(url,offset,data):
    html = requests.get(url,headers=header)
    if html.status_code==200:
        print('loading offset:',offset)
        json_data = json.loads(html.text)
        get_data(json_data,data)
    else:
        print('Something Error!')

def get_data(info,data):
    json_response = info['cmts']
    print(len(json_response))

    for item in json_response:
        data['评论日期'].append(item['startTime'][:10].strip())
        data['昵称'].append(item['nickName'])
        data['所在城市'].append(item['cityName'])
        data['评分'].append(item['score'])
        data['猫眼等级'].append(item['userLevel'])
        data['评论'].append(item['content'])




if __name__=='__main__':
    offset = 0
    startTime = '2018-10-18'
    data={
        '评论日期':[],
        '昵称':[],
        '所在城市':[],
        '评分':[],
        '猫眼等级':[],
        '评论':[]
    }
    urls=['http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={0}&startTime={1}%2020%3A58%3A51'.format(x,startTime) for x in range(0,1000,15)]
    for offset,url in enumerate(urls):
        get_page(url,offset*15,data)
    df = pd.DataFrame(data)
    table=pd.DataFrame(df)
    table.to_excel(r'E:\python_project\weather\data\maoyan.xlsx')