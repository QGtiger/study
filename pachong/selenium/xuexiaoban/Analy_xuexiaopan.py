import pandas as pd
import matplotlib.pyplot as plt
import datetime

f = open('血小板.csv')
df1 = pd.read_csv(f)

#print(df1.columns)
#df1['ctime'].apply(lambda x: x.split(' ')[0])
#print(df1['ctime'])
#print(df1.loc[4,'ctime'].split(' ')[0])

df2 = df1['ctime'].apply(lambda x:x.split(' ')[0])
df3 = df2.value_counts()


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

