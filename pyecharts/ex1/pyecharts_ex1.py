"""
author:lightfish
Time:2018.11.7
note:学习pyecharts
"""
import numpy as np
import pandas as pd
from pyecharts import Bar
from pyecharts.engine import create_default_environment

title = 'bar chart'
index = pd.date_range('7/11/2018',periods=6,freq='M')
df1 = pd.DataFrame(np.random.randn(6),index=index)
df2 = pd.DataFrame(np.random.randn(6),index=index)
print(index)
print(df1.values)

dtvalue1 = [i[0] for i in df1.values]
dtvalue2 = [i[0] for i in df2.values]

print(df1.index)

bar=Bar(title,'Profit and loss situation')
#提供更多使用工具  is_more_utils=True
bar.add('Profit',index,dtvalue1,is_more_utils=True)
bar.add('loss',index,dtvalue1)

env = create_default_environment('png')

bar.render(path=r'E:\python_project\pyecharts\ex2.html')

