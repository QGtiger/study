# coding=utf-8
"""
爬取百度图片的高清原图
Author          : Qian
Created         : 2018-9-19
"""
import re
import sys
import urllib
import os
 
import requests
 
 
def get_onepage_urls(onepageurl):
    if not onepageurl:
        print('执行结束')
        return [], ''
    try:
        html = requests.get(onepageurl).text
        
    except Exception as e:
        print(e)
        pic_urls = []
        fanye_url = ''
        return pic_urls, fanye_url
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    fanye_urls = re.findall(re.compile(r'<a href="(.*?)" class="n">.*?</a>'), html)
    print(fanye_urls)
    fanye_url = 'http://image.baidu.com' + fanye_urls[0] if fanye_urls else ''
    return pic_urls, fanye_url
 
 
def down_pic(pic_urls,localPath):
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    """给出图片链接列表, 下载图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            string = str(i + 1) + '.jpg'
            with open(localPath + '%d.jpg' % i, 'wb')as f:
                f.write(pic.content)
          #  with open(string, 'wb') as f:
          #      f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue
 
 
if __name__ == '__main__':
    keyword = '林允儿'  # 关键词, 改为你想输入的词即可
    url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='
    url_init = url_init_first + urllib.parse.quote(keyword, safe='/')
    print(url_init)
    
    all_pic_urls = []
    onepage_urls, fanye_url = get_onepage_urls(url_init)
    all_pic_urls.extend(onepage_urls)
    print(len(all_pic_urls))
    fanye_count = 1  # 图片所在页数，下载完后调整这里就行
    n=3
    while n:
        n-=1
        down_pic(list(set(onepage_urls)),'e:/PythonPic/允儿%s/' % fanye_count)#保存位置也可以修改
        onepage_urls, fanye_url = get_onepage_urls(fanye_url)
        fanye_count += 1
        print('第%s页' % fanye_count)
        if fanye_url == '' and onepage_urls == []:
            print(fanye_count)
            break
        #all_pic_urls.extend(onepage_urls)
        

    print(len(all_pic_urls))
    
    
