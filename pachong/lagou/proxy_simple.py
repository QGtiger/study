"""
author:lightfish
Time:2018.11.13
note:简易代理池的创建
66ip 西祠代理
西祠代理：  http://www.xicidaili.com/nn/
66ip：  http://www.66ip.cn

IP地址的正则表达式
"""
# -*- coding:utf-8 -*-

import re
import time
import urllib
import random
from lxml import etree
import requests
import json

def get_proxy(page):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    res = requests.get('http://www.xicidaili.com/nn/{}'.format(page),headers=headers)
    html = res.text
    ip_list = re.findall('<tr class.*?>.*?<td>(.*?)</td.*?<td>(.*?)</td>',html,re.S)
    print(len(ip_list))
    proxy_list=[]
    for ip in ip_list:
        proxy_list.append(':'.join(ip))
    return proxy_list

def proxy_read(proxy_list,i):
    proxy = proxy_list[i]
    print('当前代理IP：{}'.format(proxy))
    sleep_time = random.randint(1,2)
    print("等待{}秒".format(sleep_time))
    time.sleep(sleep_time)
    print('开始测试...')

    proxies = {
        'http':'http://'+proxy,
        'https':'https://'+proxy
    }
    headers = {
        'Connection': 'close',
    }
    try:
        res = requests.get('http://httpbin.org/ip',headers=headers,proxies=proxies,timeout=5)
        j = json.loads(res.text)
        if j['origin']:
            print('设置代理成功,IP为{}\n'.format(j['origin']))
            with open(r'C:\Users\Administrator\Desktop\proxy\proxy1.txt','a') as f:
                f.write(proxy+'\n')
    except Exception as e:
        print(e)
        print('当前ip不可用\n')


def get_proxy_2():
    proxy_t=[]
    with open(r'C:\Users\Administrator\Desktop\proxy\proxy.txt') as f:
        for line in f:
            p = line.replace('\n','')
            proxy_t.append(p)
    print(proxy_t)
    return proxy_t
if __name__=='__main__':
    for x in range(1,10):
        proxy_list = get_proxy(x)
        #ip = ['221.7.162.108:8123', '116.62.204.38:9999', '61.138.33.20:808', '118.190.95.35:9001', '101.64.32.100:808', '182.88.166.8:8123']
        useful_proxy=[]
        for i in range(len(proxy_list)):
            print('正在测试第{}个IP'.format(i+1))
            proxy = proxy_read(proxy_list,i)
            # if proxy:
            #     useful_proxy.append(proxy)
