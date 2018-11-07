"""
author:lightfish
Time:2018.11.7
note:pyecharts的学习
"""
import numpy as np
from pyecharts import Pie
attr=['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1=[np.random.randint(10,20) for _ in range(6)]
v2=[np.random.randint(10,20) for _ in range(6)]

#title_pos 标题位置  title-color 标题颜色 page_title='网页标题栏的名称' title_top='bottom' 标题在下方
pie=Pie('饼状图-玫瑰图实例',title_pos='center',title_top='bottom',width=900)
pie.use_theme('dark')
#is_label_show 显示每个点的值 is_legend_show显示每个颜色的属性
# is_random为是否随即排列颜色列表（bool）
# radius为半径，第一个为内半径，第二个是外半径
# rosetype为是否展示成南丁格尔图:'radius' 圆心角展现数据半分比，半径展现数据大小;'area'圆心角相同，为通过半径展现数据大小(默认）
# label_text_size为调整标签字体大小
pie.add('商品A',attr,v1,center=[25,50],is_random=True,radius=[30,75],rosetype='radius')
pie.add('商品B',attr,v2,center=[75,50],is_random=True,radius=[30,75],rosetype='area',is_legend_show=True,is_label_show=True)

pie.render(r'E:\python_project\pyecharts\ex4.png')
