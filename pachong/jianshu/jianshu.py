"""
时间：2018年9月20日 22：27
作者：lightfish
爬取内容：异步爬取简书网7日信息
爬取网址：https://www.jianshu.com/trending/weekly
"""
from lxml import etree
import requests
import pymongo
import re
import json
from multiprocessing import Pool

client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
redian=mydb['jianshuHotspot']

headers={
    'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
def get_url(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    url_infos=selector.xpath('//ul[@class="note-list"]/li')
    for url_info in url_infos:
        active_url=url_info.xpath('div/a/@href')[0]
        get_info('http://www.jianshu.com/'+active_url)

def get_info(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    author=selector.xpath('//span[@class="name"]/a/text()')[0]
    print(author)
    article=selector.xpath('//h1[@class="title"]/text()')[0]
    date=selector.xpath('//span[@class="publish-time"]/text()')[0]
    word=selector.xpath('//span[@class="wordage"]/text()')[0]
    view=re.findall('"views_count":(.*?),',html.text,re.S)[0]
    like=re.findall('"likes_count":(.*?),',html.text,re.S)[0]
    author_id=re.findall('{"id":(.*?),"slug"',html.text,re.S)[0]

    gain_url='https://www.jianshu.com/notes/{}/rewards?count=20'.format(author_id)
    wb_data=requests.get(gain_url,headers=headers)
    json_data=json.loads(wb_data.text)
    gain_count=json_data['rewards_count']
    #print(str(gain_count)+' '+article)

    include_list=[]
    include_url='https://www.jianshu.com/notes/{}/included_collections?page=1'.format(author_id)
    html=requests.get(include_url,headers=headers)
    #print(html.text)
    json_data=json.loads(html.text)['collections']
    for i in range(0,len(json_data)):
        include_list.append(json_data[i]['title'])

    info={
        'author':author,
        'article':article,
        'date':date,
        'word':word,
        'view_counts':view,
        'like_counts':like,
        'gain_counts':gain_count,
        'include':include_list
    }
    redian.insert(info)

if __name__=='__main__':
    urls=['http://www.jianshu.com/trending/weekly?page={}'.format(str(i)) for i in range(0,11)]
    for url in urls:
        get_url(url)

