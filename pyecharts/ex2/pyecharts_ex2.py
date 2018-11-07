"""
author:lightfish
Time:2018.11.7
note:学习pyecharts，mark_line 和 mark_point属性

"""
from pyecharts import Bar
import numpy as np
month = ['{}月'.format(i) for i in range(1,13)]
#round函数，去小数点前几位
v1 = [round(np.random.uniform(10,20),2) for _ in range(12)]
v2 = [round(np.random.uniform(10,20),2) for _ in range(12)]

bar = Bar('柱状图实例')

#mark_line=['average']：顾名思义就是画一条虚线表示平均值
#mark_point=['max','min']：顾名思义就是标识最大最小值
bar.add('蒸发量',month,v1,mark_line=['average'],mark_point=['max','min'])
bar.add('降水量',month,v2,mark_line=['average'],mark_point=['max','min'])

bar.render(r'E:\python_project\pyecharts\ex3.html')
bar.render(r'E:\python_project\pyecharts\ex3.png')