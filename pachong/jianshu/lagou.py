"""
时间：2018年9月20日 22：30
作者：lightfish
爬取内容：异步爬取简书用户动态信息
爬取网址：https://www.jianshu.com/users/9104ebf5e177/timeline

"""
import pymongo
import requests
from lxml import etree

client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
timeline=mydb['test']
headers={
    'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

def get_timeline_info(url,page):
    user_id=url.split('/')
    user_id=user_id[4]
    print(user_id)
    if url.find('page='):
        page=page+1
    html=requests.get(url,headers=headers)
    #print(html.text)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        dd=info.xpath('div/div/div/span/@data-datetime')[0]
        #print(dd)
        type=info.xpath('div/div/div/span/@data-type')[0]
        timeline.insert({'data':dd,'type':type})

    id_infos=selector.xpath('//ul[@class="note-list"]/li/@id')
    if len(infos)>1:
        feed_id=id_infos[-1]
        max_id=feed_id.split('-')[1]
        next_url='http://www.jianshu.com/users/%s/timeline?max_id=%s&page=%s' % (user_id,max_id,page)
        print(next_url)
        get_timeline_info(next_url,page)
if __name__=='__main__':
    get_timeline_info('https://www.jianshu.com/users/9104ebf5e177/timeline',1)


