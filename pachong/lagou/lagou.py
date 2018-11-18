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

class lagou(object):
    def __init__(self):
        headers={
            'Host':'www.lagou.com',
            'Referer':'https://www.lagou.com/jobs/list_Python?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Connection':'keep-alive'
        }
        self.session = requests.session()
        self.session.headers.update(headers)
        self.search_job_data=[]

    def search(self,kind,page):
        for i in range(1,int(page)+1):
            data={
                'first':'false',
                'pn':str(i),
                'kd':kind
            }
            proxies=[
                {'http':'http://180.118.243.244:61234','https':'https://180.118.243.244:61234'},
                {'http':'http://122.237.105.213:80','https':'https://122.237.105.213:80'},
                {'http':'http://111.224.100.7:808','https':'https://111.224.100.7:808'},
                {'http':'http://61.138.33.20:808','https':'https://61.138.33.20:808'}
            ]
            try:
                search_data = self.session.post(url='https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false',data=data)
            except Exception as e:
                print(e)
                break
            search_data.encoding='utf-8'
            if search_data.status_code==200:
                print('获取第{}页数据...{}%'.format(i,round(i/int(page)*100,2)))
                print(search_data.text)
                self._format_search_data(search_data.text)


    def _format_search_data(self,search_data):
        search_data = json.loads(search_data)
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
            self.search_job_data.append(job_data)
        time.sleep(100)
        #print(self.search_job_data)


if __name__=='__main__':
    lagou = lagou()
    kind = input('Please input what you want to get data: ')
    page = input('Please input how much you want to get:')
    lagou.search(kind,page)
    data = lagou.search_job_data
    df = pd.DataFrame(data,columns=['公司全名','公司简称','所在地','公司大小','要求学历','薪资','工作经验','福利待遇'])
    df.to_csv('{}工程师就业.csv'.format(kind),index=False)
