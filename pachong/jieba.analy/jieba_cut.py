"""
author:lightfish
Time:2018.10.9
note:进行简单的jieba模块学习
allowPOS是分词种词性，详细请阅读：https://blog.csdn.net/HHTNAN/article/details/77650128
"""
import jieba.analyse
import requests
import re
import time

# jieba.cut的默认参数只有三个,jieba源码如下
# cut(self, sentence, cut_all=False, HMM=True)
# 分别为:输入文本 是否为全模式分词 与是否开启HMM进行中文分词
seg_list = jieba.cut("我来到北京清华大学", cut_all=True, HMM=False)
print(seg_list)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False, HMM=True)
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

seg_list = jieba.cut("他来到了网易杭研大厦", HMM=False)
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

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
    #for url in urls:
        #get_info(url)
    f.seek(0, 0)
    content=f.read()
    try:

        # 当withWeight=True时,将会返回number类型的一个权重值(TF-IDF
        tags=jieba.analyse.extract_tags(content,topK=100,withWeight=True,allowPOS=('ns', 'n', 'vn', 'v','nr'))
        print(tags)
        for item in tags:
            print(item[0]+'\t'+str(int(item[1]*1000)))
        with open('extract_tag.txt','w') as f:
            for item in tags:
                f.write(item[0] + '\t' + str(int(item[1] * 1000))+'\n')
    finally:
        pass

    f.close()


