"""
author:lightfish
Time:2018.11.12
note:分析工作细胞
"""
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pyecharts import Bar,Pie,Page
import time

f = open(r'E:\python_project\weixin\血小板.csv')
df1 = pd.read_csv(f)


page = Page()
df2 = df1['ctime'].apply(lambda x:x.split('/')[1])
df3 = df2.value_counts()
print(df3)
month = ['{}月'.format(x) for x in df3.index]

df2 = df1['ctime'].apply(lambda x:x.split(' ')[0])
days = df2.apply(lambda x:time.strftime('%A',time.strptime(x,'%Y/%m/%d')))
days = days.value_counts()
print(days)

bar = Bar('工作细胞柱状图',title_pos='center',width=900)
bar.add("",month,df3.values,mark_point=['max','min'],is_visualmap=True)
page.add(bar)

bar1 = Bar('工作细胞一周内的评论情况',title_pos='center',title_top='bottom',width=900)
bar1.add("",days.index,days.values,mark_point=['max','min'],mark_line=['average'])
page.add(bar1)

pie = Pie("工作细胞圆饼图",title_pos='center',width=900,title_top='bottom')
pie.add("",month,df3.values,is_label_show=True,is_legend_show=True,radius=[30,75])
page.add(pie)


page.render('工作细胞.html')
'''
day_list = sorted(list(df3.index),key=lambda x:datetime.datetime.strptime(x,'%Y/%m/%d').timestamp())
print(df3)
print(df3['2018/7/8'])
list1 = list(map(lambda x:x.split('/',1)[1],day_list))
list2=[]
for i,x in enumerate(list1):
    if i%15==0:
        list2.append(list1[i])
    else:
        list2.append('')

plt.title('Commentary heat')
plt.bar(list(map(lambda x:x.split('/',1)[1],day_list)),df3[day_list])
for x,y in zip(list1,df3[day_list]):
    plt.text(x,y+25,y,ha='center',va='top')
plt.xticks(list1,list2)
plt.xlabel('Date of review')
plt.ylabel('Number of comments')

plt.show()
'''
