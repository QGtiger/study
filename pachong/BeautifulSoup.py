# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request,urllib.parse
import re

def main():
    keyword=input('请输入关键词：')
    keyword=urllib.parse.urlencode({'word':keyword})
    #print(type(keyword))
    
    print('http://baike.baidu.com/search/word?%s' % keyword)
    rep=urllib.request.urlopen('http://baike.baidu.com/search/word?%s' % keyword)
    html=rep.read()
    soup=BeautifulSoup(html,'html.parser')
    n=10
    for each in soup.find_all(href=re.compile("item")):
        content=each.text
        #print(content)
        url2=''.join(['http://baike.baidu.com',each['href']])
        #print(url2)
        rep2=urllib.request.urlopen(url2)
        html2=rep2.read()
        #print(html2)
        soup2=BeautifulSoup(html2,'html.parser')
        if soup2.h2:
            content+=soup2.h2.text
        content=''.join([content,'->',url2])
        print(content)
        n-=1
        if n<0:
            break
        

if __name__=='__main__':
    main()
