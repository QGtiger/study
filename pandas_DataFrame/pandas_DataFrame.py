import pandas as pd
#通过二维数组的建立
df1=pd.DataFrame([['Den','Aql','Rek'],[89,6,90]])
print(df1)

# 通过字典创建dataframe的要求：字典的value要求：一维数组或者单一数据
# 字典的键作为列索引
# 字典的数据作为列数据
# index没有显示指定时，创建range(0,len(dict))
dic={'数学':[25.1,26,27,28],'语文':98,'名字':['Dkd','Hff','Zfs','Lghgd']}
df2=pd.DataFrame(dic)
table=pd.DataFrame(df2)
#需要安装openpyxl,to_excel()函数
table.to_excel("app2.xlsx")
print(df2)
print("==================行索引===================")
print(df2.index)
print("==================列索引===================")
print(df2.columns)
print("=============dataframede值===================")
print(df2.values)
# 重置行索引的值
df2.index=["one","two","three","four"]
print(df2)
print('==================')
#可以直接通过列索引获取指定列的数据， eg: df[column_name]
#如果需要获取指定行的数据的话，需要通过ix方法来获取对应行索引的行数据，eg: df.ix[index_name]
print(df2['名字'])
# 通过列索行获取一整列的值
print(df2.ix['one'])
print("=========================")
print(df2.ix[['one','three'],'名字'])
# 通过列索引，修改整一列的值
df2['数学']=[98,98,98,98]
print(df2)
print('=========================')
# 通过行索引修改整行的数值
df2.ix['one']=[100,100,'Drt']
print(df2)

print(df2.loc['one'])
print(df2.iloc[1])