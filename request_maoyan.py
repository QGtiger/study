# -*- coding:gbk -*-
"""
author:lightfish
Time:2018.10.21
note:csv的文件存储，但是会出现中文乱码情况。
原因是：此种情况一般是导出的文件编码的问题。在简体中文环境下，EXCEL打开的CSV文件默认
是ANSI编码，如果CSV文件的编码方式为utf-8、Unicode等编码可能就会出现文件乱码的情况。
解决方法：使用记事本打开CSV文件，文件-另存为，编码方式选择ANSI
"""
import csv
import requests
import json

html=requests.get('http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset=0&startTime=2018-10-18%2020%3A58%3A51')
try:
    text = html.content
    json_text = json.loads(text.decode('utf-8'))
    list_info = []
    for item in json_text['cmts']:
        time = item['startTime']
        name = item['nickName']
        score = item['score']
        content = item['content']
        list = [time, name, score, content]
        list_info.append(list)
    print(list_info)
    print(type(list_info))

    with open(r'data/data.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for x in list_info:
            writer.writerow(x)
except:
    print('something error')

