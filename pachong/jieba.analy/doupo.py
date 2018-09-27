"""
time:2018.9.27
author:lightfish
爬取网址http://www.doupoxs.com/doupocangqiong，爬取斗破，并用jieba.analyse分析数据
"""
import requests
import re
import time
import jieba.analyse

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def get_info(url):
    res=requests.get(url,headers=headers)
    if(res.status_code==200):
        contents=re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        #print(contents)
        for i in range(1,len(contents)):
            f.write(contents[i].replace('&ldquo;','')+'\n')
    else:
        pass

if __name__=='__main__':
    f = open('doupo.txt', 'a+')
    urls=['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,20)]
    for url in urls:
        get_info(url)
    f.seek(0, 0)
    content=f.read()
    try:
        #jieba.analyse.set_stop_words('word_stop.txt')
        tags=jieba.analyse.extract_tags(content,topK=100,withWeight=True)
        for item in tags:
            print(item[0]+'\t'+str(int(item[1]*1000)))
    finally:
        pass

f.close()



