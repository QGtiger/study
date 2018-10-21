# -*- coding:gbk -*-
"""
author:lightfish
Time:2018.10.21
note:csv���ļ��洢�����ǻ�����������������
ԭ���ǣ��������һ���ǵ������ļ���������⡣�ڼ������Ļ����£�EXCEL�򿪵�CSV�ļ�Ĭ��
��ANSI���룬���CSV�ļ��ı��뷽ʽΪutf-8��Unicode�ȱ�����ܾͻ�����ļ�����������
���������ʹ�ü��±���CSV�ļ����ļ�-���Ϊ�����뷽ʽѡ��ANSI
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

