import requests
from pyquery import PyQuery as pq
import json
import csv
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.zhihu.com/explore'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47'
}
'''
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
    question=item.find('h2').text()
    author=item.find('.author-link').text()
    answer=pq(item.find('.content').html()).text()
    with open('explore.txt','a',encoding='utf-8') as f:
        f.write('\n'.join(['问题:\t'+question,'提问者:\t'+author,'回答:\t'+answer]))
        f.write('\n'+'='*50+'\n')
'''
#json数据的存储
data=[{
    'name':'钱根',
    'gender':'male',
    'birthday':'1997-12-11'
}]
with open('data.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data,indent=2,ensure_ascii=False))

#csv文件的存储
url='http://maoyan.com/board/4?/offset=0'
content=requests.get(url,headers=headers).text
soup=BeautifulSoup(content,'html.parser')
moive_name=soup.find_all(class_='name')
moive_score=soup.find_all(class_='score')
moive_releasetime=soup.find_all(class_='releasetime')
f=open('data.csv','a',encoding='gbk')
writer=csv.writer(f)
writer.writerow(['电影','上映时间','评分'])
for i in range(0,len(moive_name)):
    writer.writerow([moive_name[i].get_text(),moive_releasetime[i].get_text()[5:],moive_score[i].get_text()])
f.close()
#pandas从CSV中读取数据
print(pd.read_csv('data.csv',encoding='gbk'))

