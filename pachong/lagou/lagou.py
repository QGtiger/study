"""
author:lightfish
Time:2018.11.18
note:爬去拉勾网的数据
"""
import requests
import json
import random
import pandas as pd
import numpy as np
import time
from urllib.parse import quote

headers={
            'Host':'www.lagou.com',
            'Referer':'https://www.lagou.com/jobs/list_Python?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Connection':'keep-alive'
        }

class lagou(object):
    def __init__(self,location):
        headers={
            'Host':'www.lagou.com',
            'Referer':'https://www.lagou.com/jobs/list_Python?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Connection':'keep-alive'
        }
        self.index_url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(quote(location))
        self.session = requests.session()
        self.session.headers.update(headers)
        self.search_job_data=[]
        self.proxy_list=[]
        self.get_proxy()
        self.proxy={
                'http':'http://61.160.247.63:808',
                'https':'https://61.160.247.63:808'
            }

    def get_proxy(self):
        with open(r'C:\Users\Administrator\Desktop\proxy\proxy1.txt') as f:
            for line in f:
                p = line.replace('\n','')
                self.proxy_list.append({'http':'http://'+p,'https':'https://'+p})
        print('总共有{}个代理IP'.format(len(self.proxy_list)))
        print(self.proxy_list)

    def search(self,kind,page):
        for i in range(1,int(page)+1):
            data={
                'first':'false',
                'pn':str(i),
                'kd':kind
            }
            # proxies=[
            #     {'http':'http://180.118.243.244:61234','https':'https://180.118.243.244:61234'},
            #     {'http':'http://122.237.105.213:80','https':'https://122.237.105.213:80'},
            #     {'http':'http://111.224.100.7:808','https':'https://111.224.100.7:808'},
            #     {'http':'http://61.138.33.20:808','https':'https://61.138.33.20:808'}
            # ]

            while True:

                try:
                    search_data = self.session.post(url=self.index_url,data=data,proxies=self.proxy,timeout=5)
                    is_get_data = json.loads(search_data.text)
                    if is_get_data['msg'] == '您操作太频繁,请稍后再访问':
                        raise Exception('当前IP已被禁...正在IP代理池中提取可用IP...')

                    break
                except Exception as e:
                    print('当前IP已被禁...正在IP代理池中提取可用IP...')
                    self.proxy = random.choice(self.proxy_list)
                    print('当前代理' + str(self.proxy))


            search_data.encoding = 'utf-8'
            if search_data.status_code == 200:
                print('获取第{}页数据...{}%'.format(i,round(i/int(page)*100,2)))
                print(search_data.text)
                self._format_search_data(search_data.text)


    def _format_search_data(self,search_data):
        try:
            search_data = json.loads(search_data)
        except Exception as e:
            print(e)
            return
        for item in search_data['content']['positionResult']['result']:
            job_data = []
            job_data.append(item['companyFullName'] if item['companyFullName'] else 'none')
            job_data.append(item['companyShortName'] if item['companyFullName'] else 'none')
            job_data.append(item['district'] if item['district'] else 'none')
            job_data.append(item['companySize'] if item['companySize'] else 'none')
            job_data.append(item['education'] if item['education'] else 'none')
            job_data.append(item['salary'] if item['salary'] else 'none')
            job_data.append(item['workYear'] if item['workYear'] else 'none')
            job_data.append(item['positionAdvantage'] if item['positionAdvantage'] else 'none')
            #print(job_data)
            self.search_job_data.append(job_data)
        print('不行太累了，我得休息下,Zzz...Zzz...Zzz...')
        #time.sleep(30)
        #print(self.search_job_data)


if __name__=='__main__':
    kind = input('Please input what you want to get data: ')
    location = input('Please input where you want to get: ')
    lagou = lagou(location)
    try_data = {
        'first': 'false',
        'pn': '1',
        'kd': kind
    }
    response =  requests.post(lagou.index_url,data=try_data,headers=headers)
    print(response.text)
    json_data = json.loads(response.text)
    totalCount = json_data['content']['positionResult']['totalCount']
    is_total_get = input('总共有{}条数据...是否全部爬取(Y/N): '.format(totalCount))
    if is_total_get.upper() == 'Y':
        page = int(totalCount/15)
        lagou.search(kind,page)
    else:
        page = input('Please input how much page you want to get:')
        lagou.search(kind, page)

    data = lagou.search_job_data
    df = pd.DataFrame(data,columns=['公司全名','公司简称','所在地','公司大小','要求学历','薪资','工作经验','福利待遇'])
    df.to_csv('{}{}工程师就业.csv'.format(location,kind),index=False)
