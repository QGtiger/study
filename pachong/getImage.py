#-*- coding: utf-8 -*-
'''
2018年9月18日22：45
爬去网址：https://tieba.baidu.com/p/5431979599?pn=1
'''

import os
import requests
from bs4 import BeautifulSoup

folder='每日一练之爬取图片'
if not os.path.exists(folder):
    os.makedirs(folder)

def download(url,n):
    res=requests.get(url)
    with open(folder+'/'+str(n)+'.jpg','wb') as f:
        f.write(res.content)

n=1
for i in range(1,3):
    base_url='https://tieba.baidu.com/p/5304029228?pn=1'+str(i)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47'}
    soup_tieba=BeautifulSoup(requests.get(base_url).text,'html.parser')
    img_list=soup_tieba.find_all('img',attrs={'class':'BDE_Image'})

    for img in img_list:
        print('第'+str(n)+'张图片爬取中...')
        src=img.get('src')
        print(src)
        download(src,n)
        n+=1

print('OK')
        
    
    
