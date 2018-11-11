"""
author:lightfish
Time:2018.11.11
note:3D散点图的绘制
"""
from pyecharts import Scatter3D
import numpy as np

scantter = Scatter3D("3D散点状态图",width=1200,height=600)
data = [[np.random.randint(0,100),np.random.randint(0,100),np.random.randint(0,100)] for _ in range(100)]
scantter.add("",data,is_visualmap=True)
scantter.render(r'E:\python_project\pyecharts\ex6.html')
